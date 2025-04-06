import pdfplumber
import docx2txt

def extract_text(file):
    if file.name.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            return ''.join([page.extract_text() or '' for page in pdf.pages])
    elif file.name.endswith('.docx'):
        return docx2txt.process(file)
    else:
        return file.read().decode('utf-8')
