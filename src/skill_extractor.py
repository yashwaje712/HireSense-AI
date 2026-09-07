SKILLS = [
    "python", "machine learning", "deep learning", "computer vision",
    "nlp", "sql", "pandas", "numpy", "scikit-learn", "tensorflow",
    "pytorch", "streamlit", "react", "git", "github", "generative ai"
]


def extract_skills(text):
    text_lower = text.lower()
    return [skill for skill in SKILLS if skill in text_lower]


def find_missing_skills(resume_text, job_description):
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))
    return sorted(job_skills - resume_skills)
