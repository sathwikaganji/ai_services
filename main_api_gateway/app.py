from fastapi import FastAPI, UploadFile, File, Form
import requests

app = FastAPI(title="Priacc AI Microservices Gateway")

# Microservice endpoints
RESUME_PARSER_URL = "http://127.0.0.1:8001"
INVOICE_OCR_URL = "http://127.0.0.1:8002"
EMAIL_SUMMARIZER_URL = "http://127.0.0.1:8003"

@app.get("/AI")
def home():
    return {"message": "Priacc AI Gateway is running successfully."}

# -------------------- RESUME PARSER --------------------
@app.post("/resume-parser/")
async def parse_resume(file: UploadFile = File(...)):
    try:
        files = {"file": (file.filename, await file.read(), file.content_type)}
        response = requests.post(f"{RESUME_PARSER_URL}/parse_resume", files=files)
        return response.json()
    except Exception as e:
        return {"error": f"Failed to connect to Resume Parser: {e}"}

# -------------------- INVOICE OCR --------------------
@app.post("/invoice-ocr/")
async def extract_invoice(file: UploadFile = File(...)):
    try:
        files = {"file": (file.filename, await file.read(), file.content_type)}
        response = requests.post(f"{INVOICE_OCR_URL}/extract_invoice", files=files)
        return response.json()
    except Exception as e:
        return {"error": f"Failed to connect to Invoice OCR: {e}"}

# -------------------- EMAIL SUMMARIZER --------------------
@app.post("/email-summary/")
def summarize_email(text: str = Form(...)):
    try:
        response = requests.post(
            f"{EMAIL_SUMMARIZER_URL}/summarize", 
            json={"email_text": text}
        )
        return response.json()
    except Exception as e:
        return {"error": f"Failed to connect to Email Summarizer: {e}"}
