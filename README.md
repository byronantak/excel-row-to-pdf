# Excel Row to PDF
Python scripts to convert the heading row and cells in each excel rows to a pdf per row. 

# Why?
Students at the university were requested to submit their code and answers to questions on Google forms. Google forms allows you to export 
results into Google sheets. This gets difficult to mark for multiple students because you have make the cells bigger to read longer
answers. Luckily Google sheets allows one to export as an Excel file. These scripts were written so that every cell in every row (representing a student's answers) are concatentated together into pdf documents so that it looks like a single documents with all of a student's answers. 

This was done generically using column names that were not empty because the questions may change in the future,

# Setup
For the setup, see the `setup.md` file.

# How to use
`extract_data.py` reads the excel file and converts it to a more easily used json format file. 

`create_pdf.py` reads the created json file and creates the PDFs 
