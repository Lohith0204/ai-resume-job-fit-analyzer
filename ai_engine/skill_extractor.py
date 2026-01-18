import re

SKILL_VOCABULARY = [
    # Programming Languages
    "python", "java", "c", "c++", "javascript", "typescript",

    # Data & AI
    "machine learning", "deep learning", "data science",
    "artificial intelligence", "nlp", "computer vision",
    "tensorflow", "pytorch", "scikit-learn",

    # Databases
    "sql", "mysql", "postgresql", "mongodb",

    # Big Data & Engineering
    "spark", "hadoop", "kafka", "airflow",

    # Cloud & DevOps
    "aws", "azure", "gcp", "docker", "kubernetes",
    "ci/cd", "linux",

    # Software Engineering
    "git", "rest api", "microservices", "flask", "django",

    # Analytics & Tools
    "power bi", "tableau", "excel"
]


def extract_skills(text: str) -> list:
    text = text.lower()
    found_skills = set()

    for skill in SKILL_VOCABULARY:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skill)

    return sorted(found_skills)
