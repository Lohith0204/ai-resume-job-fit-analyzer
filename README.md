# AI Resume Intelligence & Job Fit Analysis System

## Live Demo
Try out the deployed application here:

🚀 **Streamlit App** → https://ai-resume-job-fit-analyzer.streamlit.app/

## Overview
AI Resume Intelligence & Job Fit Analysis System is a deployable NLP-based application that helps evaluate how well a candidate’s resume matches a given job description.

The system accepts resumes and job descriptions in multiple document formats (PDF, DOCX, TXT), extracts relevant skills, and computes a job-fit score using TF-IDF vectorization and cosine similarity. It also highlights matched skills and missing skills, providing transparent and actionable insights for both candidates and recruiters.

Unlike traditional resume parsers that only extract static fields, this project focuses on job-aware skill matching, making it useful for real-world recruitment and self-assessment scenarios.

## Features
- Upload Resume and Job Description as separate files
- Supports PDF, DOCX, and TXT formats
- Robust text extraction without OCR dependency
- Skill extraction using a curated technical skill vocabulary
- Job-fit scoring using TF-IDF + cosine similarity
- Clear breakdown of:
    - Match percentage
    - Matched skills
    - Missing skills
- Transparent display of extracted skills for both files
- Single-page, clean Streamlit UI
- Fully deployable on Streamlit Cloud
- No API keys, no external LLM dependencies
## Tech Stack
- Python
- Streamlit (UI & deployment)
- scikit-learn (TF-IDF & cosine similarity)
- pdfplumber (PDF text extraction)
- python-docx (DOCX text extraction)

## Project Structure

```text
AI_RESUME_INTELLIGENCE/
│
├── app.py                   # Streamlit application entry point
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
├── .gitignore
│
├── ai_engine/
│   ├── __init__.py
│   ├── text_extractor.py    # PDF / DOCX / TXT text extraction
│   ├── tfidf_engine.py      # TF-IDF vectorization
│   ├── skill_extractor.py   # Skill extraction logic
│   └── matcher.py           # Match score & skill gap analysis
│
└── screenshots/             # Application screenshots (optional)
```

## Screenshots

### Application Interface
![Application Interface](<screenshots/Screenshot 2026-01-04 160821.png>)

### Images Input
![Images Input](<screenshots/Screenshot 2026-01-04 160948.png>)

### Try-On Image Output
![Tryon Output](<screenshots/Screenshot 2026-01-04 161413.png>)


## How It Works
1. The user uploads a resume and a job description through the Streamlit interface.
2. Text is extracted from each file using format-specific parsers.
3. Relevant technical skills are identified using a predefined skill vocabulary.
4. Extracted skills are converted into TF-IDF vectors.
5. Cosine similarity is used to compute a job-fit score (0–100%).
6. The system identifies:
7. Skills present in both resume and job description
8. Skills missing from the resume
9. Results are displayed with a clear explanation and full transparency.

## Installation & Setup
1. Open your IDE (VS Code is recommended).
2. Clone or download the project files to your local system.
3. Create a virtual environment to avoid dependency conflicts:
   ```bash
   python -m venv venv
   venv\Scripts\activate
4. Install the required dependencies:
    pip install -r requirements.txt
5. Run the application:
    streamlit run app.py

## Usage
This application can be used by:
    - Candidates:
        - To evaluate how well they match a specific job
        - To identify missing skills and improve their profile
    - Recruiters / HR Professionals:
        - To quickly assess resume relevance
        - To shortlist candidates based on skill alignment
Users simply upload a resume and a job description, and the system provides an immediate, explainable job-fit analysis.

## Why This Approach
- No external APIs → stable and deployment-safe
- No black-box models → fully explainable results
- Skill-level matching → more meaningful than raw text similarity
- Deterministic behavior → consistent and reliable outputs
- This design reflects how real-world ATS and recruitment intelligence systems operate.
## Future Improvements
- Expand skill vocabulary dynamically based on job domain
- Add weighting for critical vs optional skills
- Support experience-level scoring based on job requirements
- Add batch resume comparison for recruiter use cases
- UI enhancements and analytics dashboard

## Learning Outcomes
- How to build an end-to-end NLP pipeline for document analysis
- Practical use of TF-IDF and cosine similarity for real-world problems
- Designing explainable AI systems without relying on large language models
- Building and deploying Streamlit applications safely on the cloud
- Making architectural decisions that balance accuracy, usability, and reliability
This project strengthened my understanding of resume intelligence, NLP pipelines, and production-friendly AI system design.
