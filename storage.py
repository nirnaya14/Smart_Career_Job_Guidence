# Prompt: Create a Python file storage system using JSON files instead of a
# database. Implement functions for user registration with duplicate email
# check, login with password validation, get user, update profile, save
# search history with max 15 entries and get history by email. Store data
# in data/users.json and data/history.json files.

import json, os
from datetime import datetime
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

USERS_FILE   = os.path.join(DATA_DIR, "users.json")
HISTORY_FILE = os.path.join(DATA_DIR, "history.json")
def _read(f):
    if not os.path.exists(f):
        return {}
    try:
        with open(f) as fp:
            return json.load(fp)
    except:
        return {}

def _write(f, d):
    with open(f, "w") as fp: json.dump(d, fp, indent=2)

def register_user(name, email, password, college, degree, year):
    users = _read(USERS_FILE)
    if email in users: return False, "Email already registered!"
    users[email] = {"name": name, "email": email, "password": password,
                    "college": college, "degree": degree, "year": year,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    _write(USERS_FILE, users)
    return True, "Success"

def login_user(email, password):
    users = _read(USERS_FILE)
    if email not in users: return False, None, "Email not found!"
    if users[email]["password"] != password: return False, None, "Wrong password!"
    return True, users[email], "OK"

def get_user(email):
    return _read(USERS_FILE).get(email)

def update_user(email, data):
    users = _read(USERS_FILE)
    if email in users:
        users[email].update(data)
        _write(USERS_FILE, users)

def save_history(email, skills, jobs, gaps):
    history = _read(HISTORY_FILE)
    if email not in history: history[email] = []
    history[email].insert(0, {
        "id": len(history[email]) + 1,
        "skills": skills,
        "top_job": jobs[0]["title"] if jobs else "—",
        "jobs_count": len(jobs),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    history[email] = history[email][:15]
    _write(HISTORY_FILE, history)

def get_history(email):
    return _read(HISTORY_FILE).get(email, [])
