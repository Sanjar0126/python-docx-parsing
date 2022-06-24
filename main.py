from uuid import NAMESPACE_DNS
import utils
import re

SUB_FOLDER = "docs_test"
IMG_FOLDER = "images"

XML_RUN_TEXT_PATH = ".//w:t"

def main():
    print("starting")

    result = []
    files = utils.get_file_names(SUB_FOLDER)
    
    
    for file in files:
        doc = utils.open_docx(f"{SUB_FOLDER}/{file}")
        
        order = 1
        question = ""
        a_ans = None
        b_ans = None
        c_ans = None
        d_ans = None
        correct = None
        question_images = []
        test_list = []
        
        for paragraph in doc.paragraphs:
            num_question_reg = re.match(r'^[#][\d]+', paragraph.text)
            question_reg = re.search(r'[A-D]+\)', paragraph.text)
            
            paragraph_xml = utils.get_paragraph_xml(paragraph._p.xml)
            
            paragraph_text = ""
            
            if num_question_reg and question != "":
                test_obj = write_test(question, a_ans, b_ans, c_ans, d_ans, correct, order, question_images)
                test_list.append(test_obj)
                order = order + 1
                question = ""
                a_ans = None
                b_ans = None
                c_ans = None
                d_ans = None
                correct = None
                question_images = []
            
            for child in paragraph_xml:
                if child.tag == f"{{{utils.XML_NAMESPACES['w']}}}r":
                    xml_text = utils.find_from_xml(XML_RUN_TEXT_PATH, child)
                    paragraph_text = paragraph_text + xml_text.text
                elif child.tag == f"{{{utils.XML_NAMESPACES['m']}}}oMath":
                    svg_file = utils.get_math(child, IMG_FOLDER)
                    question_images.append(svg_file)
                    paragraph_text = paragraph_text + f"\\image{len(question_images)}\\"
            
            for run in paragraph.runs:
                run_xml = run._r.xml
                
                if "a:graphicData" in run_xml:
                    rId = utils.get_rId_xml(run_xml)
                    image_name = utils.save_image(doc, rId, IMG_FOLDER)
                    question_images.append(image_name)
                    paragraph_text = paragraph_text + f"\\image{len(question_images)}\\"
                
                
            if num_question_reg and question == "":
                question = paragraph_text

            if question_reg is None and num_question_reg is None:
                question = f"{question}\n{paragraph_text}"

            if question_reg:
                a_b_match = re.search(r'(?<=A\))(.*?)(?=B\)|$)', paragraph_text)
                b_c_match = re.search(r'(?<=B\))(.*?)(?=C\)|$)', paragraph_text)
                c_d_match = re.search(r'(?<=C\))(.*?)(?=D\)|$)', paragraph_text)
                d_match = re.search(r'(?<=D\))(.*?)$', paragraph_text)
                
                if a_b_match:
                    a_ans = a_b_match.group(0).strip('+')
                    a_ans = a_ans.strip()
                if b_c_match:
                    b_ans = b_c_match.group(0).strip('+')
                    b_ans = b_ans.strip()
                if c_d_match:
                    c_ans = c_d_match.group(0).strip('+')
                    c_ans = c_ans.strip()
                if d_match:
                    d_ans = d_match.group(0).strip('+')
                    d_ans = d_ans.strip()
                
                a_corr = re.search(r'\+[A]', paragraph_text)
                b_corr = re.search(r'\+[B]', paragraph_text)
                c_corr = re.search(r'\+[C]', paragraph_text)
                d_corr = re.search(r'\+[D]', paragraph_text)
                
                if a_corr:
                    correct = 1
                elif b_corr:
                    correct = 2
                elif c_corr:
                    correct = 3
                elif d_corr:
                    correct = 4
        
        test_obj = write_test(question, a_ans, b_ans, c_ans, d_ans, correct, order, question_images)
        test_list.append(test_obj)
        question = ""
        a_ans = None
        b_ans = None
        c_ans = None
        d_ans = None
        correct = None
        question_images = []
        
        result.append({
            "name": file,
            "test_list": test_list,
        })
    
    utils.save_json_file(result, "tests", "output")

def write_test(question, a, b, c, d, answer, order, images=[]):
    question = re.sub(r'^[#][\d]+.', "", question)
    question = question.strip()
    return {
        "question": question,
        "opt1": a,
        "opt2": b,
        "opt3": c,
        "opt4": d,
        "ans": answer,
        "order": order,
        "question_images": images,
    }

def testing():
    qwerty = "+A) must wash their hands before leaving the toilet "
    question_reg = re.search(r'[A-D]+[)]', qwerty)
    print(question_reg)

if __name__ == "__main__":
    main()
    # testing()