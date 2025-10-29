from fastapi import FastAPI, UploadFile, File
from utils.resume_parser import parse_resume

app = FastAPI(title="Resume Parser Service")

@app.get("/")
def home():
    return {"message": "Resume Parser API is running successfully."}

@app.post("/parse_resume")
async def parse_resume_api(file: UploadFile = File(...)):
    text = await file.read()
    result = parse_resume(text.decode("utf-8", errors="ignore"))
    return {"parsed_data": result}
