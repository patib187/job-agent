from job_agent.portals.greenhouse import fetch_greenhouse
from job_agent.portals.lever import fetch_lever
import re


def matches_exp(job, min_exp, max_exp):
    text = job["title"].lower()
    nums = re.findall(r"\d+", text)

    for n in nums:
        if min_exp <= int(n) <= max_exp:
            return True
    return False


def matches_tech(job, tech_stack):
    text = job["title"].lower()
    return any(t in text for t in tech_stack)


def is_remote(job):
    return "remote" in job["title"].lower()


def is_usa(job):
    return "us" in job.get("location", "").lower()


def fetch_all_jobs(min_exp, max_exp, remote_only, tech_stack, usa_only):

    jobs = []

    for c in ["stripe", "airbnb", "databricks"]:
        jobs += fetch_greenhouse(c)

    for c in ["netflix", "uber"]:
        jobs += fetch_lever(c)

    filtered = []

    for job in jobs:
        if not matches_exp(job, min_exp, max_exp):
            continue

        if remote_only and not is_remote(job):
            continue

        if usa_only and not is_usa(job):
            continue

        if not matches_tech(job, tech_stack):
            continue

        filtered.append(job)

    return filtered[:100]
