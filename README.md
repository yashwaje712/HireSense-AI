# 💼 HireSense AI

> **Intelligent Resume & Job Matching System** powered by NLP and Machine Learning.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

HireSense AI analyzes a candidate's resume against a target job description and provides a practical compatibility report. It extracts resume text, detects relevant skills, calculates a semantic-style match score using TF-IDF and cosine similarity, identifies missing skills, and generates improvement suggestions.

## ✨ Features

- 📄 **PDF Resume Parsing** — Extract text from uploaded resumes.
- 🎯 **Job Match Score** — Compare resume and job-description content using TF-IDF + cosine similarity.
- 🧠 **Skill Detection** — Identify relevant technical skills from resume text.
- 🔎 **Missing Skills** — Highlight skills present in the job description but not detected in the resume.
- 💡 **Recommendations** — Suggest areas to strengthen based on missing skills.
- 📊 **Interactive UI** — Simple Streamlit dashboard for quick analysis.
- 🛡️ **Error Handling** — Friendly feedback when analysis cannot be completed.

## 🏗️ Architecture

```text
Resume PDF ──► PDF Text Extraction ──► Skill Extraction ──┐
                                                          ├──► Analysis Dashboard
Job Description ───────────────► TF-IDF + Cosine Similarity ┘
                                                          └──► Missing Skills + Recommendations
```

## 📁 Project Structure

```text
HireSense-AI/
├── app/
│   └── app.py
├── src/
│   ├── resume_parser.py
│   ├── job_matcher.py
│   └── skill_extractor.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yashwaje712/HireSense-AI.git
cd HireSense-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app/app.py
```

The application will open in your browser.

## 🧪 How It Works

1. Upload a resume in PDF format.
2. Paste the target job description.
3. Click **Analyze Resume**.
4. Review the match score and detected skills.
5. Check missing skills and improvement recommendations.
6. Inspect the extracted resume text when needed.

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Streamlit | Web application UI |
| PyMuPDF | PDF text extraction |
| Scikit-learn | TF-IDF and cosine similarity |
| Pandas / NumPy | Data processing |
| Plotly | Visualization-ready dependency |
| spaCy | NLP-ready dependency |
| ReportLab | Report-generation-ready dependency |

## 🎓 Project Highlights

This project demonstrates practical skills in:

- Natural Language Processing (NLP)
- Text preprocessing and information extraction
- Machine Learning similarity techniques
- Python application development
- Streamlit dashboard development
- Git and GitHub project management

## ⚠️ Current Scope

The current version uses a curated technical-skill dictionary and TF-IDF cosine similarity. It is designed as an educational and portfolio project, not as a replacement for professional recruitment decisions.

## 🔮 Future Enhancements

- Transformer-based semantic embeddings
- Larger skill taxonomy and job-role classification
- ATS keyword and formatting analysis
- Resume section quality scoring
- Downloadable PDF analysis reports
- Persistent analysis history
- Deployment with Streamlit Community Cloud

## 👨‍💻 Author

**Yash Waje**  
AI & Data Science Student | Python | Machine Learning | Computer Vision | Deep Learning | Generative AI

## 📄 License

This project is licensed under the [MIT License](LICENSE).
