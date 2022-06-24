import glob
import json
from docx import Document
from os import listdir
from lxml import etree
import uuid
import ziamath as zm

XML_NAMESPACES = {
            'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
            'wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
            'a':'http://schemas.openxmlformats.org/drawingml/2006/main',
            'pic':'http://schemas.openxmlformats.org/drawingml/2006/picture',
            'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
            'm':"http://schemas.openxmlformats.org/officeDocument/2006/math",
        }

def open_docx(file_name):
    return Document(file_name)

def get_file_names(subfolder):
    return listdir(subfolder)

def save_json_file(object, file_name, path):
    file_count = len(glob.glob1(f"./{path}",f"{file_name}_*"))
    
    file_count = 'temp'
    
    with open(f'{path}/{file_name}_{file_count}.json', 'w', encoding='utf-8') as f:
        json.dump(object, f, ensure_ascii=False, indent=4)
        
def get_rId_xml(xmlstring):
    path = ".//w:drawing/wp:inline/a:graphic/a:graphicData/pic:pic/pic:blipFill/a:blip"
    
    xmlstring = xmlstring.replace("\n", "")
    
    tree = etree.fromstring(xmlstring)
    child = find_from_xml(path, tree)
    
    return child.get(f"{{{XML_NAMESPACES['r']}}}embed")

def save_image(doc, rId, output):
    relation = doc.part.rels[rId]
    
    file_name = f"{str(uuid.uuid4())}.{relation.target_part.image.ext}"
    
    with open(f'{output}/{file_name}', 'wb') as f:
        f.write(relation.target_part.blob)
    
    return file_name

def get_math(xml, output):
    # xmlstring = xmlstring.replace("\n", "")

    xslt_root = etree.parse("OMML2MML.XSL")
    mml_transform = etree.XSLT(xslt_root)
    mml = mml_transform(xml)

    xml_string = etree.tostring(mml).decode("utf-8")
    
    file_name = f"{str(uuid.uuid4())}.svg"

    math = zm.Math(xml_string)
    math.save(f'{output}/{file_name}')

    return file_name

def get_paragraph_xml(xmlstring):
    xmlstring = xmlstring.replace("\n", "")
    tree = etree.fromstring(xmlstring)
    
    return tree

def find_from_xml(path, tree):
    return tree.find(path, XML_NAMESPACES)