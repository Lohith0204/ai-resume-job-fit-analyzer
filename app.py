import streamlit as st
import tempfile
import os

from ai_engine.text_extractor import extract_text
from ai_engine.skill_extractor import extract_skills
from ai_engine.tfidf_engine import vectorize_skills
from ai_engine.matcher import calculate_match


st.set_page_config(
    page_title="AI Resume Intelligence & Job Fit Analysis",
    layout="centered"
)

st.title("📄 AI Resume Intelligence & Job Fit Analysis System")
st.write(
    "Upload a **resume** and a **job description** to evaluate job fit, "
    "identify matched skills, and discover skill gaps."
)

resume_file = st.file_uploader(
    "Upload Resume (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

job_file = st.file_uploader(
    "Upload Job Description (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

if resume_file and job_file:
    if st.button("Analyze Job Fit"):
        with st.spinner("Analyzing resume and job description..."):

            resume_suffix = os.path.splitext(resume_file.name)[1]
            with tempfile.NamedTemporaryFile(delete=False, suffix=resume_suffix) as tmp_resume:
                tmp_resume.write(resume_file.read())
                resume_path = tmp_resume.name

            job_suffix = os.path.splitext(job_file.name)[1]
            with tempfile.NamedTemporaryFile(delete=False, suffix=job_suffix) as tmp_job:
                tmp_job.write(job_file.read())
                job_path = tmp_job.name

            resume_text = extract_text(resume_path)
            job_text = extract_text(job_path)

            resume_skills = extract_skills(resume_text)
            job_skills = extract_skills(job_text)

            resume_vector, job_vector = vectorize_skills(resume_skills, job_skills)

            result = calculate_match(resume_skills,job_skills,resume_vector,job_vector)

            os.remove(resume_path)
            os.remove(job_path)

        st.success("Analysis Complete ✅")

        st.subheader("📊 Job Fit Score")
        st.metric("Match Percentage", f"{result['match_score']} %")

        st.subheader("✅ Matched Skills")
        if result["matched_skills"]:
            st.write(", ".join(result["matched_skills"]))
        else:
            st.write("No matched skills found.")

        st.subheader("❌ Missing Skills")
        if result["missing_skills"]:
            st.write(", ".join(result["missing_skills"]))
        else:
            st.write("No missing skills. Excellent match!")

        st.subheader("📝 Explanation")
        st.write(result["explanation"])

        st.subheader("🔍 Extracted Skills (Transparency)")
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Resume Skills**")
            st.write(resume_skills)

        with col2:
            st.write("**Job Description Skills**")
            st.write(job_skills)
