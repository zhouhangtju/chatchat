# -*- coding: utf-8 -*-

import re
import base64
import requests


def get_tokens(t):
    return len(t)


def clean_spaces(t: str):
    try:
        t = re.sub(r"\t+|+", " ", t)
        return re.sub(r"\s+", " ", t.strip())
    except Exception:
        print("Error in re.sub")
        print(t)
# if __name__ == "__main__":
#     t = '''编排 技术文件；<API >；手册；FAQ；杭州东方通信软件技术有限公司；#<!image:IM19.jpg>#；声 明；本文件所有权和解释权归东方通信软件技术有限公司所有，未经东方通信软件技；术有限公司书面许可，不得复制或向第三方公开；控制说明：发布版本放入配置库由配置管理员进行维护受控；阅读对象； 本文档的阅读对象包括： CTO、CTO助理； SEPG（软件工程过程小组）成员； 项目经理； 研发经理； 系统架构师； 模块设计师； 软件工程师； 运维工程师。'''
#     print(cleasplit_text_by_sentensen_spaces(t))
    
def split_text_by_sentense(text):
    sentences = re.split(r"([！？。；])", text)
    output = []
    for sent in sentences:
        if sent in "！？；。" and output:
            output[-1] += sent
        else:
            output.append(sent)
    return output


def split_text_into_paragraphs(text, max_words_per_paragraph=300):
    # sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\。|\；|\;)\s', text)
    sentences = split_text_by_sentense(text)
    paragraphs = []

    current_paragraph = []
    word_count = 0

    for sent in sentences:
        if word_count + get_tokens(sent) <= max_words_per_paragraph:
            current_paragraph.append(sent)
            word_count += len(sent)
        else:
            paragraphs.append("".join(current_paragraph))
            current_paragraph = [sent]
            word_count = get_tokens(sent)

    if current_paragraph:
        paragraphs.append("".join(current_paragraph))

    return paragraphs


def replace_synonyms(text: str, synonym_dict: dict):
    if not synonym_dict:
        return text, ""
    get_repl = []
    for word, words_repl in synonym_dict.items():
        pattern = re.compile(rf"(?=\w|\S|^)({re.escape(word)})(?=\S|$)")
        # print(re.findall(pattern, text))
        replacement = f"{word}（{'，'.join(words_repl)}）"
        text = pattern.sub(replacement, text)
        if re.findall(pattern, text):
            get_repl.append(replacement)

    return text, "；".join(get_repl)


def delete_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    # p._p = p._element = None
    paragraph._p = paragraph._element = None


def build_title_regex3(title):
    match = re.match(
        r"([（(第])?([一二三四五六七八九十]+)?([、）)章节条\s]+)+(?=\s|[\u4e00-\u9fa5]{0,1})", title
    )
    if match:
        #         print(match.groups())
        prefix, number, suffix = match.groups()
        if prefix and suffix:
            return f"{re.escape(prefix)}[一二三四五六七八九十]+{re.escape(suffix)}"
        elif not prefix:
            return f"[一二三四五六七八九十]+{re.escape(suffix)}"
        elif not suffix:
            return f"{re.escape(prefix)}[一二三四五六七八九十]+"
        else:
            pass
    match2 = re.match(r"([（(第])?(\d+)?([、）)章节条\s]+)+(?=\s|[\u4e00-\u9fa5]{0,1})", title)
    if match2:
        prefix, number, suffix = match2.groups()
        if prefix and suffix:
            return f"{re.escape(prefix)}[\d+]{re.escape(suffix)}"
        elif not prefix:
            return f"[\d+]{re.escape(suffix)}"
        elif not suffix:
            return f"{re.escape(prefix)}[\d+]"
        else:
            pass
    match3 = re.match(r"([\d+.)]+)+(?=\s|[\u4e00-\u9fa5]{0,1})", title)
    #     match3 = re.match(r'(\d\w\s.)', title)
    if match3:
        number = re.findall(r"\d+", match3[0])
        regex = match3[0]
        for n in number:
            # 构建正则表达式
            regex = regex.replace(n, r"\d+")
        re.escape(regex)
        # regex = f'{re.escape(prefix)}[一二三四五六七八九十]+|[\d.]{re.escape(suffix)}'
        return regex
    #             return match[0]
    else:
        return None


def get_toc_hierarchy(toc, max_lvl=5, with_idx=False, file_title=""):
    prev_regex = {}
    curr_title = [""] * max_lvl
    deepest_lvl = 0

    lines_all = []

    for i in range(len(toc)):
        title = toc[i][0]
        try:
            regex = build_title_regex3(title)
        except TypeError:
            print(title)
            continue
        # print(title, regex)
        if not regex:  # toc 前半部分（编号）识别不出，即目录这一行是纯文本
            if not deepest_lvl:  # 例如：标题、序章
                curr_title[0] = title
            else:  # 目前不在最外层，则作为当前最深层放入，与上一行目录并行
                curr_title[deepest_lvl - 1] = title
                # print(deepest_lvl, title)
        else:
            if regex in prev_regex.keys():
                lvl = prev_regex[regex]
            else:
                lvl = deepest_lvl
                prev_regex[regex] = deepest_lvl
                deepest_lvl += 1
            try:
                if with_idx:
                    curr_title[lvl] = " ".join(toc[i])
                else:
                    curr_title[lvl] = toc[i][-1]
            except IndexError:
                pass
                # print("idx error, ", prev_regex)
            for j in range(lvl + 1, len(curr_title)):
                curr_title[j] = ""
        line = " ".join(curr_title).replace("DummyTitle", "")
        line = file_title + " " + line
        # print(line)
        lines_all.append(line.strip())
    return lines_all


def get_images_ocr(pic_data, format):
    try:
        data = {"file": {"pic_format": format, "data": base64.b64encode(pic_data).decode()}}
        # 重拍识别的示例URL地址
        url = "http://10.8.132.224:7006/ocr"
        response = requests.post(url, json=data)
        # print(response.text)
        # response_t = response.text.encode('utf-8').decode('utf-8')
        if response.json()["code"] == 0:
            return " ".join(response.json()["ocr_result"])
        else:
            raise ValueError("图片转OCR失败")
    except Exception as e:
        raise ValueError("图片转OCR失败，报错信息："+str(e))

if __name__ == "__main__":
    img_save_path = "temp/temp pics\IM87.jpeg"
    format = img_save_path.split(".")[-1]
    pic_data = open(img_save_path, "rb").read()
    print(type(pic_data))

    text = get_images_ocr(pic_data, format)
    print(text)