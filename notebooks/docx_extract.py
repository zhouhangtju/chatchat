# from docsplitter.getTOC import get_toc_docx, get_toc_hierarchy
from utils import *
from getPics import *
from getTables import *
import re
import docx
import traceback
from lxml import etree
import zipfile
from docx.oxml.ns import qn



def get_toc_docx(path):
    """
    通过docx文件目录（TOC），从xml中获取每段分段的标题
    :param path: docx文件
    :return: list of TOC in format: [[title_number, title], ...]
        这里title_number示例：1.1、1.1.2、第一章, ...
    """
    if not path.endswith(".docx"):
        print("文件类型必须是docx")
        return False
    toc = []
    # docx解压
    zipf = zipfile.ZipFile(path)
    tree = etree.fromstring(zipf.read("word/document.xml"))
    xml = etree.tounicode(tree)

    # 获取目录内容
    body = next(tree.iterfind(qn("w:body")))
    try:
        sdt = next(body.iterfind(qn("w:sdt")))
        content = next(sdt.iterfind(qn("w:sdtContent")))
    except Exception as e:
        # traceback.print_exc()
        # err_msg = str(e)
        # print(f"识别文档目录失败！请重新检查文档是否有自动目录。Error message: {err_msg}")
        # raise e
        content = body
    # print(content)
    paragraphs = content.findall(qn("w:p"))

    for para in paragraphs:
        hyperlinks = para.findall(qn("w:hyperlink"))
        if hyperlinks:
            relationships = hyperlinks[0].findall(qn("w:r"))
        else:
            relationships = para.findall(qn("w:r"))
        # print(len(relationships))
        text = []
        for r in relationships:
            # text = ""
            t = next(r.iterfind(qn("w:t")), None)

            if t is not None:
                text.append(t.text)

        text_split = None
        if text and text[-1].isdigit():
            # print(text)
            if len(text) >= 2:
                text[1] = " " + text[1]
            text_join = "".join(text[:-1])
            """
            title3 = "2、提供xxx"
            heading_number3 = build_title_regex3(title3)
            tmp = re.findall(heading_number3, title3)[0]
            content = title3.strip(tmp)
            content
            """
            title_regex = build_title_regex3(text_join)
            # print(text_join, title_regex)
            # if not title_regex:
            #     text = [text]
            # else:
            # print(title_regex)
            # text_split = text
            if title_regex:
                title_id = re.findall(title_regex, text_join)
                if title_id:
                    tmp = title_id[0]
                else:
                    continue
                content = text_join.strip(tmp)
                text_split = [tmp.strip(), content.strip()]

                if (
                    toc
                    and text
                    and tmp.count(".")
                    and toc[-1][0].count(".")
                    and (tmp.count(".") - toc[-1][0].count(".") > 1)
                ):
                    toc.append([tmp[:-2], "DummyTitle"])
            # else:
            #     text_split = [text_join.strip()]
        if text_split:
            # print(text_split)
            toc.append(text_split)
    return toc
