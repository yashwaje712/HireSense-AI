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

HireSense AI is a portfolio-focused NLP and Machine Learning application that compares a candidate's resume with a target job description. It extracts resume text, detects technical skills, calculates a TF-IDF + cosine-similarity match score, identifies missing skills, and generates practical recommendations.

## ✨ What You Can Do

| Feature | Description |
|---|---|
| 📄 Resume Parser | Extract text from PDF resumes |
| 🎯 Match Score | Measure resume/job-description similarity |
| 🧠 Skill Detection | Find relevant technical skills |
| 🔎 Skill Gap | Identify missing job-relevant skills |
| 💡 Recommendations | Suggest areas to strengthen |
| 📊 Dashboard | View results in a clean Streamlit UI |

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
                 │  Skill Extractor │
                 └────────┬─────────┘
                          │
                          ▼
┌─────────────────┐  ┌──────────────────┐
│ Job Description │─►│ TF-IDF + Cosine   │
└─────────────────┘  │ Similarity Engine │
                     └────────┬─────────┘
                              ▼
                 ┌────────────────────────┐
                 │   HireSense Dashboard  │
                 │ Match • Skills • Gaps  │
                 │ Recommendations        │
                 └────────────────────────┘
```

## 📁 Project Structure

```text
HireSense-AI/
│
├── app/
│   └── app.py                 # Streamlit application
│
├── src/
│   ├── resume_parser.py       # PDF text extraction
│   ├── job_matcher.py         # TF-IDF similarity engine
│   └── skill_extractor.py     # Skill detection & gap analysis
│
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
- Machine Learning
- Python application development
- Streamlit UI development
- Git & GitHub workflow

## 🔮 Roadmap

- [ ] Transformer-based semantic embeddings
- [ ] Advanced ATS keyword analysis
- [ ] Job-role classification
- [ ] Larger skill taxonomy
- [ ] Resume section quality scoring
- [ ] Downloadable PDF reports
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
