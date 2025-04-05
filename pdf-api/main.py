from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import fitz

app = FastAPI()

app.add_middleware (
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract-pdf")
async def extract_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    pdf = fitz.open(stream=contents, filetype="pdf")
    text = "\n".join([page.get_text() for page in pdf])
    return {"text": text}