from fastapi import FastAPI, UploadFile, File
from utils.invoice_ocr import extract_text_from_image
from PIL import UnidentifiedImageError

app = FastAPI(title="Invoice OCR Service")

@app.get("/")
def home():
    return {"message": "Invoice OCR API is running successfully."}

@app.post("/extract_invoice")
async def extract_invoice(file: UploadFile = File(...)):
    try:
        text = extract_text_from_image(file.file)
        return {"extracted_text": text}
    except UnidentifiedImageError:
        return {"error": "Invalid image format. Please upload a valid image (PNG, JPG, JPEG)."}
    except Exception as e:
        return {"error": str(e)}
