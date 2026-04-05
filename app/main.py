from fastapi import FastAPI, UploadFile, File
from app.s3_utils import upload_file_to_s3
from app.file_utils import extract_text, clean_text
from app.rag_pipeline import add_document, search
from app.llm import generate_answer
import io

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI System Running 🚀"}


@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    file_bytes = await file.read()

    file_for_s3 = io.BytesIO(file_bytes)
    file_for_processing = io.BytesIO(file_bytes)

    url = upload_file_to_s3(file_for_s3, file.filename)

    text = extract_text(file_for_processing, file.filename)
    text = clean_text(text)

    add_document(text)

    return {
        "file_url": url,
        "message": "Document processed successfully"
    }


@app.get("/query/")
def query(q: str):
    context = search(q)
    answer = generate_answer(q, context)

    return {"answer": answer}