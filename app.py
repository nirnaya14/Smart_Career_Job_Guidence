# Create a Flask application called CareerAI with routes for home,
# register, login, logout, dashboard, find jobs with POST for skill matching,
# browse all jobs with category filter, job detail page, history and profile
# update page. Use session for login management and login_required decorator

from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
from storage import register_user, login_user, get_user, update_user, save_history, get_history
from jobs_db import match_jobs, get_skill_gaps, get_all_categories, JOBS_DATABASE

app = Flask(__name__)
app.secret_key = "career-ai-2024-secret"

def login_required(f):
    @wraps(f)
    def dec(*a, **kw):
        if "email" not in session:
            flash("Please login first.", "warning")
            return redirect(url_for("login"))
        return f(*a, **kw)
    return dec

@app.route("/")
def home():
    return render_template("home.html", total_jobs=len(JOBS_DATABASE),
                           categories=get_all_categories())

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name     = request.form["name"].strip()
        email    = request.form["email"].strip().lower()
        password = request.form["password"]
        confirm  = request.form["confirm_password"]
        college  = request.form.get("college","").strip()
        degree   = request.form.get("degree","B.Tech")
        year     = request.form.get("year","3rd Year")
        if not all([name, email, password]):
            flash("All fields are required.", "danger")
            return render_template("auth/register.html")
        if password != confirm:
            flash("Passwords do not match.", "danger")
            return render_template("auth/register.html")
        if len(password) < 6:
            flash("Password must be at least 6 characters.", "danger")
            return render_template("auth/register.html")
        ok, msg = register_user(name, email, password, college, degree, year)
        if ok:
            session["email"] = email
            session["name"]  = name
            flash(f"Welcome {name}! Account created successfully!", "success")
            return redirect(url_for("dashboard"))
        flash(msg, "danger")
    return render_template("auth/register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email    = request.form["email"].strip().lower()
        password = request.form["password"]
        ok, user, msg = login_user(email, password)
        if ok:
            session["email"] = email
            session["name"]  = user["name"]
            flash(f"Welcome back, {user['name']}!", "success")
            return redirect(url_for("dashboard"))
        flash(msg, "danger")
    return render_template("auth/login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for("home"))

@app.route("/dashboard")
@login_required
def dashboard():
    user    = get_user(session["email"])
    history = get_history(session["email"])
    return render_template("dashboard.html", user=user, history=history[:5],
                           total_searches=len(history))

@app.route("/find-jobs", methods=["GET","POST"])
@login_required
def find_jobs():
    user         = get_user(session["email"])
    result       = None
    skills_input = ""
    if request.method == "POST":
        skills_input = request.form.get("skills","").strip()
        if not skills_input:
            flash("Please enter at least one skill.", "danger")
            return render_template("find_jobs.html", user=user, result=None)
        matched_jobs = match_jobs(skills_input)
        skill_gaps   = get_skill_gaps(skills_input, matched_jobs)
        if matched_jobs:
            save_history(session["email"], skills_input, matched_jobs, skill_gaps)
            result = {"jobs": matched_jobs, "gaps": skill_gaps,
                      "skills": skills_input, "found": True}
            flash(f"Found {len(matched_jobs)} matching jobs!", "success")
        else:
            result = {"found": False, "skills": skills_input}
            flash("No matches found. Try adding more skills!", "warning")
    return render_template("find_jobs.html", user=user, result=result,
                           skills_input=skills_input)

@app.route("/job/<job_title>")
@login_required
def job_detail(job_title):
    job = next((j for j in JOBS_DATABASE if j["title"] == job_title), None)
    if not job:
        flash("Job not found.", "danger")
        return redirect(url_for("find_jobs"))
    return render_template("job_detail.html", job=job)

@app.route("/browse")
@login_required
def browse():
    category   = request.args.get("category", "All")
    jobs       = JOBS_DATABASE if category == "All" else [j for j in JOBS_DATABASE if j["category"] == category]
    categories = ["All"] + sorted(get_all_categories())
    return render_template("browse.html", jobs=jobs, categories=categories, selected=category)

@app.route("/history")
@login_required
def history():
    hist = get_history(session["email"])
    return render_template("history.html", history=hist)

@app.route("/profile", methods=["GET","POST"])
@login_required
def profile():
    user = get_user(session["email"])
    if request.method == "POST":
        update_user(session["email"], {
            "name":    request.form["name"].strip(),
            "college": request.form.get("college","").strip(),
            "degree":  request.form.get("degree",""),
            "year":    request.form.get("year",""),
        })
        session["name"] = request.form["name"].strip()
        flash("Profile updated!", "success")
        return redirect(url_for("profile"))
    return render_template("profile.html", user=user)
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)













