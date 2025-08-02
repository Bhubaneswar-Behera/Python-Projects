from langchain.schema import Document
import PyPDF2

def load_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        texts = [page.extract_text() for page in reader.pages if page.extract_text()]
    return [Document(page_content=text) for text in texts]
