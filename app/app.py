import sys
from io import BytesIO
from pathlib import Path

import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.job_matcher import calculate_match_score
from src.resume_parser import extract_text_from_pdf
from src.skill_extractor import (
    calculate_skill_coverage,
    extract_job_keywords,
    extract_skills,
    find_matched_skills,
    find_missing_skills,
)

st.set_page_config(page_title="HireSense AI", page_icon="💼", layout="wide")

st.title("💼 HireSense AI")
st.subheader("Intelligent Resume & Job Matching System")
st.caption("Analyze resume–job compatibility with NLP and machine learning.")

with st.sidebar:
    st.header("⚙️ Analysis")
    st.info("Upload a PDF resume and paste a target job description to generate an AI-assisted compatibility report.")
    st.markdown("**Pipeline:** PDF → NLP → Skills → Match → Skill Gap → Recommendations")

resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("📝 Paste Job Description", height=220, placeholder="Paste the target job description here...")


def build_pdf_report(score, coverage, matched, missing, resume_skills, keywords, sections):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 50

    def line(text, gap=18):
        nonlocal y
        if y < 55:
            pdf.showPage()
            y = height - 50
        pdf.drawString(45, y, text[:105])
        y -= gap

    pdf.setTitle("HireSense AI Resume Analysis Report")
    pdf.setFont("Helvetica-Bold", 18)
    line("HireSense AI - Resume Analysis Report", 28)
    pdf.setFont("Helvetica", 11)
    line(f"Resume Match Score: {score}%")
    line(f"Job Skill Coverage: {coverage}%")
    line("")
    line("Matched Skills:")
    for item in matched or ["None detected"]:
        line(f"- {item}", 15)
    line("")
    line("Missing Skills:")
    for item in missing or ["None detected"]:
        line(f"- {item}", 15)
    line("")
    line("Detected Resume Skills:")
    line(", ".join(resume_skills) if resume_skills else "None detected")
    line("")
    line("Top Job Keywords:")
    line(", ".join(keywords) if keywords else "None detected")
    line("")
    line("Resume Sections Detected:")
    line(", ".join(section for section, found in sections.items() if found) or "No common sections detected")
    line("")
    line("Disclaimer: This report is an educational analytical aid and not a hiring decision.")
    pdf.save()
    return buffer.getvalue()


if st.button("🚀 Analyze Resume", type="primary", use_container_width=True):
    if not resume_file or not job_description.strip():
        st.warning("Please upload a PDF resume and enter a job description.")
    else:
        try:
            resume_text = extract_text_from_pdf(resume_file)
            if not resume_text.strip():
                st.error("No readable text was found in this PDF. Try a text-based resume PDF.")
                st.stop()

            score = calculate_match_score(resume_text, job_description)
            resume_skills = extract_skills(resume_text)
            matched_skills = find_matched_skills(resume_text, job_description)
            missing_skills = find_missing_skills(resume_text, job_description)
            coverage = calculate_skill_coverage(resume_text, job_description)
            keywords = extract_job_keywords(job_description)

            section_patterns = {
                "Contact": ["email", "phone", "linkedin"],
                "Summary": ["summary", "objective", "profile"],
                "Education": ["education", "degree", "university", "college"],
                "Experience": ["experience", "work history", "employment"],
                "Projects": ["projects", "project"],
                "Skills": ["skills", "technical skills", "technologies"],
                "Certifications": ["certifications", "certificates"],
            }
            resume_lower = resume_text.lower()
            sections = {name: any(pattern in resume_lower for pattern in patterns) for name, patterns in section_patterns.items()}

            st.success("Analysis completed successfully!")

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("🎯 Match Score", f"{score}%")
            col2.metric("🧩 Skill Coverage", f"{coverage}%")
            col3.metric("✅ Matched Skills", len(matched_skills))
            col4.metric("⚠️ Missing Skills", len(missing_skills))

            if score >= 75:
                st.success("Strong resume-to-job alignment detected.")
            elif score >= 50:
                st.info("Moderate alignment detected. Review the skill gaps below.")
            else:
                st.warning("Low alignment detected. Consider tailoring the resume to the target role.")

            left, right = st.columns(2)
            with left:
                st.markdown("### ✅ Matched Skills")
                if matched_skills:
                    st.write(", ".join(matched_skills))
                else:
                    st.write("No matching skills detected.")

                st.markdown("### 📄 Detected Resume Skills")
                st.write(", ".join(resume_skills) if resume_skills else "No supported skills detected.")

            with right:
                st.markdown("### ⚠️ Missing Skills")
                if missing_skills:
                    st.write(", ".join(missing_skills))
                else:
                    st.write("No major missing skills detected.")

                st.markdown("### 🔑 Top Job Keywords")
                st.write(", ".join(keywords) if keywords else "No keywords detected.")

            st.markdown("### 📋 Resume Section Check")
            section_cols = st.columns(4)
            for index, (section, found) in enumerate(sections.items()):
                section_cols[index % 4].write(f"{'✅' if found else '⚪'} {section}")

            st.markdown("### 💡 Personalized Recommendations")
            recommendations = []
            if missing_skills:
                recommendations.append("Highlight or develop these job-relevant skills: " + ", ".join(missing_skills) + ".")
            if not sections["Projects"]:
                recommendations.append("Add a Projects section with measurable outcomes and technologies used.")
            if not sections["Experience"]:
                recommendations.append("Add relevant internship, experience, or practical training details if applicable.")
            if not sections["Skills"]:
                recommendations.append("Add a clearly labeled technical Skills section for easier ATS scanning.")
            if score < 60:
                recommendations.append("Tailor keywords and project descriptions to the target job without adding skills you do not have.")
            if not recommendations:
                recommendations.append("Your resume structure and detected skills align well with this job description. Keep improving measurable achievements.")
            for recommendation in recommendations:
                st.write("• " + recommendation)

            report = build_pdf_report(score, coverage, matched_skills, missing_skills, resume_skills, keywords, sections)
            st.download_button(
                "📥 Download PDF Report",
                data=report,
                file_name="hiresense_ai_report.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

            with st.expander("🔍 View Extracted Resume Text"):
                st.text(resume_text)

        except Exception as exc:
            st.error(f"Unable to analyze the resume: {exc}")
