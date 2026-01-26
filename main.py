import sys
import os
import PyPDF2

from text_utils import clean_text
from skill_extractor import extract_skills
from matcher import match_resume

def read_resume(path):
    if path.endswith(".pdf"):
        text = ""
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()
        return text
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

def read_jobs(folder):
    jobs = []
    names = []
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                jobs.append(f.read())
                names.append(file)
    return jobs, names

def main():
    if len(sys.argv) != 3:
        print("Usage:")
        print("python main.py resume.pdf jobs_folder/")
        return
    resume_path = sys.argv[1]
    jobs_folder = sys.argv[2]
    
    print("Loading resume and job descriptions...")
    resume_text = read_resume(resume_path)
    job_texts, job_names = read_jobs(jobs_folder)
    resume_clean = clean_text(resume_text)
    jobs_clean = [clean_text(j) for j in job_texts]
    resume_skills = extract_skills(resume_clean)
    scores = match_resume(resume_clean, jobs_clean)
    results = list(zip(job_names, scores, jobs_clean))
    results.sort(key=lambda x: x[1], reverse=True)

    print("\nMATCH RESULTS\n")
    for name, score, job_text in results:
        job_skills = extract_skills(job_text)
        missing = set(job_skills) - set(resume_skills)
        print(f"Job: {name}")
        print(f"Match Score: {round(score * 100, 2)}%")
        print(f"Your Skills: {resume_skills}")
        print(f"Job Skills: {job_skills}")
        if missing:
            print(f"Missing Skills: {list(missing)}")
        else:
            print("You match all skills!")
        print("-" * 50)

if __name__ == "__main__":
    main()
