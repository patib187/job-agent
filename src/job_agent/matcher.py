def ats_score(jd: str, resume: str):
    jd_words = jd.lower().split()
    res = resume.lower()

    if not jd_words:
        return 0

    matches = sum(1 for w in jd_words if w in res)

    return int((matches / len(jd_words)) * 100)
