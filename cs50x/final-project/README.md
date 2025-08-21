# Race Timing System

## Overview

This Race Timing System provides a complete solution for timing, scoring, and managing cross-country or similar races. It supports individual and team results, live timing with milliseconds precision, RFID tag integration, and a web-based interface for management and real-time result viewing. It is available as a GUI solution, or a smaller featured console version.

---

## Features of GUI version

- **Race Timing & Scoring**
  - Record finish times manually by bib number or using spacebar input.
  - Live timing with millisecond precision.
  - Individual and team scoring (top 5 finishers plus 2 displacers).
  - Supports multiple races/heats by race number.
  - Prevents duplicate bibs and RFID tags.

- **RFID Integration**
  - Reads finish times from RFID tag scans.
  - Supports live RFID reading through file watching or TCP scanning.
  - On-site RFID assignment via GUI.
  - Bulk import of RFID mappings from CSV.

- **Data Management**
  - Stores data in SQLite databases named by race date (`YYYYMMDDRace.db`).
  - Supports multiple race days and merges databases if needed.
  - Backup system running every 3 minutes.
  - Load previous race results by date for viewing and printing.

- **Web Interface (Flask)**
  - Upload runner CSV files.
  - Assign RFID tags to runners.
  - View individual and team results by race.
  - Real-time results viewing with place ranking.
  - Editable runner and result tables via web form.
  - Documentation and usage notes pages.
  - Admin panel for centralized management.

- **Export & Reporting**
  - Export results in HTML with Bootstrap CSS styling.
  - Generate charts using Matplotlib for race statistics.


## Features of both versions

- **GUI Application**
  - GTK4-based GUI for race timing and RFID scan handling.
  - Sound alerts on RFID scans.
  - Support for manual and RFID timing modes.
  - File rotation and race number support.
---

## Installation

### Prerequisites

- Python 3.8+
- GTK4 (for GUI)
- Required Python packages:
  - Flask
  - matplotlib
  - sqlite3 (built-in)
  - watchdog (for file watching RFID input)
  - PyGObject (for GTK GUI)

Install dependencies using:

```bash
pip install flask matplotlib watchdog PyGObject


Starting the Flask web server:
from the web/ directory, run:

python app.py

Navigate to http://localhost:5000



Running the GTK GUI
From the gui/ directory, run:
python race-timer-rfid-gui.py



How to Use
Upload runners via the web interface (CSV format with bib, name, team, RFID).

Assign RFID tags manually or in bulk.

Start races and enter finish times manually or via RFID scans.

View individual and team results by race date.

Export results and generate reports via the web interface.

Use the admin panel for system management.

File Naming Conventions
Runner CSV files: runners_YYYYMMDD.csv

SQLite databases: YYYYMMDDRace.db

Backup databases: stored in data/backups/ with timestamps.

RFID input file (for live reading): rfid_input.txt



# Race Timing Console Application

## Overview

This is a Python console-based race timing and scoring system designed for cross country and similar events. It supports:

- **Individual and team results**
- **Live timing with milliseconds (via system clock)**
- **RFID tag reading via file watcher**
- **Manual time entry by bib number**
- **SQLite database storage per race day**
- **Team scoring** using top 5 finishers plus 2 displacers
- **Sound alerts** on runner finish

## Features

- Import runners from CSV files including bib number, name, team, and optional RFID tag.
- Real-time race timing using RFID scans appended to a file.
- Manual entry for finishers by bib number.
- Separate race numbers to handle multiple heats.
- Team scoring calculates points from top 5 runners and includes 2 displacers.
- Results and runner data saved in SQLite database files named `YYYYMMDDRace.db`.
- Sound alerts played on successful finish time entry.
- Menu-driven CLI interface.

## Requirements

- Python 3.7+
- Packages:
  - `playsound`
  - `watchdog`

Install dependencies via pip:

```bash
pip install playsound watchdog

Setup
Place a short sound file named beep.mp3 in the working directory.

Create a data directory or let the program create it.

Prepare runners CSV files with columns: bib, name, team, and optional rfid.

Start the program using:

bash
Copy code
python race_timing_console.py
Usage
Load Runners CSV: Load runners into the database.

Record manual result: Enter a bib number manually to record a finish.

List race results: Show all finishers for the current race.

Show team scores: Display team rankings and scores based on results.

Change race number: Switch the current race/heat number.

Quit: Exit the program safely.

RFID tags are monitored live by watching the data/rfid_input.txt file. Append RFID codes to this file to record automatic finishes.

File Structure
arduino
Copy code
race_timing_console.py
beep.mp3
data/
  ├── rfid_input.txt
  └── YYYYMMDDRace.db
runners.csv
Notes
Ensure rfid_input.txt is updated by your RFID reader software.

Sound alerts notify you of successful finish recording.

Duplicate bib numbers or RFID tags in runners CSV will be skipped with a warning.

Team scores require at least 5 finishers to calculate.

License
This project is released under the MIT License.


Contributing
Contributions, bug reports, and feature requests are welcome! Please fork the repository and submit pull requests.


License
MIT License

For questions or support, please contact TJ Tryon at tj@tjtryon.com



