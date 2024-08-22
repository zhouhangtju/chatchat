'''
Author       : your name
Date         : 2024-06-24 08:19:18
LastEditors  : your name
LastEditTime : 2024-08-12 08:42:50
FilePath     : /tests/zhouh/test_knowledge_chat.py
Description  : 
Copyright 2024 OBKoro1, All Rights Reserved. 
2024-06-24 08:19:18
'''
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
    print("\n")
    print("=" * 30 + title + "  input " + "="*30)
    pprint(d)


def dump_output(r, title):
    print("\n")
    print("=" * 30 + title + "  output" + "="*30)
    for line in r.iter_content(None, decode_unicode=True):
        print(line, end="", flush=True)

def test_knowledge_chat(api="/chat/knowledge_base_chat"):
    url = f"{api_base_url}{api}"
    data = {
        "query": "RUIJIERG-S6000E系列交换机,如何开启接口索引永久化功能，即设备重启后接口索引不变,给出配置指令",
        "knowledge_base_name": "cloudResources",
        "stream": True
    }
    dump_input(data, api)
    response = requests.post(url, headers=headers, json=data, stream=True)
    print("\n")
    print("=" * 30 + api + "  output" + "="*30)
    for line in response.iter_content(None, decode_unicode=True):
        data = json.loads(line[6:])
        if "answer" in data:
            print(data["answer"], end="", flush=True)
            print("###")
    pprint(data)
    assert "docs" in data and len(data["docs"]) > 0
    assert response.status_code == 200

test_knowledge_chat()