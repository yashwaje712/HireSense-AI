<div align="center">

# 💼 HireSense AI

### Intelligent Resume & Job Matching System

**Turn a resume + job description into an actionable compatibility report.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-2ea44f.svg)](LICENSE)

</div>

---

## 🚀 Overview

HireSense AI is a portfolio-focused NLP and Machine Learning application that compares a candidate's resume with a target job description. It extracts resume text, detects technical skills, calculates a TF-IDF + cosine-similarity match score, measures job-skill coverage, identifies skill gaps, checks common resume sections, extracts important job keywords, and provides actionable recommendations.

## ✨ Features

| Feature | Description |
|---|---|
| 📄 Resume Parser | Extract readable text from PDF resumes |
| 🎯 Match Score | TF-IDF + cosine similarity compatibility score |
| 🧠 Skill Detection | Detect 40+ technical skills and AI technologies |
| ✅ Matched Skills | Show skills present in both resume and job description |
| 🔎 Skill Gap | Identify detected job skills missing from the resume |
| 📈 Skill Coverage | Calculate the percentage of detected job skills covered |
| 🔑 Keyword Analysis | Surface frequent keywords from the target job description |
| 📋 Section Check | Check common sections such as Education, Experience, Projects and Skills |
| 💡 Recommendations | Generate tailored resume improvement suggestions |
| 📥 PDF Report | Download an analysis report for the current resume/job pair |
| 📊 Dashboard | View the complete analysis in a clean Streamlit UI |

## 🧠 How It Works

```text
                 ┌──────────────────┐
                 │   Resume (PDF)   │
                 └────────┬─────────┘
                          ▼
                 ┌──────────────────┐
                 │  PDF Text Parser │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  Skill + Section │
                 │     Analysis     │
                 └────────┬─────────┘
                          │
┌─────────────────┐       ▼
│ Job Description │─►┌──────────────────┐
└─────────────────┘  │ TF-IDF + Cosine   │
                     │ Similarity Engine │
                     └────────┬─────────┘
                              ▼
                 ┌────────────────────────┐
                 │   HireSense Dashboard  │
                 │ Score • Skills • Gaps  │
                 │ Keywords • Sections    │
                 │ Recommendations • PDF  │
                 └────────────────────────┘
```

## 📁 Project Structure

```text
HireSense-AI/
│
├── app/
│   └── app.py                 # Streamlit application & report generator
│
├── src/
│   ├── resume_parser.py       # PDF text extraction
│   ├── job_matcher.py         # TF-IDF similarity engine
│   └── skill_extractor.py     # Skills, coverage & keyword analysis
│
├── .github/
│   └── ISSUE_TEMPLATE/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## ⚡ Quick Start

```bash
git clone https://github.com/yashwaje712/HireSense-AI.git
cd HireSense-AI
python -m venv .venv
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Install & Run

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## 🧰 Tech Stack

**Python · Streamlit · PyMuPDF · Scikit-learn · Pandas · NumPy · Plotly · spaCy · ReportLab · Git/GitHub**

## 🎯 Skills Demonstrated

- Natural Language Processing (NLP)
- TF-IDF & cosine similarity
- Information extraction
- Keyword and skill-gap analysis
- Resume structure analysis
- Machine Learning application development
- Python application development
- Streamlit dashboard development
- PDF report generation
- Git & GitHub workflow

## 🔮 Roadmap

- [ ] Transformer-based semantic embeddings
- [ ] Advanced ATS keyword weighting
- [ ] Job-role classification
- [ ] Larger domain-specific skill taxonomy
- [ ] Resume section quality scoring
- [x] Downloadable PDF reports
- [ ] Analysis history
- [ ] Streamlit Cloud deployment

## ⚠️ Disclaimer

HireSense AI is an educational and portfolio project. Its score is an analytical aid and should not be treated as a professional hiring decision.

## 👨‍💻 Author

**Yash Waje**  
AI & Data Science Student · Python · Machine Learning · Computer Vision · Deep Learning · Generative AI

---

<div align="center">

⭐ **If you find this project useful, consider starring the repository!** ⭐

</div>
