# 🎭 AI Mood-Based Daily Planner

An interactive, mood-driven productivity app built with **FastAPI**, **SQLAlchemy**, **Pydantic**, and a beautiful **JavaScript frontend**. Users select their current mood and receive a motivational quote and task suggestion based on it. Tasks can be viewed, marked as complete, or deleted.


## ✨ Features

- 🌈 Mood-based suggestion generator (Happy, Stressed, Bored, Sad)
- 💡 Instant motivational quote + productivity tip
- 🧠 Backend built with FastAPI, SQLAlchemy, and Pydantic
- 🎨 Interactive and themed frontend (vanilla JS, CSS)
- 📋 Task list with complete/delete functionality
- 🗃️ SQLite database support

---

## 📸 Preview

![Mood-Based Planner UI](https://dummyimage.com/700x400/00ffff/000&text=Mood+Planner+Preview)  
*(Replace this with a real screenshot after launching)*

---

## 🛠 Tech Stack

| Layer      | Tools Used                        |
|------------|-----------------------------------|
| Backend    | FastAPI, SQLAlchemy, Pydantic     |
| Frontend   | HTML, CSS, Vanilla JavaScript     |
| Database   | SQLite                            |
| Server     | Hypercorn (Python 3.13 compatible)|

---

## 🚀 Getting Started

### 🔧 Install Requirements

Make sure Python 3.13 is installed.

```bash
pip install -r requirements.txt
```

**`requirements.txt`:**
```
fastapi
sqlalchemy
pydantic
hypercorn
```

---

### 📂 Project Structure

```
mood_planner/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── requirements.txt
└── README.md
```

---

### ▶️ Run the Backend

```bash
hypercorn backend.main:app
```

Visit API docs here: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 🌐 Open the Frontend

Open `frontend/index.html` in your browser:

- ✅ Double-click the file  
- ✅ Or use VS Code Live Server extension  
- ✅ It makes API calls to FastAPI backend

---

## 📚 API Endpoints

| Method | Endpoint           | Description                      |
|--------|--------------------|----------------------------------|
| POST   | `/mood`            | Generate quote + task from mood |
| GET    | `/tasks`           | View all saved tasks            |
| PUT    | `/tasks/{task_id}` | Mark a task as completed        |
| DELETE | `/tasks/{task_id}` | Delete a task                   |

---

## 🤖 AI Logic (Python)

```python
def mood_suggestion(mood: str):
    if mood == "happy":
        return ("Happiness is contagious!", "Celebrate and help someone today.")
    elif mood == "stressed":
        return ("Breathe in, breathe out.", "Break tasks into small chunks.")
    elif mood == "bored":
        return ("Time to spark curiosity!", "Try a new hobby for 15 mins.")
    elif mood == "sad":
        return ("You are not alone.", "Go outside or talk to someone.")
    else:
        return ("Pause. Reflect. Breathe.", "Do something gentle for yourself.")
```

---

## ✅ To-Do & Future Enhancements

- [ ] Add user accounts (login/signup)
- [ ] Sync tasks across sessions (localStorage/db)
- [ ] Host backend on Render/Vercel & frontend on Netlify
- [ ] Add animations to mood transitions

---

## 👩‍💻 Author

Made by Aditi   
GitHub: [https://github.com/aditi2003hb](https://github.com/aditi2003hb)

---

## 📄 License

MIT License
