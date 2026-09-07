# HireSense AI

**Intelligent Resume & Job Matching System**

HireSense AI is a Streamlit-based application that analyzes a resume against a job description using NLP and machine learning techniques.

## Features

- Resume PDF text extraction
- TF-IDF and cosine-similarity job matching
- Resume match score
- Skill detection
- Missing skill identification
- Actionable recommendations
- Extracted resume text preview

## Tech Stack

Python, Streamlit, PyMuPDF, Pandas, NumPy, Scikit-learn, Plotly, spaCy, ReportLab

## Project Structure

```text
HireSense-AI/
├── app/
│   └── app.py
├── src/
│   ├── resume_parser.py
│   ├── job_matcher.py
│   └── skill_extractor.py
├── requirements.txt
└── README.md
```

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## Author

Yash Waje

AI & Data Science Student | Python | Machine Learning | Computer Vision | Deep Learning | Generative AI
