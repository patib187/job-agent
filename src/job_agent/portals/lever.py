import requests


def fetch_lever(company):
    url = f"https://api.lever.co/v0/postings/{company}"

    r = requests.get(url, timeout=10)
    if r.status_code != 200:
        return []

    data = r.json()
    jobs = []

    for job in data:
        jobs.append({
            "company": company,
            "title": job.get("text", ""),
            "location": job.get("categories", {}).get("location", ""),
            "job_url": job.get("hostedUrl", "")
        })

    return jobs
