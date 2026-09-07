from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(resume_text, job_description):
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform([resume_text, job_description])
    score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    return round(score * 100, 2)
