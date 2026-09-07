import streamlit as st
from src.resume_parser import extract_text_from_pdf
from src.job_matcher import calculate_match_score
from src.skill_extractor import extract_skills, find_missing_skills

st.set_page_config(page_title="HireSense AI", page_icon="💼", layout="wide")
st.title("💼 HireSense AI")
st.subheader("Intelligent Resume & Job Matching System")
st.write("Upload your resume and compare it with a job description using NLP and machine learning.")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description", height=220)

if st.button("Analyze Resume", type="primary"):
    if not resume_file or not job_description.strip():
        st.warning("Please upload a PDF resume and enter a job description.")
    else:
        resume_text = extract_text_from_pdf(resume_file)
        score = calculate_match_score(resume_text, job_description)
        resume_skills = extract_skills(resume_text)
        missing_skills = find_missing_skills(resume_text, job_description)

        st.success("Analysis completed!")
        col1, col2 = st.columns(2)
        col1.metric("Resume Match Score", f"{score}%")
        col2.metric("Skills Detected", len(resume_skills))

        st.markdown("### Detected Skills")
        st.write(", ".join(resume_skills) if resume_skills else "No supported skills detected.")

        st.markdown("### Missing Skills")
        st.write(", ".join(missing_skills) if missing_skills else "No major missing skills detected.")

        st.markdown("### Recommendations")
        if missing_skills:
            st.write("Consider adding relevant projects, coursework, or experience for: " + ", ".join(missing_skills) + ".")
        else:
            st.write("Your detected skills align well with the job description.")

        with st.expander("View Extracted Resume Text"):
            st.text(resume_text)
