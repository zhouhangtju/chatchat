'''
Author       : your name
Date         : 2024-06-21 08:33:45
LastEditors  : your name
LastEditTime : 2024-07-02 02:57:53
FilePath     : /tests/zhouh/create_kb_api.py
Description  : 
Copyright 2024 OBKoro1, All Rights Reserved. 
2024-06-21 08:33:45
'''

import requests
import json
import sys
from pathlib import Path

root_path = Path(__file__).parent.parent.parent
sys.path.append(str(root_path))
from server.utils import api_address
from configs import VECTOR_SEARCH_TOP_K
from server.knowledge_base.utils import get_kb_path, get_file_path
from webui_pages.utils import ApiRequest

from pprint import pprint


api_base_url = api_address()
api: ApiRequest = ApiRequest(api_base_url)
kb = "cloudResourcesPdf"
# kb = "samples"
def test_create_kb(kb="cloudResources"):

    print(f"\n创建新知识库： {kb}")
    data = api.create_knowledge_base(kb)
    pprint(data)
    assert data["code"] == 200
    assert data["msg"] == f"已新增知识库 {kb}"
# test_create_kb()

def test_list_kbs(api="/knowledge_base/list_knowledge_bases"):
    url = api_base_url + api
    print("\n获取知识库列表：")
    r = requests.get(url)
    data = r.json()
    pprint(data)
    assert data["code"] == 200
    assert isinstance(data["data"], list) and len(data["data"]) > 0
    assert kb in data["data"]
test_list_kbs()

def test_list_files(api="/knowledge_base/list_files"):
    url = api_base_url + api
    print("\n获取知识库中文件列表：")
    r = requests.get(url, params={"knowledge_base_name": kb})
    data = r.json()
    pprint(data)
    assert data["code"] == 200
    assert isinstance(data["data"], list)
    # for name in test_files:
    #     assert name in data["data"]
test_list_files()

def test_delete_kb_after(api="/knowledge_base/delete_knowledge_base"):
    url = api_base_url + api
    print("\n删除知识库")
    r = requests.post(url, json=kb)
    data = r.json()
    pprint(data)

    # check kb not exists anymore
    url = api_base_url + "/knowledge_base/list_knowledge_bases"
    print("\n获取知识库列表：")
    r = requests.get(url)
    data = r.json()
    pprint(data)
    assert data["code"] == 200
    assert isinstance(data["data"], list) and len(data["data"]) > 0
    assert kb not in data["data"]

# test_delete_kb_after()



def test_upload_docs(api="/knowledge_base/upload_docs"):
    url = api_base_url + api
    files = [("files", (name, open(path, "rb"))) for name, path in test_files.items()]

    print(f"\n上传知识文件")
    data = {"knowledge_base_name": kb, "override": True}
    r = requests.post(url, data=data, files=files)
    data = r.json()
    pprint(data)
    assert data["code"] == 200
    assert len(data["data"]["failed_files"]) == 0

    print(f"\n尝试重新上传知识文件， 不覆盖")
    data = {"knowledge_base_name": kb, "override": False}
    files = [("files", (name, open(path, "rb"))) for name, path in test_files.items()]
    r = requests.post(url, data=data, files=files)
    data = r.json()
    pprint(data)
    assert data["code"] == 200
    assert len(data["data"]["failed_files"]) == len(test_files)

    print(f"\n尝试重新上传知识文件， 覆盖，自定义docs")
    docs = {"FAQ.MD": [{"page_content": "custom docs", "metadata": {}}]}
    data = {"knowledge_base_name": kb, "override": True, "docs": json.dumps(docs)}
    files = [("files", (name, open(path, "rb"))) for name, path in test_files.items()]
    r = requests.post(url, data=data, files=files)
    data = r.json()
    pprint(data)
    assert data["code"] == 200
    assert len(data["data"]["failed_files"]) == 0


# from server.knowledge_base.utils import get_kb_path, get_file_path
# test_files = {
#     "acl&qos": get_file_path(kb, "acl&qos.md"),
# }
# print(test_files["acl&qos"])