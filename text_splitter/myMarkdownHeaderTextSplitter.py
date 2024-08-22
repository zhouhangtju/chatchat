'''
Author       : your name
Date         : 2024-08-12 07:27:14
LastEditors  : your name
LastEditTime : 2024-08-12 07:49:20
FilePath     : /text_splitter/myMarkdownHeaderTextSplitter.py
Description  : 
Copyright 2024 OBKoro1, All Rights Reserved. 
2024-08-12 07:27:14
'''
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain.text_splitter import LineType
# from langchain_text_splitters import MarkdownHeaderTextSplitter
# from langchain_text_splitters.markdown import LineType
from langchain_core.documents import Document
from typing import Any, Dict, List, Tuple, TypedDict


class MyMarkdownHeaderTextSplitter(MarkdownHeaderTextSplitter):
    def __init__(
        self,
        headers_to_split_on: List[Tuple[str, str]],
        return_each_line: bool = False,
        strip_headers: bool = True,
        ):
        super().__init__(headers_to_split_on=headers_to_split_on,return_each_line=return_each_line,strip_headers=strip_headers)
    def aggregate_lines_to_chunks(self, lines: List[LineType]) -> List[Document]:
        """Combine lines with common metadata into chunks
        Args:
            lines: Line of text / associated header metadata
        """
        aggregated_chunks: List[LineType] = []

        for line in lines:
            if (
                aggregated_chunks
                and aggregated_chunks[-1]["metadata"] == line["metadata"]
            ):
                # If the last line in the aggregated list
                # has the same metadata as the current line,
                # append the current content to the last lines's content
                aggregated_chunks[-1]["content"] += "  \n" + line["content"]
            elif (
                aggregated_chunks
                and aggregated_chunks[-1]["metadata"] != line["metadata"]
                # may be issues if other metadata is present
                and len(aggregated_chunks[-1]["metadata"]) < len(line["metadata"])
                and aggregated_chunks[-1]["content"].split("\n")[-1][0] == "#"
                and not self.strip_headers
            ):
                # If the last line in the aggregated list
                # has different metadata as the current line,
                # and has shallower header level than the current line,
                # and the last line is a header,
                # and we are not stripping headers,
                # append the current content to the last line's content
                aggregated_chunks[-1]["content"] += "  \n" + line["content"]
                # and update the last line's metadata
                aggregated_chunks[-1]["metadata"] = line["metadata"]
            else:
                # Otherwise, append the current line to the aggregated list
                aggregated_chunks.append(line)

        # return [
        #     # Document(page_content=chunk["content"], metadata=chunk["metadata"])
        #     # for chunk in aggregated_chunks
        #     # Document(page_content=(json.dumps(chunk["metadata"])+"\n"+chunk["content"]), metadata=chunk["metadata"])
        #     # for chunk in aggregated_chunks
        # ]
        documents = []
        for chunk in aggregated_chunks:
            metadata = chunk["metadata"]
            max_head_num = 0
            metadata_text = ""
            for key, value in metadata.items():
                if key.startswith("head") and key[4:].isdigit():
                    head_num = int(key[4:])
                    if head_num > max_head_num:
                        max_head_num = head_num
                        metadata_text = value
            if len(metadata_text)>0:  # 仅在找到符合条件的head时添加
                page_content = f'{metadata_text}\n{chunk["content"]}'
                documents.append(Document(page_content=page_content, metadata=chunk["metadata"]))
        return documents