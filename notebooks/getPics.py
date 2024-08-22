'''
Author       : your name
Date         : 2024-07-31 03:23:27
LastEditors  : your name
LastEditTime : 2024-07-31 06:12:16
FilePath     : /getPics.py
Description  : 
Copyright 2024 OBKoro1, All Rights Reserved. 
2024-07-31 03:23:27
'''
import docx
from docx.document import Document
from docx.text.paragraph import Paragraph
from docx.oxml.shape import CT_Picture
from docx.parts.image import ImagePart
from docx.image.image import Image
from docx.table import Table

from utils import clean_spaces
from getTables import get_docx_imgs_totext

def get_picture_list(document: Document, paragraphs: [Paragraph]):
    # 获取WORD中的图片列表，有可能一个段落中含有多张图片
    img_list = []
    for paragraph in paragraphs:
        img_list += paragraph._element.xpath(".//pic:pic")
    if len(img_list) == 0 or not img_list:
        return []
    # 将图片列表中的图片读出来另存为文件，并返回文件名列表
    size = len(img_list)
    re_list = []
    for i in range(0, size):
        img: CT_Picture = img_list[i]
        embed = img.xpath(".//a:blip/@r:embed")[0]
        related_part: ImagePart = document.part.related_parts[embed]
        try:
            image: Image = related_part.image
            re_list.append(image)
        except docx.image.exceptions.UnrecognizedImageError:
            pass
    return re_list
	
def tbl2_text_withpics(doc: Document, table: Table, pics_folder="./pics_tmp",
                       **kwargs) -> [str]:
    """从表格内提取文字内容 转化为纯文本；将图片保存在`pics_folder`中 并在文本中添加图片标识"""
    data = []
    i_start = 0
    headers = None
    if len(table.rows) > 1 and table.cell(0, 0).text.strip():
        headers = [cell.text for cell in table.row_cells(0)]
        # headers = list(table.row_cells(0))
        i_start = 1
    tbl_pic_count = 0
    for i in range(i_start, len(table.rows)):
        row_data = []
        col_n = len(table.row_cells(i))

        for j in range(col_n):
            cell_text = table.cell(i, j).text
            pics = get_picture_list(doc, table.cell(i, j).paragraphs)
            for pic in pics:
                image_saved_name = get_docx_imgs_totext(pic, tbl_pic_count, pics_folder,**kwargs)
                if image_saved_name:
                    # cell_text += image_saved_label
                    cell_text += image_saved_name
                    tbl_pic_count += 1
            cell_wcol = (
                f"{headers[j].strip()}：{cell_text.strip()}"
                if headers and cell_text.strip()
                else cell_text.strip()
            )
            # print(cell_text)
            # cell_wcol = cell_text
            cell_wcol = cell_wcol.replace("\n", " ")
            if not cell_wcol or (row_data and row_data[-1] == cell_wcol):
                pass
            else:
                if not cell_wcol.strip().endswith((",",".","?","!","。","，","！","？","；")):
                    cell_wcol += "，"
                cell_wcol = clean_spaces(cell_wcol)
                row_data.append(cell_wcol)
            # print(row_data)
        if row_data:
            data.append("".join(row_data))
    if not data and headers:
        return headers, tbl_pic_count
    return data, tbl_pic_count

