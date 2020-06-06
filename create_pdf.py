import html
import json
import os
import sys

import pdfkit

FILENAME = 'student_answers.json'
STUDENT_DATA_NAME = "student_details"
CONFIG_HEADER_NAME = "config_header"
CONTAINING_FOLDER_NAME = 'pdfs'
STUDENT_NUMBER_NAME = 'Student no'
CODE_TYPE_CONFIG_OPTION = 'code'

with open('style_doc.css', 'r') as f:
    styles_html = "<style>" + f.read() + "</style>"


def get_formatted_value(key, unescaped_value, column_type):
    value = html.escape(unescaped_value)
    if value == '':
        return f'<h2 class="question">{key}</h2><p class="answer"><b class="blank-student-answer"> -- Left blank -- </b></p><hr>'
    if column_type == CODE_TYPE_CONFIG_OPTION:
        return f'<h2 class="question">{key}</h2><pre class="code-answer">{value}</pre><hr>'
    else:
        value = value.replace('\n', '<br>')
        return f'<h2 class="question">{key}</h2><p class="answer">{value}</p><hr>'


def get_header(student_number):
    return f'<h1 class="header">{student_number} RESPONSE</h1>'


def create_pdf(data_dict, config):
    folder_name = f'{CONTAINING_FOLDER_NAME}/{data_dict["folder_name"]}'
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    pdf_name = data_dict[STUDENT_NUMBER_NAME] + '.pdf'
    file_path = f'{folder_name}/{pdf_name}'
    with open(file_path, 'wb'):
        pass
    html_str = f'<head><meta charset="utf-8">{styles_html}</head><body>'
    html_str += get_header(data_dict[STUDENT_NUMBER_NAME])
    for key in data_dict:
        if key == 'file_name' or key == 'folder_name' or key == '':
            continue
        html_str += get_formatted_value(key, data_dict[key], config[key])
    html_str += '</body>'
    pdfkit.from_string(html_str, file_path)


try:
    json_file = open(FILENAME)
except IOError:
    print("Could not open/read file:", FILENAME)
    sys.exit(1)

with json_file:
    obj = json.load(json_file)
    config_header = obj[CONFIG_HEADER_NAME]
    student_answers = obj[STUDENT_DATA_NAME]
    if not os.path.exists(CONTAINING_FOLDER_NAME):
        os.mkdir(CONTAINING_FOLDER_NAME)

    for data in student_answers:
        print(f'Creating PDF for student {data[STUDENT_NUMBER_NAME]}:')
        create_pdf(data, config_header)
