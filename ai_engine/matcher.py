from sklearn.metrics.pairwise import cosine_similarity


def calculate_match(resume_skills, job_skills, resume_vector, job_vector):

    similarity = cosine_similarity(resume_vector, job_vector)[0][0]
    match_score = round(similarity * 100, 2)

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = sorted(resume_set.intersection(job_set))
    missing_skills = sorted(job_set.difference(resume_set))

    explanation = _generate_explanation(match_score, matched_skills, missing_skills)

    return {
        "match_score": match_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "explanation": explanation
    }


def _generate_explanation(score, matched, missing):
    if score >= 80:
        return "Strong match. Candidate meets most of the required skills."
    elif score >= 60:
        return "Moderate match. Candidate has key skills but lacks some requirements."
    else:
        return "Low match. Candidate is missing several important skills."
