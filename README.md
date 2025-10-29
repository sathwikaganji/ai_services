# Python AI Microservices — Priacc Hackathon

This project contains 3 FastAPI-based AI microservices:
1. Invoice OCR (pytesseract)
2. Resume Parser (text-based skill extractor)
3. Email Summarizer (transformers model)

##  Run Individually
# Run Invoice OCR
cd invoice_ocr_service
uvicorn app:app --reload --port 8000

# Run Resume Parser
cd resume_parser_service
uvicorn app:app --reload --port 8001

# Run Email Summarizer
cd email_summarizer_service
uvicorn app:app --reload --port 8002

## Run All Together (Docker)
docker-compose up --build

## API URLs
- Invoice OCR: http://localhost:8000/docs
- Resume Parser: http://localhost:8001/docs
- Email Summarizer: http://localhost:8002/docs
