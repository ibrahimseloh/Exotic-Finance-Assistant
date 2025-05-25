import PyPDF2

def extract_text_from_pdf(path):
    with open(path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page in reader.pages : 
            text += page.extract_text()
        return text
    
