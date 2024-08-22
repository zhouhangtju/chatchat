'''
Author       : your name
Date         : 2024-07-31 10:10:27
LastEditors  : your name
LastEditTime : 2024-07-31 10:10:27
FilePath     : /test_doc_split.py
Description  : 
Copyright 2024 OBKoro1, All Rights Reserved. 
2024-07-31 10:10:27
'''
import docx
from collections import defaultdict
from docx.document import Document
from docx.table import Table
from docx.oxml.shape import CT_Picture
from docx.oxml.shared import qn
import base64
import io

def extract_docx_content(file_path):
    doc = docx.Document(file_path)
    content = defaultdict(list)
    current_heading = "No Heading"
    
    for element in doc.element.body:
        if element.tag.endswith('p'):
            paragraph = doc.paragraphs[doc.element.body.index(element)]
            if paragraph.style.name.startswith('Heading'):
                current_heading = paragraph.text
            else:
                content[current_heading].append({"type": "text", "content": paragraph.text})
        elif element.tag.endswith('tbl'):
            table = Table(element, doc)
            table_data = []
            for row in table.rows:
                table_data.append([cell.text for cell in row.cells])
            content[current_heading].append({"type": "table", "content": table_data})
        elif element.tag.endswith('r'):
            for run in element.findall(".//"+qn('w:drawing')):
                blip = run.find(".//"+qn('a:blip'))
                if blip is not None:
                    image_rid = blip.get(qn('r:embed'))
                    image_part = doc.part.related_parts[image_rid]
                    image_bytes = image_part.blob
                    image_base64 = base64.b64encode(image_bytes).decode()
                    content[current_heading].append({"type": "image", "content": image_base64})
    
    return content

def format_output(content):
    output = []
    for heading, elements in content.items():
        block = {
            "metadata": {"title": heading},
            "content": []
        }
        for element in elements:
            if element['type'] == 'text':
                block['content'].append(f"Text: {element['content']}")
            elif element['type'] == 'table':
                table_str = "Table:\n" + "\n".join([", ".join(row) for row in element['content']])
                block['content'].append(table_str)
            elif element['type'] == 'image':
                block['content'].append(f"Image: [Base64 encoded image data]")
        block['content'] = "\n".join(block['content'])
        output.append(block)
    return output

def main(file_path):
    extracted_content = extract_docx_content(file_path)
    formatted_output = format_output(extracted_content)
    
    # Print the output (you can modify this to save to a file if needed)
    for block in formatted_output:
        print(f"Title: {block['metadata']['title']}")
        print(f"Content:\n{block['content']}\n")
        print("#"*100)

if __name__ == "__main__":
    file_path = "/root/llm/Langchain-Chatchat-master/notebooks/docx-test/docx_test.docx"  # Replace with your actual file path
    main(file_path)