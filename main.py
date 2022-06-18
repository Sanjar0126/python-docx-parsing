import utils
import re
import json

SUB_FOLDER = "docs"

def main():
    print("starting")
    
    question = None
    a_ans = None
    b_ans = None
    c_ans = None
    d_ans = None
    correct = None

    result = []
    files = utils.get_file_names(SUB_FOLDER)
    
    
    for file in files:
        doc = utils.open_docx(f"{SUB_FOLDER}/{file}")
        
        order = 1
        test_list = []
        
        for paragraph in doc.paragraphs:
            num_question_reg = re.match(r'^[#][\d]+', paragraph.text)
            question_reg = re.search(r'[A-D]+\)', paragraph.text)
            
            if num_question_reg:
                if question == None:
                    question = paragraph.text
                else:
                    test_obj = write_test(question, a_ans, b_ans, c_ans, d_ans, correct, order)
                    test_list.append(test_obj)
                    order = order + 1
                    question = paragraph.text

            if question_reg is None and num_question_reg is None:
                question = f"{question}\n{paragraph.text}"
            else:
                a_b_match = re.search(r'(?<=A\))(.*?)(?=B\)|$)', paragraph.text)
                b_c_match = re.search(r'(?<=B\))(.*?)(?=C\)|$)', paragraph.text)
                c_d_match = re.search(r'(?<=C\))(.*?)(?=D\)|$)', paragraph.text)
                d_match = re.search(r'(?<=D\))(.*?)$', paragraph.text)
                
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
                
                a_corr = re.search(r'\+[A]', paragraph.text)
                b_corr = re.search(r'\+[B]', paragraph.text)
                c_corr = re.search(r'\+[C]', paragraph.text)
                d_corr = re.search(r'\+[D]', paragraph.text)
                
                if a_corr:
                    correct = 1
                elif b_corr:
                    correct = 2
                elif c_corr:
                    correct = 3
                elif d_corr:
                    correct = 4
        
        result.append({
            "test_list": test_list,
            "name": file,
        })
    
    with open(f'output/tests.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

def write_test(question, a, b, c, d, answer, order):
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
    }

def testing():
    qwerty = "+A) must wash their hands before leaving the toilet "
    question_reg = re.search(r'[A-D]+[)]', qwerty)
    print(question_reg)

if __name__ == "__main__":
    main()
    # testing()