<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=170&section=header&text=HireSense%20AI&fontSize=48&fontColor=E6F7FF&fontAlignY=38&desc=RESUME%20%2B%20JOB%20DESCRIPTION%20ANALYSIS&descAlignY=62&descSize=13&color=0:0B1220,55:102A43,100:0891B2" width="100%" alt="HireSense AI — resume and job description analysis" />

**Understand resume-to-role alignment with explainable text analysis.**

![Python](https://img.shields.io/badge/Python-0B1220?style=flat-square&logo=python&logoColor=67E8F9)
![Streamlit](https://img.shields.io/badge/Streamlit-0B1220?style=flat-square&logo=streamlit&logoColor=67E8F9)
![scikit-learn](https://img.shields.io/badge/scikit--learn-0B1220?style=flat-square&logo=scikitlearn&logoColor=67E8F9)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-0B1220?style=flat-square&logo=adobeacrobatreader&logoColor=67E8F9)

[Overview](#overview) · [Features](#features) · [How it works](#how-it-works) · [Run locally](#run-locally)

</div>

---

## Overview

**HireSense AI** is a Python and Streamlit application that compares a PDF resume with a target job description. It extracts resume text, applies TF-IDF and cosine similarity, detects supported skills, highlights potential gaps, and presents suggestions in an interactive dashboard.

The match score is a text-similarity indicator—not a prediction of hiring success or an automated hiring decision.

## Features

- **PDF resume text extraction** with PyMuPDF
- **Resume/job-description similarity** using TF-IDF and cosine similarity
- **Skill detection** and matched-skill summaries
- **Skill-gap analysis** to surface detected job skills not found in the resume
- **Keyword and resume-section checks**
- **Improvement recommendations**
- **Downloadable PDF analysis report**
- **Interactive Streamlit dashboard**

## How it works

```text
Resume PDF ──► Text extraction ──┐
                                 ├──► TF-IDF + cosine similarity
Job description ────────────────┘             │
                                              ├──► Match score
                                              ├──► Skills and gaps
                                              ├──► Keyword / section insights
                                              └──► Recommendations + PDF report
```

## Tech stack

| Area | Tools |
|---|---|
| Language and UI | Python, Streamlit |
| Text similarity | scikit-learn, TF-IDF, cosine similarity |
| PDF extraction | PyMuPDF |
| Data processing | Pandas, NumPy |
| Visualization | Plotly |
| NLP utilities | spaCy |
| PDF reporting | ReportLab |

## Run locally

**Prerequisites:** Python 3.x, Git, and pip.

```bash
git clone https://github.com/yashwaje712/HireSense-AI.git
cd HireSense-AI
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies and launch:

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## Project structure

```text
HireSense-AI/
├── app/
│   └── app.py
├── src/
│   ├── resume_parser.py
│   ├── job_matcher.py
│   └── skill_extractor.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Limitations and responsible use

- The score measures text similarity and should not be interpreted as hiring probability.
- Skill detection depends on the skills and terms supported by the implementation.
- Users should review suggestions and make their own decisions; the tool should not be the sole basis for recruitment decisions.

## Roadmap

- [ ] Semantic embeddings for improved contextual matching
- [ ] Expanded skill taxonomy and role-specific analysis
- [ ] Resume-to-multiple-job comparison
- [ ] Analysis history and richer visual analytics
- [ ] Automated tests and deployment workflow

## Author

**Yash Waje** · [GitHub profile](https://github.com/yashwaje712)

---

<div align="center">

**Analyze · Understand · Improve**

</div>
