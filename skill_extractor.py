SKILLS = [
    "python", "java", "c++", "c#", "machine learning", "deep learning",
    "sql", "mysql", "mongodb", "docker", "kubernetes", "aws", "azure",
    "flask", "django", "react", "node", "git", "linux", "html", "css",
    "javascript", "pandas", "numpy", "scikit-learn", "opencv", "nlp"
]

def extract_skills(text):
    found = set()
    text = text.lower()
    for skill in SKILLS:
        if skill in text:
            found.add(skill)
    return sorted(list(found))
