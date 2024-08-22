'''
Author       : your name
Date         : 2024-07-25 06:29:50
LastEditors  : your name
LastEditTime : 2024-08-07 03:12:07
FilePath     : /tests/zhouh/test_pdf_chat.py
Description  : 
Copyright 2024 OBKoro1, All Rights Reserved. 
2024-07-25 06:29:50
'''
import json

# 从文件中读取 JSON 列表
test_json_path = '/root/llm/Langchain-Chatchat-master/notebooks/test_rag_data/rag_test_md.json'
output_logs = "/root/llm/Langchain-Chatchat-master/tests/zhouh/outputs/pdf-test.txt"
with open(test_json_path, 'r', encoding='utf-8') as file:
    json_list = json.load(file)

# print("从 data.json 文件中读取的 JSON 列表：")
# print(json_list)

import requests
import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from server.utils import api_address

from pprint import pprint


api_base_url = api_address()
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}
def dump_input(d, title):
    # print("\n")
    # print("=" * 30 + title + "  input " + "="*30)
    with open(output_logs,"a",encoding="utf-8") as f:
        f.write(("=" * 30 + title + "  input " + json.dumps(d, ensure_ascii=False, indent=4) +"="*30 + "\n"))

def dump_output(r):
    with open(output_logs,"a",encoding="utf-8") as f:
        f.write(r)

def test_knowledge_chat(api="/chat/knowledge_base_chat",json_list=json_list):
    url = f"{api_base_url}{api}"
    

        # data["query"] = data["query"]+",请生成配置指令代码"
        # data["query"] = json_list[6]["query"]

    # "query": "绿色低碳运营的目标是什么",

    data = {
    "query": "2024年集团目标、省内目标机楼达标率是多少",
    # "query": "基础网络运行情况的事件体系是啥",
    # "knowledge_base_name": "pdf-test",
    "knowledge_base_name": "pre-docx",
    "stream": True}
    data["frequency_penalty"] = 2
    data["temperature"] = 0.01
    print(data)
    response = requests.post(url, headers=headers, json=data, stream=True)
    # print("\n")
    # print("=" * 30 + api + "  output" + "="*30)
    with open(output_logs,"a",encoding="utf-8") as f:
        f.write("=" * 30 + api + "  output" + "="*30 + "\n")
    for line in response.iter_content(None, decode_unicode=True):
        print(line+"###")
        try:
            if line.startswith("data: "):
                data = json.loads(line[6:])
            elif line.startswith(":"):  # skip sse comment line
                continue
            else:
                data = json.loads(line)
            # yield data
        except Exception as e:
            msg = f"接口返回json错误： ‘{line}’。错误信息是：{e}。"
            print(msg)
            # logger.error(f'{e.__class__.__name__}: {msg}',
            #              exc_info=e if log_verbose else None)
        if "answer" in data:
            # print(data["answer"], end="", flush=True)
            with open(output_logs,"a",encoding="utf-8") as f:
                f.write(data["answer"])

    with open(output_logs,"a",encoding="utf-8") as f:
        f.write("\n")
        if line.startswith('data: {"docs"'):
            data = json.loads(line[6:])
            print(data)
            # print(json.dumps(data, ensure_ascii=False))
            f.write(json.dumps(data, ensure_ascii=False)+"\n")
    # pprint(data)
    assert "docs" in data and len(data["docs"]) > 0
    assert response.status_code == 200
test_knowledge_chat(api="/chat/knowledge_base_chat",json_list=json_list)