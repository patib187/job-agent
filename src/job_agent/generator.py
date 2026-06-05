import os
from datetime import datetime


def generate_outputs(company, title, resume):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = f"output/{company}_{title}_{ts}".replace(" ", "_")

    os.makedirs(folder, exist_ok=True)

    with open(f"{folder}/tailored_resume.md", "w") as f:
        f.write(resume)

    with open(f"{folder}/cover_letter.md", "w") as f:
        f.write(f"Cover letter for {company}")

    return folder
