'''
Author       : your name
Date         : 2024-05-14 08:40:33
LastEditors  : your name
LastEditTime : 2024-08-01 07:27:33
FilePath     : /document_loaders/__init__.py
Description  : 
Copyright 2024 OBKoro1, All Rights Reserved. 
2024-05-14 08:40:33
'''
from .mypdfloader import RapidOCRPDFLoader
from .myimgloader import RapidOCRLoader
from .mydocloader import RapidOCRDocLoader
from .mypptloader import RapidOCRPPTLoader
from .myDocxLoadAndSplitter import *