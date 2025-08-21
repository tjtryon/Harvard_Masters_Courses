import sqlite3
import time
import os

DB_FILE = 'race.db'

# Create DB schema if it doesn't exist
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS runners (
                    bib INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    team TEXT NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS results (
                    bib INTEGER,
                    finish_time REAL,
                    assigned INTEGER DEFAULT 0,
                    FOREIGN KEY(bib) REFERENCES runners(bib))''')
    conn.commit()
    conn.close()

# Insert runners from a CSV
def load_runners_from_csv(csv_file):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    with open(csv_file, 'r') as f:
        for line in f:
            try:
                bib, name, team = line.strip().split(',')
                c.execute("INSERT OR IGNORE INTO runners (bib, name, team) VALUES (?, ?, ?)", (int(bib), name.strip(), team.strip()))
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
    conn.commit()
    conn.close()

start_time = None
race_active = False
unassigned_times = []

def start_race():
    global start_time, race_active
    start_time = time.perf_counter()
    race_active = True
    print("Race started.")

def stop_race():
    global race_active
    race_active = False
    print("Race stopped. No more finish times will be recorded.")

def record_time(bib=None):
    if not race_active:
        print("Race is not active. Start the race before recording times.")
        return

    elapsed = round(time.perf_counter() - start_time, 3)
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    if bib is not None:
        c.execute("SELECT * FROM results WHERE bib = ?", (bib,))
        if c.fetchone():
            print(f"Runner {bib} already has a time.")
        else:
            c.execute("INSERT INTO results (bib, finish_time, assigned) VALUES (?, ?, 1)", (bib, elapsed))
            print(f"Bib {bib} recorded at {elapsed:.3f} sec")
    else:
        c.execute("INSERT INTO results (bib, finish_time, assigned) VALUES (?, ?, 0)", (None, elapsed))
        unassigned_times.append(elapsed)
        print(f"Unassigned time recorded: {elapsed:.3f} sec")
    conn.commit()
    conn.close()

def assign_bib_to_unassigned(bib):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT rowid, finish_time FROM results WHERE assigned = 0 ORDER BY rowid LIMIT 1")
    row = c.fetchone()
    if row:
        rowid, time_val = row
        c.execute("UPDATE results SET bib = ?, assigned = 1 WHERE rowid = ?", (bib, rowid))
        print(f"Assigned bib {bib} to unassigned time {time_val:.3f} sec")
    else:
        print("No unassigned times to assign.")
    conn.commit()
    conn.close()

def show_individual_results():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''SELECT r.bib, name, team, finish_time FROM results AS res
                 JOIN runners r ON res.bib = r.bib
                 WHERE assigned = 1
                 ORDER BY finish_time ASC''')
    rows = c.fetchall()
    print("\n--- Individual Results ---")
    for bib, name, team, finish_time in rows:
        print(f"{bib}: {name} ({team}) - {finish_time:.3f} s")
    conn.close()

def show_team_results():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''SELECT team, finish_time FROM results AS res
                 JOIN runners r ON res.bib = r.bib
                 WHERE assigned = 1''')
    team_times = {}
    for team, time_val in c.fetchall():
        team_times.setdefault(team, []).append(time_val)

    print("\n--- Team Results ---")
    for team, times in team_times.items():
        times.sort()
        top5 = times[:5]
        displacers = times[5:7]
        if len(top5) == 5:
            score = sum(top5)
            print(f"{team}: {score:.3f} s (Top 5)")
            if displacers:
                print("  Displacers: " + ", ".join(f"{t:.3f}" for t in displacers))
        else:
            print(f"{team}: Incomplete team")
    conn.close()

def export_html(filename):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''SELECT r.bib, name, team, finish_time FROM results AS res
                 JOIN runners r ON res.bib = r.bib
                 WHERE assigned = 1
                 ORDER BY finish_time ASC''')
    rows = c.fetchall()

    with open(filename, 'w') as f:
        f.write("""<!DOCTYPE html><html lang='en'><head>
<title>Race Results</title>
<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet'>
</head><body class='bg-light'>
<div class='container my-5'>
<h1 class='text-center mb-4'>Race Results</h1>
<table class='table table-striped table-bordered'>
<thead><tr><th>Bib</th><th>Name</th><th>Team</th><th>Finish Time (s)</th></tr></thead><tbody>
""")
        for bib, name, team, time_val in rows:
            f.write(f"<tr><td>{bib}</td><td>{name}</td><td>{team}</td><td>{time_val:.3f}</td></tr>\n")
        f.write("""</tbody></table></div></body></html>""")
    conn.close()
    print(f"HTML results exported to {filename}")

def main_menu():
    print("\n--- Race Timing Console Menu ---")
    print("Commands:")
    print("  start  - start the race")
    print("  stop   - stop the race (no more times recorded)")
    print("  indiv  - show individual results")
    print("  team   - show team results")
    print("  export - export results to HTML")
    print("  quit   - exit program")
    print("\nInput:")
    print("  Spacebar = record time without bib")
    print("  3-digit BIB + space = record bib + time")
    print("  Type bib only = assign bib to earliest unassigned time")

    while True:
        user_input = input("> ")

        cmd = user_input.strip().lower()

        if cmd == "start":
            start_race()

        elif cmd == "stop":
            stop_race()

        elif cmd == "indiv":
            show_individual_results()

        elif cmd == "team":
            show_team_results()

        elif cmd == "export":
            export_html("results.html")

        elif cmd == "quit":
            print("Exiting program.")
            break

        elif user_input.strip() == "":
            record_time()  # unassigned time

        elif user_input.strip().isdigit() and len(user_input.strip()) == 3:
            record_time(int(user_input.strip()))

        elif user_input.strip().isdigit():
            assign_bib_to_unassigned(int(user_input.strip()))

        else:
            print("Unrecognized input")

if __name__ == '__main__':
    init_db()
    if not os.path.exists('runners.csv'):
        print("Missing runners.csv! Please create it with: bib,name,team")
    else:
        load_runners_from_csv('runners.csv')
        main_menu()
