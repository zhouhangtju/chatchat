'''
Author       : your name
Date         : 2024-08-12 06:28:52
LastEditors  : your name
LastEditTime : 2024-08-12 07:18:44
FilePath     : /vector_stores/FaissWithMetaData.py
Description  : 
Copyright 2024 OBKoro1, All Rights Reserved. 
2024-08-12 06:28:52
'''
import json
import logging
import operator
import os
import pickle
import uuid
import warnings
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Sized,
    Tuple,
    Union,
)
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.faiss import dependable_faiss_import,_len_check_if_sized
from langchain_core.embeddings import Embeddings
import numpy as np
from langchain_core.documents import Document
from langchain_core.runnables.config import run_in_executor
from langchain_core.vectorstores import VectorStore

from langchain_community.docstore.base import AddableMixin, Docstore
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores.utils import (
    DistanceStrategy,
    maximal_marginal_relevance,
)


class FAISSWithMetadata(FAISS):
    def __init__(self, embedding_function: Embeddings, *args, **kwargs):
        super().__init__(embedding_function, *args, **kwargs)
        self.metadata_index = None
        self.content_index = None
        self.content_weight = kwargs.get('content_weight', 0.5)
        self.metadata_weight = 1 - self.content_weight

    @classmethod
    def from_texts(
        cls,
        texts: List[str],
        embedding: Embeddings,
        metadatas: Optional[List[dict]] = None,
        ids: Optional[List[str]] = None,
        **kwargs: Any
    ) -> "FAISSWithMetadata":
        # content_embeddings, metadata_embeddings = cls._get_embeddings_with_metadata(texts, metadatas, embedding)
        instance = super().from_texts(texts, embedding, metadatas=metadatas, ids=ids, **kwargs)
        embeddings = embedding.embed_documents(texts)
        instance.content_index = cls._create_faiss_index(embeddings)
        instance.metadata_index = cls._create_faiss_index(embeddings)
        
        return instance

    @staticmethod
    def _get_embeddings_with_metadata(texts: List[str], metadatas: List[dict], embedding: Embeddings) -> Tuple[List[List[float]], List[List[float]]]:
        metadatas_title_summary = []
        for metadata in metadatas:
            max_head_num = 0
            metadata_text = ""
            for key, value in metadata.items():
                if key.startswith("head") and key[4:].isdigit():
                    head_num = int(key[4:])
                    if head_num > max_head_num:
                        max_head_num = head_num
                        metadata_text = value
            metadatas_title_summary.append(metadata_text)

        content_embeddings = embedding.embed_documents(texts)
        metadata_embeddings = embedding.embed_documents(metadatas_title_summary)
        
        return content_embeddings, metadata_embeddings

    @staticmethod
    def _create_faiss_index(embeddings: List[List[float]]):
        faiss = dependable_faiss_import()
        dimension = len(embeddings[0])
        index = faiss.IndexFlatL2(dimension)
        index.add(np.array(embeddings, dtype=np.float32))
        return index

    # def add_texts(
    #     self,
    #     texts: Iterable[str],
    #     metadatas: Optional[List[dict]] = None,
    #     ids: Optional[List[str]] = None,
    #     **kwargs: Any
    # ) -> List[str]:
    #     texts = list(texts)
    #     content_embeddings, metadata_embeddings = self._get_embeddings_with_metadata(texts, metadatas, self.embedding_function)
        
    #     # 更新主索引（内容索引）
    #     if self.metadata_index is not None:
    #         self.metadata_index.add(np.array(metadata_embeddings, dtype=np.float32))
    #     else:
    #         self.metadata_index = self._create_faiss_index(metadata_embeddings)
    #     self.index.add(np.array(content_embeddings, dtype=np.float32))
        
    #     # 更新元数据索引
    #     if self.metadata_index is not None:
    #         self.metadata_index.add(np.array(metadata_embeddings, dtype=np.float32))
    #     else:
    #         self.metadata_index = self._create_faiss_index(metadata_embeddings)

    #     return super().add_texts(texts, metadatas=metadatas, ids=ids, **kwargs)

    def similarity_search_with_metadata_scores(
        self,
        query: str,
        k: int = 4,
        filter: Optional[Dict[str, Any]] = None,
        fetch_k: int = 10,
        top_k: int = 3,
        score_threshold = None,
        **kwargs: Any
    ) -> List[Tuple[Document, float]]:
        query_embedding = self.embedding_function.embed_query(query)
        
        # 使用内容索引进行搜索
        # content_scores, content_indices = self.content_index.search(np.array([query_embedding], dtype=np.float32), fetch_k)
        # content_tuples = list(zip(content_scores.flatten(),content_indices.flatten()))
        # sorted_content_tuples = sorted(content_tuples, key=lambda x: x[0])
        
        
        # 使用元数据索引进行搜索
        metadata_scores, metadata_indices = self.metadata_index.search(np.array([query_embedding], dtype=np.float32), fetch_k)
        metadata_tuples = list(zip(metadata_scores.flatten(),metadata_indices.flatten()))
        sorted_metadata_tuples = sorted(metadata_tuples, key=lambda x: x[0])
        
        # temp_index = faiss.IndexFlatL2(len(query_embedding))
        # for meta_index in metadata_indices.flatten():
        #     content_vector = self.content_index.reconstruct(meta_index+1)    score, index = self.content_index.search(np.array([self.content_index.reconstruct(int(metadata_indices.flatten()[0]))]),2)

        metadata_tuples = list(zip(metadata_scores.flatten(),metadata_indices.flatten()))
        metadata_dicts = {t[1]: t[0] for t in metadata_tuples}

        for i in np.arange(3):
            print(self.docstore.search(self.index_to_docstore_id[sorted_metadata_tuples[i][1]]))
            # print(self.docstore.search(self.index_to_docstore_id[sorted_content_tuples[k][1]-1]))
            print("##############%%%%%%%%%%")
            
        faiss = dependable_faiss_import()
        index_content_score=[]
        temp_index = faiss.IndexFlatL2(len(query_embedding))
        for index in metadata_indices.flatten():
            # if index==0:
            #     print(self.docstore.search(self.index_to_docstore_id[index]))
            #     continue
            doc = self.docstore.search(self.index_to_docstore_id[index])
            content_embedding = self.content_index.reconstruct(int(index))

            if temp_index is not None:
                temp_index.add(np.array([content_embedding],dtype=np.float32))
            # content_score = 1/(np.dot(content_embedding,query_embedding)/(np.linalg.norm(content_embedding)*np.linalg.norm(query_embedding))+1)
            # index_content_score.append((index,content_score))
        results = []
        content_scores,indices = temp_index.search(np.array([query_embedding],dtype=np.float32),int(temp_index.ntotal))
        for j,i in enumerate(indices[0]):
            if i==-1:
                continue
            metadata_score = metadata_scores.flatten()[i]
            content_score = content_scores[0][j]

            combined_score = 0.05*content_score+0.95*metadata_score
            results.append((self.docstore.search(self.index_to_docstore_id[metadata_indices.flatten()[i]]),combined_score))
        
        results.sort(key=lambda x: x[1])
        # for result in results:
        #     print(result[0].page_content)
        if score_threshold is not None:
            cmp = (
                operator.ge
                if self.distance_strategy
                in (DistanceStrategy.MAX_INNER_PRODUCT, DistanceStrategy.JACCARD)
                else operator.le
            )
            results = [
                (doc, similarity)
                for doc, similarity in results
                if cmp(similarity, score_threshold)
            ]
        return results[:int(min(k,top_k))]
        # 合并和加权分数
        # combined_scores = {}
        # for i in range(fetch_k):
        #     content_id = content_indices[0][i+1]
        #     metadata_id = metadata_indices[0][i+1]
        #     if content_id != -1:
        #         combined_scores[content_id] = self.content_weight * content_scores[0][i]
        #     if metadata_id != -1:
        #         combined_scores[metadata_id] = combined_scores.get(metadata_id, 0) + self.metadata_weight * metadata_scores[0][i]
        
        # # 排序并选择top k
        # sorted_ids = sorted(combined_scores.keys(), key=lambda x: combined_scores[x])[:k]
        
        # docs_and_scores = []
        # for i in sorted_ids:
        #     _id = self.index_to_docstore_id[i]
        #     doc = self.docstore.search(_id)
        #     if not isinstance(doc, Document):
        #         raise ValueError(f"Could not find document for id {_id}, got {doc}")
        #     docs_and_scores.append((doc, combined_scores[i]))
        
        # return docs_and_scores
        
    def add_embeddings(
        self,
        content_embeddings: List[List[float]],
        metadata_embeddings: List[List[float]],
        texts: List[str],
        metadatas: Optional[List[dict]] = None,
        ids: Optional[List[str]] = None,
        **kwargs: Any
    ) -> List[str]:

        faiss = dependable_faiss_import()
        if not isinstance(self.docstore, AddableMixin):
            raise ValueError(
                "If trying to add texts, the underlying docstore should support "
                f"adding items, which {self.docstore} does not"
            )

        _len_check_if_sized(texts, metadatas, "texts", "metadatas")
        _metadatas = metadatas or ({} for _ in texts)
        documents = [
            Document(page_content=t, metadata=m) for t, m in zip(texts, _metadatas)
        ]

        _len_check_if_sized(documents, content_embeddings, "documents", "content_embeddings")
        _len_check_if_sized(documents, metadata_embeddings, "documents", "metadata_embeddings")
        _len_check_if_sized(documents, ids, "documents", "ids")



        if ids and len(ids) != len(set(ids)):
            raise ValueError("Duplicate ids found in the ids list.")

        # Add to the content index
        content_vector = np.array(content_embeddings, dtype=np.float32)
        if self._normalize_L2:
            faiss.normalize_L2(content_vector)
        # if self.content_index is None:
        #     self.content_index = self._create_faiss_index(content_vector)
        # else:
        self.content_index.add(content_vector)

        # Add to the metadata index
        metadata_vector = np.array(metadata_embeddings, dtype=np.float32)
        if self._normalize_L2:
            faiss.normalize_L2(metadata_vector)
        # if self.metadata_index is None:
        #     self.metadata_index = self._create_faiss_index(metadata_vector)
        # else:
        self.metadata_index.add(metadata_vector)

        # Add information to docstore and index
        ids = ids or [str(uuid.uuid4()) for _ in texts]
        self.docstore.add({id_: doc for id_, doc in zip(ids, documents)})
        starting_len = len(self.index_to_docstore_id)
        index_to_id = {starting_len + j: id_ for j, id_ in enumerate(ids)}
        self.index_to_docstore_id.update(index_to_id)

        return ids

    def add_texts(
        self,
        texts: Iterable[str],
        metadatas: Optional[List[dict]] = None,
        ids: Optional[List[str]] = None,
        **kwargs: Any
    ) -> List[str]:
        texts = list(texts)
        metadatas = metadatas or [{} for _ in texts]
        content_embeddings = self.embedding_function.embed_documents(texts)
        metadata_embeddings = self.embedding_function.embed_documents([self._get_metadata_text(m) for m in metadatas])
        
        return self.add_embeddings(content_embeddings, metadata_embeddings, texts, metadatas, ids, **kwargs)

    # 你可能还想重写其他方法，比如 max_marginal_relevance_search, amax_marginal_relevance_search 等
    def save_local(self, folder_path: str, index_name: str = "index") -> None:
        path = Path(folder_path)
        path.mkdir(exist_ok=True, parents=True)
        # save index separately since it is not picklable
        faiss = dependable_faiss_import()
        # 保存两个索引
        faiss.write_index(self.content_index, str(path / f"{index_name}_content.faiss"))
        faiss.write_index(self.metadata_index, str(path / f"{index_name}_metadata.faiss"))

        # 保存 docstore、index_to_docstore_id 和权重
        with open(path / f"{index_name}.pkl", "wb") as f:
            pickle.dump((self.docstore, self.index_to_docstore_id, 
                         self.content_weight, self.metadata_weight), f)

    @classmethod
    def load_local(
        cls,
        folder_path: str,
        embeddings: Embeddings,
        index_name: str = "index",
        *,
        allow_dangerous_deserialization: bool = True,
        **kwargs: Any,
    ) -> "FAISSWithMetadata":
        if not allow_dangerous_deserialization:
            raise ValueError(
                "The de-serialization relies on loading a pickle file. "
                "Set `allow_dangerous_deserialization` to `True` if you trust the source."
            )
        
        path = Path(folder_path)
        # save index separately since it is not picklable
        faiss = dependable_faiss_import()
        # 加载两个索引
        content_index = faiss.read_index(str(path / f"{index_name}_content.faiss"))
        metadata_index = faiss.read_index(str(path / f"{index_name}_metadata.faiss"))

        # 加载 docstore、index_to_docstore_id 和权重
        with open(path / f"{index_name}.pkl", "rb") as f:
            docstore, index_to_docstore_id, content_weight, metadata_weight = pickle.load(f)
        
        instance = cls(embeddings, content_index, docstore, index_to_docstore_id, **kwargs)
        instance.metadata_index = metadata_index
        instance.content_index = content_index
        instance.content_weight = content_weight
        instance.metadata_weight = metadata_weight
        return instance

    def serialize_to_bytes(self) -> bytes:
        """Serialize both indexes, docstore, index_to_docstore_id, and weights to bytes."""
        return pickle.dumps((self.content_index, self.metadata_index, self.docstore, 
                             self.index_to_docstore_id, self.content_weight, self.metadata_weight))

    @classmethod
    def deserialize_from_bytes(
        cls,
        serialized: bytes,
        embeddings: Embeddings,
        **kwargs: Any,
    ) -> "FAISSWithMetadata":
        """Deserialize both indexes, docstore, index_to_docstore_id, and weights from bytes."""
        content_index, metadata_index, docstore, index_to_docstore_id, content_weight, metadata_weight = pickle.loads(serialized)
        instance = cls(embeddings, content_index, docstore, index_to_docstore_id, **kwargs)
        instance.metadata_index = metadata_index
        instance.content_weight = content_weight
        instance.metadata_weight = metadata_weight
        return instance


    def delete(self, ids: Optional[List[str]] = None, **kwargs: Any) -> Optional[bool]:
        """Delete by ID. These are the IDs in the vectorstore.

        Args:
            ids: List of ids to delete.

        Returns:
            Optional[bool]: True if deletion is successful,
            False otherwise, None if not implemented.
        """
        if ids is None:
            raise ValueError("No ids provided to delete.")
        missing_ids = set(ids).difference(self.index_to_docstore_id.values())
        if missing_ids:
            raise ValueError(
                f"Some specified ids do not exist in the current store. Ids not found: "
                f"{missing_ids}"
            )

        reversed_index = {id_: idx for idx, id_ in self.index_to_docstore_id.items()}
        index_to_delete = {reversed_index[id_] for id_ in ids}

        self.metadata_index.remove_ids(np.fromiter(index_to_delete, dtype=np.int64))
        self.content_index.remove_ids(np.fromiter(index_to_delete, dtype=np.int64))

        self.docstore.delete(ids)
        for ind in index_to_delete:
            self.index_to_docstore_id.pop(ind)