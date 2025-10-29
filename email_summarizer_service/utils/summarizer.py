from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_email(text):
    if len(text.split()) < 30:
        return "Text too short for summarization."
    result = summarizer(text, max_length=80, min_length=30, do_sample=False)
    return result[0]['summary_text']
