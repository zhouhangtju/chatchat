'''
Author       : your name
Date         : 2024-07-27 08:35:16
LastEditors  : your name
LastEditTime : 2024-07-27 10:25:18
FilePath     : /notebooks/test_router.py
Description  : 
Copyright 2024 OBKoro1, All Rights Reserved. 
2024-07-27 08:35:16
'''
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import json

import os
import shutil

from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import CommaSeparatedListOutputParser
from typing import List, Dict
import numpy as np
from server.knowledge_base.kb_service.base import EmbeddingsFunAdapter
from langchain.vectorstores.faiss import FAISS

embeddings = EmbeddingsFunAdapter()
class KnowledgeBaseSelector:
    def __init__(self, kb_list: List[str], llm: ChatOpenAI):
        self.kb_list = kb_list
        self.llm = llm
        self.prompt = PromptTemplate(
            input_variables=["query", "kb_list"],
            template="""Given the following query and list of knowledge bases, select the most relevant knowledge bases for answering the query. Return the names of the selected knowledge bases as a comma-separated list.
Query: {query}
Knowledge Bases: {kb_list}
Relevant Knowledge Bases:"""
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt, output_parser=CommaSeparatedListOutputParser())

    def select_kbs(self, query: str) -> List[str]:
        print("#")
        query = "'Given the following query and list of knowledge bases', 'select the most relevant knowledge bases for answering the query. Return the names of the selected knowledge bases as a comma-separated list.\nQuery: What are some significant technological advancements in the 20th century?"
        return self.chain.run(query=query, kb_list=", ".join(self.kb_list))

    
kb_list = ["history", "technology", "science", "literature"]

# Initialize components
from configs import (LLM_MODELS, LLM_DEVICE, EMBEDDING_DEVICE,
                     MODEL_PATH, MODEL_ROOT_PATH, ONLINE_LLM_MODEL, logger, log_verbose,
                     FSCHAT_MODEL_WORKERS, HTTPX_DEFAULT_TIMEOUT)
from server.utils import get_model_worker_config,fschat_openai_api_address
config = get_model_worker_config("llama3")

llm = ChatOpenAI(model_name="llama3-8b",temperature=0,openai_api_key=config.get("api_key", "EMPTY"),openai_api_base=config.get("api_base_url", fschat_openai_api_address()))
# embeddings = OpenAIEmbeddings()


# Create knowledge bases
kb_texts = {
    "history": ["Historical text 1", "Historical text 2"],
    "technology": ["Tech text 1", "Tech text 2"],
    "science": ["Science text 1", "Science text 2"],
    "literature": ["Literature text 1", "Literature text 2"]
}

kb_dict = {name: FAISS.from_texts(texts, embeddings, metadatas=[{"source": name}]*len(texts)) 
           for name, texts in kb_texts.items()}
# print(kb_dict)
# Initialize KnowledgeBaseSelector and CustomRetriever
kb_selector = KnowledgeBaseSelector(kb_list, llm)
# retriever = CustomRetriever(kb_dict, embeddings)

def process_query(query: str) -> str:
    # Select relevant knowledge bases
    selected_kbs = kb_selector.select_kbs(query)
    print(f"Selected knowledge bases: {selected_kbs}")
    print("end")

#     # Retrieve relevant documents
#     retrieved_docs = retriever.retrieve(query, selected_kbs)
    
#     # Generate answer using retrieved documents
#     context = "\n".join([f"From {doc['kb']}: {doc['content']}" for doc in retrieved_docs])
#     answer_prompt = PromptTemplate(
#         input_variables=["query", "context"],
#         template="Answer the following query based on the provided context:\n\nQuery: {query}\n\nContext: {context}\n\nAnswer:"
#     )
#     answer_chain = LLMChain(llm=llm, prompt=answer_prompt)
#     answer = answer_chain.run(query=query, context=context)

#     return answer

# Example usage
query = "What are some significant technological advancements in the 20th century?"
result = process_query(query)
# print(f"Query: {query}")
# print(f"Answer: {result}")