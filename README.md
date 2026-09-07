<div align="center">

# 💼 HireSense AI

### Intelligent Resume & Job Matching System

**Resume intelligence for better job alignment.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit--learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![PyMuPDF](https://img.shields.io/badge/PyMuPDF-PDF-555555)](https://pymupdf.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-2ea44f.svg)](LICENSE)

**Upload → Analyze → Understand → Improve**

</div>

---

## 📌 About the Project

**HireSense AI** is a Python + Streamlit application that analyzes a resume against a target job description using NLP and machine-learning techniques.

The system extracts text from a PDF resume, compares it with the job description, detects relevant skills, identifies skill gaps, analyzes keywords and resume sections, and produces an actionable report.

### 🎯 Problem

Job descriptions contain many requirements, while resumes often use different wording or omit important skills. Manually checking alignment can be time-consuming.

### 💡 Solution

HireSense AI provides an **explainable resume–job compatibility analysis** so users can quickly understand what aligns and where the resume could be strengthened.

---

## ✨ Features at a Glance

| | Feature | Description |
|---|---|---|
| 📄 | **PDF Resume Parser** | Extract text from uploaded PDF resumes |
| 🎯 | **Match Score** | TF-IDF + cosine similarity between resume and job description |
| 🧠 | **Skill Detection** | Detect supported technical and AI/ML skills |
| ✅ | **Matched Skills** | Find skills appearing in both texts |
| 🔎 | **Skill Gap Analysis** | Identify detected job skills missing from the resume |
| 📈 | **Skill Coverage** | Calculate detected job-skill coverage |
| 🔑 | **Keyword Analysis** | Surface frequently occurring job-description terms |
| 📋 | **Section Analysis** | Check common resume sections |
| 💡 | **Recommendations** | Suggest areas to strengthen |
| 📥 | **PDF Report** | Export the analysis as a report |
| 📊 | **Dashboard** | Interactive Streamlit interface |

---

## 🧠 How It Works

```text
                    ┌─────────────────────┐
                    │    Resume PDF       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  PDF Text Parser    │
                    │     PyMuPDF         │
                    └──────────┬──────────┘
                               │
                               ▼
┌───────────────────┐   ┌─────────────────────┐
│ Job Description   │──►│    NLP Analysis     │
└───────────────────┘   │ • TF-IDF            │
                        │ • Cosine Similarity  │
                        │ • Skill Extraction   │
                        │ • Keyword Analysis   │
                        │ • Section Analysis   │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │  HireSense AI       │
                        │     Dashboard       │
                        ├─────────────────────┤
                        │ Match Score         │
                        │ Skills & Skill Gaps │
                        │ Keywords            │
                        │ Recommendations     │
                        │ PDF Report          │
                        └─────────────────────┘
```

---

## 📊 What You Get

### 🎯 Resume Match Score
A similarity score based on the resume and job-description text.

### 🧠 Skill Intelligence
See detected resume skills, matched skills, missing skills, and overall skill coverage.

### 🔑 Job Keywords
Understand recurring terms in the target job description.

### 📋 Resume Structure Check
Check whether common sections such as **Education, Experience, Projects, Skills, Certifications, and Summary** are present.

### 💡 Actionable Recommendations
Use the detected gaps to decide which relevant skills, projects, coursework, or experience to highlight.

### 📥 Downloadable Report
Export the current analysis for later reference.

> **Important:** The match score is a text-similarity indicator. It is not a prediction of hiring success and should not be treated as an automated hiring decision.

---

## 🖥️ User Workflow

```text
1. Upload Resume PDF
          ↓
2. Paste Job Description
          ↓
3. Click Analyze Resume
          ↓
4. Review Match Score
          ↓
5. Check Skills & Skill Gaps
          ↓
6. Review Keywords & Sections
          ↓
7. Read Recommendations
          ↓
8. Download PDF Report
```

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python |
| **Frontend / UI** | Streamlit |
| **Machine Learning** | Scikit-learn |
| **NLP Method** | TF-IDF + Cosine Similarity |
| **PDF Extraction** | PyMuPDF |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly |
| **NLP Toolkit** | spaCy |
| **Report Generation** | ReportLab |
| **Version Control** | Git + GitHub |

---

## 📁 Project Structure

```text
HireSense-AI/
│
├── app/
│   └── app.py                    # Streamlit application
│
├── src/
│   ├── resume_parser.py          # PDF text extraction
│   ├── job_matcher.py            # Similarity engine
│   └── skill_extractor.py        # Skill & keyword analysis
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

### Prerequisites

- Python 3.x
- pip
- Git

### 1️⃣ Clone

```bash
git clone https://github.com/yashwaje712/HireSense-AI.git
cd HireSense-AI
```

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
```

### 3️⃣ Activate environment

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Launch the app

```bash
streamlit run app/app.py
```

---

## 🧪 Example Use Case

**Input**

- Resume: PDF
- Target role: Machine Learning / AI-related position
- Job description: required skills, responsibilities, and qualifications

**Output**

- Resume match score
- Detected and matched skills
- Missing skills
- Skill coverage
- Important job keywords
- Resume section checks
- Improvement recommendations
- Downloadable PDF report

---

## 🎓 What This Project Demonstrates

- Natural Language Processing
- Text vectorization
- TF-IDF implementation
- Cosine similarity
- Information extraction
- Skill-gap analysis
- Keyword analysis
- Resume structure analysis
- Machine Learning application development
- Python modular architecture
- Streamlit application development
- PDF processing
- Automated report generation
- Git/GitHub workflow

---

## 🔮 Roadmap

- [ ] Transformer-based semantic embeddings
- [ ] Advanced ATS keyword weighting
- [ ] Job-role classification
- [ ] Larger domain-specific skill taxonomy
- [ ] Resume section quality scoring
- [x] Downloadable PDF reports
- [ ] Resume-to-multiple-job comparison
- [ ] Analysis history
- [ ] Interactive visual analytics
- [ ] Streamlit Cloud deployment

---

## 🤝 Contributing

Contributions, bug reports, and feature ideas are welcome.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Open a pull request

For reproducible bugs, use the repository's issue template.

---

## ⚠️ Disclaimer

HireSense AI is an **educational and portfolio project**. The generated analysis is informational and should not be used as the sole basis for employment, recruitment, or hiring decisions.

---

## 👨‍💻 Author

<div align="center">

### Yash Waje

**AI & Data Science Student**

Python • Machine Learning • Computer Vision • Deep Learning • Generative AI

urlGitHub Profilehttps://github.com/yashwaje712

⭐ **If you find this project useful, consider starring the repository!**

</div>

---

<div align="center">

**Build • Evaluate • Improve • Deploy** 🚀

</div>
