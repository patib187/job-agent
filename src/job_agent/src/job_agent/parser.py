from docx import Document


def parse_resume(path: str):
    if path.endswith(".docx"):
        doc = Document(path)
        return "\n".join([p.text for p in doc.paragraphs])

    with open(path, "r", encoding="utf-8") as f:
        return f.read()
