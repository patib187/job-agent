import sqlite3

conn = sqlite3.connect("tracker.db")


def init():
    conn.execute("""
    CREATE TABLE IF NOT EXISTS jobs(
        company TEXT,
        title TEXT,
        status TEXT
    )
    """)


def add_record(company, title, status):
    init()
    conn.execute("INSERT INTO jobs VALUES (?, ?, ?)", (company, title, status))
    conn.commit()


def list_records():
    rows = conn.execute("SELECT * FROM jobs").fetchall()
    for r in rows:
        print(r)


def update_record(company, title, status):
    conn.execute("""
    UPDATE jobs
    SET status=?
    WHERE company=? AND title=?
    """, (status, company, title))
    conn.commit()
