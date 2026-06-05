# Job Application Agent

This is a simple Python CLI tool I built to experiment with automating parts of the job application process.

Right now it can:
- Read a resume
- Compare it with a job description
- Give a basic match score
- Store job tracking data locally
- Fetch some job listings from common portals

It’s not perfect and still evolving, but it’s a good starting point.

---

## Project Structure

. ├── pyproject.toml ├── README.md └── src/ └── job_agent/ ├── cli.py ├── parser.py ├── matcher.py ├── generator.py ├── tracker.py └── portals/ ├── aggregator.py ├── greenhouse.py └── lever.py



---

## How to Clone

If you're using Git:

git clone ​https://github.com/YOUR_USERNAME/job-application-agent.git​cd job-application-agent



If you don’t want to use Git:

- Click the green **Code** button
- Select **Download ZIP**
- Extract it
- Open the folder

---

## Setup

Make sure you have Python 3.9+ installed.

Create a virtual environment:

python -m venv venv



Activate it:

### Windows
venv\Scripts\activate



### Mac/Linux
source venv/bin/activate



Install dependencies:

pip install -e .



---

## How to Run

First check if everything is working:

job-agent --help



You should see a list of commands.

---

## Commands

### 1. Analyze Resume vs JD

job-agent analyze profile.yaml resume.docx jd.txt



This just compares resume and job description.

---

### 2. Prepare Application Files

job-agent prepare profile.yaml resume.docx "Company" "Job Title" jd.txt



This will:
- Score your resume
- Generate basic output files
- Save job record

---

### 3. Run Automatic Job Fetch

job-agent auto-run profile.yaml resume.docx --once



This will:
- Fetch jobs
- Filter them
- Store results

Use `--once` so it runs only one cycle.

---

### 4. View Saved Jobs

job-agent track-list



---

### 5. Update Job Status

job-agent track-update "Company" "Job Title" applied



---

## Notes

- This project is experimental
- Job matching logic is very basic
- Not all job portals may return results consistently
- You should manually review everything before applying

---

## Future Improvements

- Better resume parsing
- Real ATS keyword matching
- AI-based resume tailoring
- Better job filtering

---

## Author

Pavan Kumar Patibandla
