<div align="center">

# 💼 HireSense AI

### Intelligent Resume & Job Matching System

**AI-powered resume analysis that helps you understand how well your resume aligns with a target role.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![PyMuPDF](https://img.shields.io/badge/PyMuPDF-PDF-555555)](https://pymupdf.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-2ea44f.svg)](LICENSE)

</div>

---

## 🚀 Overview

**HireSense AI** is a portfolio-focused Natural Language Processing (NLP) and Machine Learning application built with Python and Streamlit.

It compares a **resume PDF** with a **target job description**, then turns the text into an easy-to-read compatibility report. The system combines PDF text extraction, TF-IDF vectorization, cosine similarity, skill detection, skill-gap analysis, keyword analysis, resume-section checks, recommendations, and downloadable reporting.

> **Goal:** Make resume–job alignment easier to understand through practical, explainable analysis.

---

## ✨ Key Features

| Feature | What it does |
|---|---|
| 📄 **PDF Resume Parser** | Extracts text from uploaded resumes |
| 🎯 **Resume Match Score** | Measures resume/JD similarity using TF-IDF + cosine similarity |
| 🧠 **Skill Detection** | Detects supported technical and AI/ML skills |
| ✅ **Matched Skills** | Shows skills found in both the resume and job description |
| 🔎 **Skill Gap Analysis** | Identifies detected job skills missing from the resume |
| 📈 **Skill Coverage** | Shows how much of the detected job-skill set is covered |
| 🔑 **Keyword Analysis** | Highlights important repeated terms from the job description |
| 📋 **Resume Section Check** | Checks common sections such as Education, Experience, Projects and Skills |
| 💡 **Recommendations** | Generates practical areas to strengthen |
| 📥 **PDF Report** | Exports the current analysis as a report |
| 📊 **Streamlit Dashboard** | Presents results through a simple interactive interface |

---

## 🖥️ Application Flow

```text
┌─────────────────────┐       ┌──────────────────────┐
│   Resume PDF        │       │   Job Description    │
└──────────┬──────────┘       └──────────┬───────────┘
           │                             │
           ▼                             ▼
┌─────────────────────┐       ┌──────────────────────┐
│  PDF Text Extraction│       │   Text Preprocessing  │
└──────────┬──────────┘       └──────────┬───────────┘
           │                             │
           └──────────────┬──────────────┘
                          ▼
              ┌────────────────────────┐
              │ NLP + ML Analysis       │
              │ • TF-IDF Similarity     │
              │ • Skill Detection       │
              │ • Skill Gap             │
              │ • Keywords              │
              │ • Section Checks        │
              └────────────┬───────────┘
                           ▼
              ┌────────────────────────┐
              │ HireSense AI Dashboard │
              │ Score • Skills • Gaps  │
              │ Keywords • Suggestions │
              │        • PDF Report    │
              └────────────────────────┘
```

---

## 📊 Analysis Output

After analysis, the dashboard provides:

- **Resume Match Score** — similarity between the resume and job description.
- **Skill Coverage** — percentage of detected job skills present in the resume.
- **Matched Skills** — overlapping skills.
- **Missing Skills** — detected job skills not found in the resume.
- **Job Keywords** — frequently occurring job-description terms.
- **Resume Sections** — presence of common resume sections.
- **Recommendations** — practical suggestions based on detected gaps.
- **PDF Report** — downloadable summary of the analysis.

> **Note:** The match score is a text-similarity signal, not a prediction of hiring success.

---

## 🧰 Tech Stack

| Category | Technologies |
|---|---|
| Language | Python |
| UI | Streamlit |
| NLP / ML | Scikit-learn, TF-IDF, Cosine Similarity |
| PDF Processing | PyMuPDF |
| Data | Pandas, NumPy |
| Visualization | Plotly |
| NLP Toolkit | spaCy |
| Reporting | ReportLab |
| Version Control | Git, GitHub |

---

## 📁 Project Structure

```text
HireSense-AI/
│
├── app/
│   └── app.py                    # Streamlit UI & analysis workflow
│
├── src/
│   ├── resume_parser.py          # PDF text extraction
│   ├── job_matcher.py            # TF-IDF similarity engine
│   └── skill_extractor.py        # Skills, gaps & keyword analysis
│
├── .github/
│   └── ISSUE_TEMPLATE/           # Issue templates
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## ⚡ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/yashwaje712/HireSense-AI.git
cd HireSense-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate it

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app/app.py
```

The application will open in your browser.

---

## 🧪 Example Workflow

1. Upload a resume in **PDF** format.
2. Paste the target **job description**.
3. Click **Analyze Resume**.
4. Review the match score and skill coverage.
5. Check matched and missing skills.
6. Review important job keywords and resume sections.
7. Read the recommendations.
8. Download the analysis report.

---

## 🎯 Skills Demonstrated

This project demonstrates practical experience with:

- Natural Language Processing (NLP)
- Text vectorization with TF-IDF
- Cosine similarity
- Information extraction
- Skill and keyword analysis
- Resume structure analysis
- Machine Learning application development
- Python modular programming
- Streamlit dashboard development
- PDF processing and report generation
- Git and GitHub project workflow

---

## 🔮 Roadmap

- [ ] Transformer-based semantic embeddings
- [ ] Advanced ATS keyword weighting
- [ ] Job-role classification
- [ ] Expanded domain-specific skill taxonomy
- [ ] Resume section quality scoring
- [x] Downloadable PDF reports
- [ ] Resume-to-multiple-job comparison
- [ ] Analysis history
- [ ] Interactive charts and visual analytics
- [ ] Streamlit Cloud deployment

---

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the application
5. Open a pull request

For bugs, please use the repository's issue template.

---

## ⚠️ Disclaimer

HireSense AI is an **educational and portfolio project**. Its analysis is intended as an informational aid and should not be used as the sole basis for employment or hiring decisions.

---

## 👨‍💻 Author

<div align="center">

### Yash Waje

**AI & Data Science Student**  
Python • Machine Learning • Computer Vision • Deep Learning • Generative AI

⭐ If you find HireSense AI useful, consider **starring the repository**!

</div>

---

<div align="center">

**Build • Evaluate • Improve • Deploy** 🚀

</div>
