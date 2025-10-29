def parse_resume(text):
    keywords = ["Python", "Java", "Machine Learning", "AI", "SQL", "JavaScript", "Flask"]
    skills = [kw for kw in keywords if kw.lower() in text.lower()]
    return {"skills_found": skills, "total_words": len(text.split())}
