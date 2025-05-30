import PyPDF2
from docx import Document

def extract_pdf_text(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_docx_text(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_txt_text(file):
    return file.read().decode('utf-8')
