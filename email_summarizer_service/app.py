from fastapi import FastAPI, Body
from utils.summarizer import summarize_email

app = FastAPI(title="Email Summarizer Service")

@app.get("/")
def home():
    return {"message": "Email Summarizer API is running "}

@app.post("/summarize")
def summarize_api(email_text: str = Body(..., embed=True)):
    summary = summarize_email(email_text)
    return {"summary": summary}
