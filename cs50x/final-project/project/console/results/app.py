from flask import Flask, render_template, g
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
DATA_DIR = "data"

def get_db():
    date_str = datetime.now().strftime("%Y%m%d")
    db_path = os.path.join(DATA_DIR, f"{date_str}Race.db")
    if not hasattr(g, 'db'):
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/individual_results')
def individual_results():
    db = get_db()
    results = db.execute('''
        SELECT r.bib, r.name, r.team, rs.finish_time as time
        FROM results rs
        JOIN runners r ON rs.bib = r.bib
        ORDER BY rs.finish_time ASC
    ''').fetchall()
    return render_template('individual_results.html', results=results)


@app.route('/console_features')
def console_features():
    return render_template('race_timing_console_features.html')





@app.route('/team_results')
def team_results():
    db = get_db()
    runners = db.execute('''
        SELECT r.team, rs.bib, rs.finish_time
        FROM results rs
        JOIN runners r ON rs.bib = r.bib
        ORDER BY rs.finish_time ASC
    ''').fetchall()

    from collections import defaultdict
    teams = defaultdict(list)
    for r in runners:
        teams[r['team']].append(r)

    team_scores = {}
    for team, members in teams.items():
        score = sum((i + 1) for i in range(min(5, len(members))))
        team_scores[team] = score

    team_list = [{'name': team, 'score': score} for team, score in sorted(team_scores.items(), key=lambda x: x[1])]
    return render_template('team_results.html', teams=team_list)

if __name__ == '__main__':
    app.run(debug=True)
