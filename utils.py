from docx import Document
from os import listdir

def open_docx(file_name):
    return Document(file_name)

def get_file_names(subfolder):
    return listdir(subfolder)