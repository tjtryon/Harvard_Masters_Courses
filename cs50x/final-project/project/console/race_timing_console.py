import sqlite3
import os
import time
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from playsound import playsound
from collections import defaultdict

DATA_DIR = "data"
RFID_INPUT_FILE = os.path.join(DATA_DIR, "rfid_input.txt")
SOUND_FILE = "beep.mp3"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Generate DB filename based on date
today_str = datetime.datetime.now().strftime("%Y%m%d")
db_filename = f"{today_str}Race.db"
db_path = os.path.join(DATA_DIR, db_filename)

# Connect to SQLite database
conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS runners (
    bib INTEGER PRIMARY KEY,
    name TEXT,
    team TEXT,
    rfid TEXT UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS results (
    bib INTEGER,
    finish_time TEXT,
    race_number INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

def load_runners_from_csv(csv_path):
    import csv
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                cursor.execute(
                    "INSERT INTO runners (bib, name, team, rfid) VALUES (?, ?, ?, ?)",
                    (int(row['bib']), row['name'], row['team'], row.get('rfid', None))
                )
            except sqlite3.IntegrityError:
                print(f"⚠️ Duplicate bib or RFID detected: {row['bib']}")
    conn.commit()

def record_finish(bib, race_number):
    finish_time = time.strftime("%H:%M:%S", time.localtime())
    cursor.execute("INSERT INTO results (bib, finish_time, race_number) VALUES (?, ?, ?)",
                   (bib, finish_time, race_number))
    conn.commit()
    print(f"✅ Recorded: Bib {bib} at {finish_time} for Race {race_number}")
    try:
        playsound(SOUND_FILE)
    except:
        print("⚠️ Error playing sound.")

class RFIDHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("rfid_input.txt"):
            with open(RFID_INPUT_FILE, 'r') as f:
                lines = f.read().splitlines()
            for rfid in lines[-5:]:  # only last few
                cursor.execute("SELECT bib FROM runners WHERE rfid = ?", (rfid.strip(),))
                row = cursor.fetchone()
                if row:
                    record_finish(row[0], current_race_number)
                else:
                    print(f"⚠️ Unknown RFID scanned: {rfid.strip()}")

def start_rfid_monitor():
    event_handler = RFIDHandler()
    observer = Observer()
    observer.schedule(event_handler, path=DATA_DIR, recursive=False)
    observer.start()
    print("📡 Started RFID monitoring.")
    return observer

def list_results(race_number):
    print(f"\n🏁 Results for Race {race_number}:")
    cursor.execute('''
    SELECT runners.bib, runners.name, runners.team, results.finish_time
    FROM results
    JOIN runners ON runners.bib = results.bib
    WHERE results.race_number = ?
    ORDER BY results.finish_time ASC
    ''', (race_number,))
    for row in cursor.fetchall():
        print(f"BIB {row[0]} | {row[1]} | Team: {row[2]} | Time: {row[3]}")

def calculate_team_scores(race_number):
    print(f"\n📊 Team Scores for Race {race_number}:")
    cursor.execute('''
    SELECT runners.bib, runners.name, runners.team, results.finish_time
    FROM results
    JOIN runners ON runners.bib = results.bib
    WHERE results.race_number = ?
    ORDER BY results.finish_time ASC
    ''', (race_number,))
    results = cursor.fetchall()

    team_positions = defaultdict(list)
    for i, row in enumerate(results):
        bib, name, team, _ = row
        team_positions[team].append(i + 1)

    for team, places in team_positions.items():
        if len(places) >= 5:
            score = sum(places[:5])
            displacers = places[5:7]  # 2 displacers
            print(f"🏆 {team}: Score = {score}, Displacers = {displacers}")
        else:
            print(f"❌ {team}: Not enough runners to score (has {len(places)})")

# Main console loop
current_race_number = 1
observer = start_rfid_monitor()

try:
    while True:
        print("\n📋 Menu:")
        print("1. Load runners CSV")
        print("2. Record manual result")
        print("3. List race results")
        print("4. Show team scores")
        print("5. Change race number")
        print("6. Quit")

        choice = input("👉 Choose an option: ").strip()
        if choice == '1':
            path = input("📁 Enter path to runners.csv: ")
            if os.path.exists(path):
                load_runners_from_csv(path)
            else:
                print("⚠️ File not found.")
        elif choice == '2':
            bib = input("🏃 Enter bib number: ").strip()
            if bib.isdigit():
                record_finish(int(bib), current_race_number)
        elif choice == '3':
            list_results(current_race_number)
        elif choice == '4':
            calculate_team_scores(current_race_number)
        elif choice == '5':
            race_input = input("🔢 Enter new race number: ")
            if race_input.isdigit():
                current_race_number = int(race_input)
                print(f"✅ Switched to race #{current_race_number}")
        elif choice == '6':
            break
        else:
            print("⚠️ Invalid input.")

finally:
    observer.stop()
    observer.join()
    conn.close()
    print("📦 Exiting and closing database.")
