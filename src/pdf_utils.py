import PyPDF2

def extract_text_from_pdf(path):
    with open('data/exotic_option.pdf', 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        chunks = []
        i = 0
        for page_number, page in enumerate(reader.pages):
            text = page.extract_text() or ''
            if text == '':
                continue
            chunks.append({
                "id": f"exotic_{i+1}",
                "page": f"{page_number+1}",
                "text": text
            })
            i += 1
        return chunks
    

    