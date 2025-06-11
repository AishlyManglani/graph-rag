import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = " ".join([page.get_text() for page in doc])
    return text.strip() if text else "[No text found in PDF]"