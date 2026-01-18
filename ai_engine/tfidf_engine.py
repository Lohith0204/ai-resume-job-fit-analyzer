from sklearn.feature_extraction.text import TfidfVectorizer


def vectorize_skills(resume_skills: list, job_skills: list):
    resume_text = " ".join(resume_skills)
    job_text = " ".join(job_skills)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_text])

    return vectors[0], vectors[1]
