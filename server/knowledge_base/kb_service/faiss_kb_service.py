import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
import json

import os
import shutil

from configs import SCORE_THRESHOLD,METADATA_QUERY
from server.knowledge_base.kb_service.base import KBService, SupportedVSType, EmbeddingsFunAdapter
from server.knowledge_base.kb_cache.faiss_cache import kb_faiss_pool, ThreadSafeFaiss
from server.knowledge_base.utils import KnowledgeFile, get_kb_path, get_vs_path
from server.utils import torch_gc
from langchain.docstore.document import Document
from typing import List, Dict, Optional, Tuple

'''接入混合检索部分，加入bm25检索，并使用EnsembleRetriever进行混合检索'''
from langchain.retrievers import EnsembleRetriever,BM25Retriever,SelfQueryRetriever

# from langchain.retrievers.self_query.faiss import FAISSTranslator
from langchain.vectorstores import VectorStore
from langchain.chains.query_constructor.base import AttributeInfo
# from langchain.llms import OpenAI
# from langchain_community.llms.openai import OpenAI
from server.utils import get_OpenAI

class FaissKBService(KBService):
    vs_path: str
    kb_path: str
    vector_name: str = None
 
    def vs_type(self) -> str:
        return SupportedVSType.FAISS

    def get_vs_path(self):
        return get_vs_path(self.kb_name, self.vector_name)

    def get_kb_path(self):
        return get_kb_path(self.kb_name)

    def load_vector_store(self) -> ThreadSafeFaiss:
        return kb_faiss_pool.load_vector_store(kb_name=self.kb_name,
                                               vector_name=self.vector_name,
                                               embed_model=self.embed_model)

    def save_vector_store(self):
        self.load_vector_store().save(self.vs_path)

    def get_doc_by_ids(self, ids: List[str]) -> List[Document]:
        with self.load_vector_store().acquire() as vs:
            return [vs.docstore._dict.get(id) for id in ids]

    def del_doc_by_ids(self, ids: List[str]) -> bool:
        with self.load_vector_store().acquire() as vs:
            vs.delete(ids)

    def do_init(self):
        self.vector_name = self.vector_name or self.embed_model
        self.kb_path = self.get_kb_path()
        self.vs_path = self.get_vs_path()

    def do_create_kb(self):
        if not os.path.exists(self.vs_path):
            os.makedirs(self.vs_path)
        self.load_vector_store()

    def do_drop_kb(self):
        self.clear_vs()
        try:
            shutil.rmtree(self.kb_path)
        except Exception:
            ...

    def do_search(self,
                  query: str,
                  top_k: int,
                  score_threshold: float = SCORE_THRESHOLD,
                  ) -> List[Tuple[Document, float]]:
        # embed_func = EmbeddingsFunAdapter(self.embed_model)
        # embeddings = embed_func.embed_query(query)
        # with self.load_vector_store().acquire() as vs:
        #     docs = vs.similarity_search_with_score_by_vector(embeddings, k=top_k, score_threshold=score_threshold)
        embed_func = EmbeddingsFunAdapter()
        embeddings = embed_func.embed_query(query)
        '''基于metadata进行检索'''
        ###FAISSWITHMETADATA
        if METADATA_QUERY:
            with self.load_vector_store().acquire() as vs:
                # docs = vs.similarity_search_by_metadata(embed_func,embeddings, k=top_k,fetch_k=10) 
                # docs_meta = vs.similarity_search_with_score(query,k=top_k,fetch_k=10)
                docs_meta = vs.similarity_search_with_metadata_scores(query,k=top_k,fetch_k=10,score_threshold=score_threshold) 
        else:
            docs_meta = []
        # docs = rerank(query,docs) 
        # return docs_meta
        '''混合检索逻辑'''

        '''metadata field(创建元数据检索器)'''
        # metadata_field_info = [
        #     AttributeInfo(
        #         name="head1",
        #         description="文档的head1属性",
        #         type="string",
        #     ),
        #     AttributeInfo(
        #         name="head2",
        #         description="文档的head1属性",
        #         type="string",
        #     ),
        #     AttributeInfo(
        #         name="head3",
        #         description="文档的head1属性",
        #         type="string",
        #     ),
        #     AttributeInfo(
        #         name="head4",
        #         description="文档的head1属性",
        #         type="string",
        #     ),
        #     AttributeInfo(
        #         name="head5",
        #         description="文档的head1属性",
        #         type="string",
        #     ),   
        #     AttributeInfo(
        #         name="head6",
        #         description="文档的head1属性",
        #         type="string",
        #     ),           
        # ]
        # model = get_OpenAI(model_name="llama3-8b",temperature=0,max_tokens=2048)


        with self.load_vector_store().acquire() as vs:
            faiss_retriever = vs.as_retriever(
                search_type="similarity",
                search_kwargs={"score_threshold": score_threshold, "k": top_k})
            import jieba
            
            # cutter = Cutter()
            docs = list(vs.docstore._dict.values())
            bm25_retriever = BM25Retriever.from_documents(
                docs,
                preprocess_func=jieba.lcut_for_search,
            )
            bm25_retriever.k = top_k
            # self_query_retriever = SelfQueryRetriever.from_llm(model,vs,query,metadata_field_info)
            # self_query_retriever = SelfQueryRetriever.from_llm(llm=llm,vectorstore=vs,document_contents=query,metadata_field_info=metadata_field_info)
            # docs = self_query_retriever.invoke(query)
            ensemble_retriever = EnsembleRetriever(
                retrievers=[bm25_retriever, faiss_retriever], weights=[0.5, 0.5]
            )
        
        docs = ensemble_retriever.get_relevant_documents(query)
        #这里还有bug要改，一部分是带分数的，一部分是不带分数的
        docs = [(doc,-1) for doc in docs]
        return list({t[0].page_content: t for t in docs+docs_meta}.values())

    def do_add_doc(self,
                   docs: List[Document],
                   **kwargs,
                   ) -> List[Dict]:
        data = self._docs_to_embeddings(docs) # 将向量化单独出来可以减少向量库的锁定时间

        with self.load_vector_store().acquire() as vs:
            # ids = vs.add_embeddings(text_embeddings=zip(data["texts"], data["embeddings"]),
            #                         metadatas=data["metadatas"],
            #                         ids=kwargs.get("ids"))
            
            #FAISSWithMetadata
            if METADATA_QUERY:
                try:
                    ids = vs.add_embeddings(content_embeddings=data["embeddings_contents"],
                                            metadata_embeddings=data["embeddings_metadatas_title"],
                                            texts=data["texts"],
                                            metadatas=data["metadatas"],
                                            ids=kwargs.get("ids"))
                except:
                    print(data)
                    ids = vs.add_embeddings(content_embeddings=data["embeddings_contents"],
                                                                metadata_embeddings=data["embeddings_metadatas_title"],
                                                                texts=data["texts"],
                                                                metadatas=data["metadatas"],
                                                                ids=kwargs.get("ids"))                
            else:
                ids = vs.add_embeddings(text_embeddings=zip(data["texts"], data["embeddings"]),
                                        metadatas=data["metadatas"],
                                        ids=kwargs.get("ids")) 
               
            if not kwargs.get("not_refresh_vs_cache"):
                vs.save_local(self.vs_path)
        doc_infos = [{"id": id, "metadata": doc.metadata} for id, doc in zip(ids, docs)]
        torch_gc()
        return doc_infos

    # def do_delete_doc(self,
    #                   kb_file: KnowledgeFile,
    #                   **kwargs):
    #     with self.load_vector_store().acquire() as vs:
    #         ids = [k for k, v in vs.docstore._dict.items() if v.metadata.get("source").lower() == kb_file.filename.lower()]
    #         if len(ids) > 0:
    #             vs.delete(ids)
    #         if not kwargs.get("not_refresh_vs_cache"):
    #             vs.save_local(self.vs_path)
    #     return ids
    def do_delete_doc(self, kb_file, **kwargs):
        with self.load_vector_store().acquire() as vs:
            # 获取所有文档ID，检查其metadata["source"]是否与kb_file.filename匹配
            ids = [k for k, v in vs.docstore._dict.items() 
                if v.metadata.get("source") and v.metadata.get("source").lower() == kb_file.filename.lower()]
            
            # 如果匹配的ID存在，则删除这些文档
            if len(ids) > 0:
                vs.delete(ids)
            
            # 根据kwargs决定是否刷新vector store缓存
            if not kwargs.get("not_refresh_vs_cache"):
                vs.save_local(self.vs_path)
        
        return ids


    def do_clear_vs(self):
        with kb_faiss_pool.atomic:
            kb_faiss_pool.pop((self.kb_name, self.vector_name))
        try:
            shutil.rmtree(self.vs_path)
        except Exception:
            ...
        os.makedirs(self.vs_path, exist_ok=True)

    def exist_doc(self, file_name: str):
        if super().exist_doc(file_name):
            return "in_db"

        content_path = os.path.join(self.kb_path, "content")
        if os.path.isfile(os.path.join(content_path, file_name)):
            return "in_folder"
        else:
            return False

def dump_input(d):
    # print("\n")
    # print("=" * 30 + title + "  input " + "="*30)
    with open(output_logs,"a",encoding="utf-8") as f:
        f.write(("=" * 30  + "  input " + json.dumps(d, ensure_ascii=False, indent=4) +"="*30 + "\n"))
from server.reranker.reranker import LangchainReranker
from configs import (LLM_MODELS, 
                     VECTOR_SEARCH_TOP_K, 
                     SCORE_THRESHOLD, 
                     TEMPERATURE,
                     USE_RERANKER,
                     RERANKER_MODEL,
                     RERANKER_MAX_LENGTH,)
from server.utils import embedding_device
from server.utils import get_model_path
from server.knowledge_base.model.kb_document_model import DocumentWithVSId

def rerank(query,docs):
    # 加入reranker
    docs = [DocumentWithVSId(**x[0].dict(), id=x[0].metadata.get("id")) for x in docs]
    for i in range(len(docs)):
        if len(docs[i].page_content) > RERANKER_MAX_LENGTH:
            docs[i].page_content = docs[i].page_content[:RERANKER_MAX_LENGTH]
    reranker_model_path = get_model_path(RERANKER_MODEL)
    reranker_model = LangchainReranker(top_n=3,
                                    device=embedding_device(),
                                    max_length=RERANKER_MAX_LENGTH,
                                    model_name_or_path=reranker_model_path
                                    )
    print("-------------before rerank-----------------")
    print(docs)
    docs = reranker_model.compress_documents(documents=docs,
                                            query=query)
    print("------------after rerank------------------")
    print(docs)
    return docs

def dump_output(r):
    with open(output_logs,"a",encoding="utf-8") as f:
        f.write(r)
if __name__ == '__main__':
    # faissService = FaissKBService("test")
    # faissService.add_doc(KnowledgeFile("README.md", "test"))
    # faissService.delete_doc(KnowledgeFile("README.md", "test"))
    # faissService.do_drop_kb()
    # print(faissService.search_docs("如何启动api服务"))

    # faissService = FaissKBService("cloudResources")
    # faissService = FaissKBService("docx-test")
    # faissService = FaissKBService("pre-docx")
    # faissService = FaissKBService("docx-yun")
    faissService = FaissKBService("md-test")
    # docs = faissService.do_search(query="RUIJIERG-S6000E系列交换机，如何配置接口的索引永久化",top_k=4,score_threshold=5)
    # context = "\n".join([doc.page_content for doc in docs])
   
    test_json_path = r'D:/Langchain-Chatchat-master/notebooks/test_rag_data/rag_test_md.json'
    output_logs = r"D:/Langchain-Chatchat-master/tests/zhouh/outputs/rag_meta_query.txt"
    with open(test_json_path, 'r', encoding='utf-8') as file:
        json_list = json.load(file)
    for data in json_list:
        # data["query"] = data["query"]+",请生成配置指令代码"
        # data["query"] = json_list[6]["query"]
        # data["query"] = "CE与AR VPN对接采用EBGP方式对接，"
        # data["query"] = "绿色低碳运营的目标是啥，"
        # data["query"] = "如何配置 DNS 解析策略的A 类型信息（对内解析）"
        data["query"] = "RUIJIERG-S6000E系列交换机,如何开启接口索引永久化功能，即设备重启后接口索引不变"

        dump_input(data)
        docs = faissService.do_search(query=data["query"],top_k=4,score_threshold=0.7)
        context = "\n".join(["doc"+"\n"+doc[0].page_content+"\n" for doc in docs])
        break
        # with open(output_logs,"a",encoding="utf-8") as f:
        #     f.write("\n")
        #     f.write(json.dumps(context, ensure_ascii=False)+"\n")
        