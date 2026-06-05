import requests
import re


def fetch_greenhouse(company):
    url = f"https://boards.greenhouse.io/{company}"

    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers, timeout=10)
    if r.status_code != 200:
        return []

    jobs = []

    matches = re.findall(r'href="(/.*?)".*?>(.*?)</a>', r.text)

    for link, title in matches:
        jobs.append({
            "company": company,
            "title": title.strip(),
            "location": "US",
            "job_url": f"https://boards.greenhouse.io{link}"
        })

    return jobs
