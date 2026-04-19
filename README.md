# 🚀 Smart Career & Job Guidance Portal

A web-based application that helps users explore career paths, find jobs, and manage their career journey effectively.
---

## 🌐 Live Demo

👉 https://smart-career-job-guidence.onrender.com

---

## 📌 Features

* 🔐 User Registration & Login
* 💼 Job Search & Recommendations
* 📊 Career Guidance System
* 📝 User History Tracking
* 📂 JSON-based Data Storage

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Python (Flask)
* **Server:** Gunicorn
* **Deployment:** Render

---

## 📁 Project Structure

```
career_v2/
│
├── app.py
├── jobs_db.py
├── storage.py
├── requirements.txt
├── Procfile
│
├── data/
│   ├── users.json
│   └── history.json
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── auth/
│   └── ...
│
└── static/
```

---

## ⚙️ Installation (Run Locally)

```bash
git clone https://github.com/nirnaya14/Smart_Career_Job_Guidence.git
cd Smart_Career_Job_Guidence
pip install -r requirements.txt
python app.py
```

Open: http://127.0.0.1:5000/

---

## 🚀 Deployment

Deployed using Render.

* **Build Command:**
  `pip install -r requirements.txt`

* **Start Command:**
  `gunicorn app:app`

---

## ⚠️ Notes

* Ensure JSON files exist in `/data` folder
* Backend must run for full functionality
* Free Render instance may sleep when inactive

---

⭐ If you like this project, give it a star on GitHub!
