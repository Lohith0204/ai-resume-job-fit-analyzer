import os
import pdfplumber
from docx import Document


def extract_text(file_path: str) -> str:
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".txt":
        return _extract_txt(file_path)

    elif extension == ".pdf":
        return _extract_pdf(file_path)

    elif extension == ".docx":
        return _extract_docx(file_path)

    else:
        raise ValueError("Unsupported file format. Use PDF, DOCX, or TXT.")


def _extract_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def _extract_pdf(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def _extract_docx(file_path: str) -> str:
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])
