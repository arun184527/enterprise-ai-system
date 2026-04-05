from pypdf import PdfReader
import json
import re
def extract_text(file, filename):
    ext = filename.split('.')[-1].lower()

    if ext == "pdf":
        return extract_pdf(file)

    elif ext == "txt":
        return file.read().decode("utf-8")

    elif ext == "json":
        data = json.load(file)
        return json.dumps(data, indent=2)

    else:
        return "Unsupported file type"


def extract_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def clean_text(text):
    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # remove weird line breaks
    text = re.sub(r'\n+', ' ', text)

    # remove repeated characters
    text = text.strip()

    return text