from fastapi import FastAPI, UploadFile, File
from utils.invoice_ocr import extract_text_from_image

app = FastAPI(title="Invoice OCR Service")

@app.get("/")
def home():
    return {"message": "Invoice OCR API is running 🚀"}

@app.post("/extract_invoice")
async def extract_invoice(file: UploadFile = File(...)):
    text = extract_text_from_image(file.file)
    return {"extracted_text": text}
