from langchain.docstore.document import Document
from configs import EMBEDDING_MODEL, logger,METADATA_QUERY,CHUNK_SIZE,EMBEDDING_BATCH_SIZE
from server.model_workers.base import ApiEmbeddingsParams
from server.utils import BaseResponse, get_model_worker_config, list_embed_models, list_online_embed_models
from fastapi import Body
from fastapi.concurrency import run_in_threadpool
from typing import Dict, List
import torch

online_embed_models = list_online_embed_models()

def batch_embedding(texts: List[str], embed_model: str, to_query: bool, batch_size: int=64) -> List:
    embeddings = []
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]
        batch_embeddings = embed_texts(texts=batch_texts, embed_model=embed_model, to_query=to_query).data
        embeddings.extend(batch_embeddings)
        torch.cuda.empty_cache() 
    return embeddings

    
def embed_texts(
        texts: List[str],
        embed_model: str = EMBEDDING_MODEL,
        to_query: bool = False,
) -> BaseResponse:
    '''
    对文本进行向量化。返回数据格式：BaseResponse(data=List[List[float]])
    '''
    try:
        if embed_model in list_embed_models():  # 使用本地Embeddings模型
            from server.utils import load_local_embeddings

            embeddings = load_local_embeddings(model=embed_model)
            return BaseResponse(data=embeddings.embed_documents(texts))

        if embed_model in list_online_embed_models():  # 使用在线API
            config = get_model_worker_config(embed_model)
            worker_class = config.get("worker_class")
            embed_model = config.get("embed_model")
            worker = worker_class()
            if worker_class.can_embedding():
                params = ApiEmbeddingsParams(texts=texts, to_query=to_query, embed_model=embed_model)
                resp = worker.do_embeddings(params)
                return BaseResponse(**resp)

        return BaseResponse(code=500, msg=f"指定的模型 {embed_model} 不支持 Embeddings 功能。")
    except Exception as e:
        logger.error(e)
        return BaseResponse(code=500, msg=f"文本向量化过程中出现错误：{e}")


async def aembed_texts(
    texts: List[str],
    embed_model: str = EMBEDDING_MODEL,
    to_query: bool = False,
) -> BaseResponse:
    '''
    对文本进行向量化。返回数据格式：BaseResponse(data=List[List[float]])
    '''
    try:
        if embed_model in list_embed_models(): # 使用本地Embeddings模型
            from server.utils import load_local_embeddings

            embeddings = load_local_embeddings(model=embed_model)
            return BaseResponse(data=await embeddings.aembed_documents(texts))

        if embed_model in list_online_embed_models(): # 使用在线API
            return await run_in_threadpool(embed_texts,
                                           texts=texts,
                                           embed_model=embed_model,
                                           to_query=to_query)
    except Exception as e:
        logger.error(e)
        return BaseResponse(code=500, msg=f"文本向量化过程中出现错误：{e}")


def embed_texts_endpoint(
        texts: List[str] = Body(..., description="要嵌入的文本列表", examples=[["hello", "world"]]),
        embed_model: str = Body(EMBEDDING_MODEL,
                                description=f"使用的嵌入模型，除了本地部署的Embedding模型，也支持在线API({online_embed_models})提供的嵌入服务。"),
        to_query: bool = Body(False, description="向量是否用于查询。有些模型如Minimax对存储/查询的向量进行了区分优化。"),
) -> BaseResponse:
    '''
    对文本进行向量化，返回 BaseResponse(data=List[List[float]])
    '''
    return embed_texts(texts=texts, embed_model=embed_model, to_query=to_query)


def embed_documents(
        docs: List[Document],
        embed_model: str = EMBEDDING_MODEL,
        to_query: bool = False,
) -> Dict:
    """
    将 List[Document] 向量化，转化为 VectorStore.add_embeddings 可以接受的参数
    """
    texts = [x.page_content[0:CHUNK_SIZE] for x in docs]
    metadatas = [x.metadata for x in docs]

    metadatas_title_summary = []
    for metadata in metadatas:
        max_head_num = 0
        metadata_text = ""
        head_num = 0
        for key,value in metadata.items():
            if key.startswith("title"):
                metadata_text = value
                break
            if key.startswith("head") and key[4:].isdigit():
                head_num = int(key[4:])
            if head_num > max_head_num:
                max_head_num = head_num
                metadata_text = value
        metadatas_title_summary.append(metadata_text)

    ##batch-embedding
    embeddings = batch_embedding(texts=texts, embed_model=embed_model, to_query=to_query,batch_size=EMBEDDING_BATCH_SIZE)
    embeddings_metadatas_title = batch_embedding(texts=metadatas_title_summary, embed_model=embed_model, to_query=to_query, batch_size=EMBEDDING_BATCH_SIZE)
    # embeddings = embed_texts(texts=texts, embed_model=embed_model, to_query=to_query).data
    # if embeddings is None:
    #     print(embeddings)
    # embeddings_metadatas_title = embed_texts(texts=metadatas_title_summary, embed_model=embed_model, to_query=to_query).data
    # if embeddings is not None:
    #     return {
    #         "texts": texts,
    #         "embeddings": embeddings,
    #         # "embeddings_metadatas_title": embeddings_metadatas_title,
    #         "metadatas": metadatas,
    #    }

    # FAISSWithMetadata
    if embeddings is not None:
        if METADATA_QUERY:
            return {
                "texts": texts,
                "embeddings_contents": embeddings,
                "embeddings_metadatas_title": embeddings_metadatas_title,
                "metadatas": metadatas,
            }
        else:
            return {
            "texts": texts,
            "embeddings": embeddings,
            "metadatas": metadatas,
       }
