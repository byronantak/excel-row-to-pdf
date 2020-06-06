import json
import sys

import xlrd

EMAIL_COLUMN_NAME = "Email address"
STUDENT_NUMBER_COLUMN_NAME = "Student no"

path_to_file = './Q1.xlsx'
workbook = xlrd.open_workbook(path_to_file)
sheet = workbook.sheet_by_index(0)

config_header = {
}

student_details = []


def prompt_if_code_block():
    if column_name != '' and column_name is not None:
        test_input = input(
            f'Would you like the values in "{column_name}" column to be formatted as a code block? (y/N):')
        if test_input.lower() == 'y':
            config_header[column_name] = 'code'
        else:
            config_header[column_name] = 'text'


def validate_required_headers():
    if EMAIL_COLUMN_NAME not in student_data:
        print(f'ERROR: Please ensure that email address column is called "{EMAIL_COLUMN_NAME}"')
        sys.exit(1)
    if STUDENT_NUMBER_COLUMN_NAME not in student_data:
        print(f'ERROR: Please ensure that student number column is called "{STUDENT_NUMBER_COLUMN_NAME}"')
        sys.exit(1)


for row_idx in range(1, sheet.nrows):
    student_data = {}
    for col_idx in range(1, sheet.ncols):
        column_name = str(sheet.cell(0, col_idx).value)
        if row_idx == 1:
            prompt_if_code_block()

        if column_name != '':
            value = str(sheet.cell(row_idx, col_idx).value)
            student_data[column_name] = value

    if row_idx == 1:
        validate_required_headers()

    student_number = student_data[STUDENT_NUMBER_COLUMN_NAME]
    if student_number == '' or student_number is None:
        print(f'Warning: row number {row_idx} - no student number provided')
    else:
        student_data['folder_name'] = student_number
        student_data['file_name'] = f'{student_number}.pdf '
        student_details.append(student_data)

final_json = {
    "config_header": config_header,
    "student_details": student_details
}

with open('student_answers.json', 'w') as file:
    json.dump(final_json, file)
