from fastapi import FastAPI
import requests

app = FastAPI(title="Priacc AI Microservices Gateway")

# Base URLs for your microservices
RESUME_PARSER_URL = "http://127.0.0.1:8001"
INVOICE_OCR_URL = "http://127.0.0.1:8002"
EMAIL_SUMMARIZER_URL = "http://127.0.0.1:8003"

@app.get("/")
def home():
    return {"message": "Main API Gateway running successfully."}

@app.post("/resume-parser/")
def parse_resume(file: bytes):
    files = {"file": ("resume.pdf", file)}
    response = requests.post(f"{RESUME_PARSER_URL}/parse_resume", files=files)
    return response.json()

@app.post("/invoice-ocr/")
def extract_invoice(file: bytes):
    files = {"file": ("invoice.png", file)}
    response = requests.post(f"{INVOICE_OCR_URL}/extract_text", files=files)
    return response.json()

@app.post("/email-summary/")
def summarize_email(text: str):
    response = requests.post(f"{EMAIL_SUMMARIZER_URL}/summarize", json={"text": text})
    return response.json()
