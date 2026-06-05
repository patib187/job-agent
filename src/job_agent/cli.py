import typer
import time
from job_agent.parser import parse_resume
from job_agent.matcher import ats_score
from job_agent.generator import generate_outputs
from job_agent.tracker import add_record, list_records, update_record
from job_agent.portals.aggregator import fetch_all_jobs

app = typer.Typer()


def get_preferences():
    exp = typer.prompt("Experience (entry/mid/senior)", default="mid")
    remote = typer.prompt("Remote only? (Y/N)", default="Y")
    tech = typer.prompt("Tech (python,ai,backend,data)", default="python")
    loc = typer.prompt("Location (usa/global)", default="usa")

    exp_map = {
        "entry": (0, 2),
        "mid": (3, 6),
        "senior": (7, 20)
    }

    return {
        "min_exp": exp_map[exp][0],
        "max_exp": exp_map[exp][1],
        "remote_only": remote.lower() == "y",
        "tech_stack": [t.strip().lower() for t in tech.split(",")],
        "usa_only": loc == "usa"
    }


@app.command()
def analyze(profile: str, resume: str, jd: str):
    r = parse_resume(resume)
    j = open(jd).read()

    typer.echo({
        "resume_len": len(r),
        "jd_len": len(j)
    })


@app.command()
def prepare(profile: str, resume: str, company: str, title: str, jd: str):
    r = parse_resume(resume)
    j = open(jd).read()

    score = ats_score(j, r)

    generate_outputs(company, title, r)

    status = "ready_to_apply" if score >= 75 else "review_needed"
    add_record(company, title, status)

    typer.echo(f"✅ Score: {score}")


@app.command()
def track_list():
    list_records()


@app.command()
def track_update(company: str, title: str, status: str):
    update_record(company, title, status)


@app.command()
def auto_run(profile: str, resume: str, once: bool = False):
    prefs = get_preferences()

    while True:
        print("\n🚀 Running cycle...")
        jobs = fetch_all_jobs(**prefs)

        processed, failed = 0, 0

        for job in jobs:
            try:
                r = parse_resume(resume)
                score = ats_score(job["title"], r)

                status = "ready_to_apply" if score >= 75 else "review_needed"
                add_record(job["company"], job["title
