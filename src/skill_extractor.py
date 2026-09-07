SKILLS = [
    "python", "machine learning", "deep learning", "computer vision",
    "nlp", "sql", "pandas", "numpy", "scikit-learn", "tensorflow",
    "pytorch", "streamlit", "react", "git", "github", "generative ai",
    "javascript", "html", "css", "opencv", "matplotlib", "seaborn",
    "flask", "fastapi", "docker", "aws", "azure", "mongodb", "mysql",
    "postgresql", "power bi", "tableau", "llm", "langchain", "transformers"
]


def extract_skills(text):
    """Return supported technical skills found in the supplied text."""
    text_lower = text.lower()
    return [skill for skill in SKILLS if skill in text_lower]


def find_missing_skills(resume_text, job_description):
    """Return job-description skills that are not detected in the resume."""
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))
    return sorted(job_skills - resume_skills)


def find_matched_skills(resume_text, job_description):
    """Return skills detected in both the resume and job description."""
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))
    return sorted(resume_skills & job_skills)


def calculate_skill_coverage(resume_text, job_description):
    """Calculate percentage of detected job skills covered by the resume."""
    job_skills = set(extract_skills(job_description))
    if not job_skills:
        return 0.0
    matched = set(find_matched_skills(resume_text, job_description))
    return round((len(matched) / len(job_skills)) * 100, 2)


def extract_job_keywords(job_description, limit=15):
    """Return useful frequent keywords from a job description."""
    import re
    from collections import Counter

    stop_words = {
        "the", "and", "for", "with", "that", "this", "you", "your", "are",
        "our", "from", "will", "have", "has", "not", "but", "all", "job",
        "role", "work", "working", "using", "into", "their", "they", "who",
        "about", "can", "should", "must", "years", "year", "required"
    }
    words = re.findall(r"[a-zA-Z][a-zA-Z+#.-]{2,}", job_description.lower())
    counts = Counter(word for word in words if word not in stop_words)
    return [word for word, _ in counts.most_common(limit)]
