from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import models, schemas, crud
from backend.database import SessionLocal, engine
import random

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Mood-Based Planner")

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Mood-based AI suggestion logic
def mood_suggestion(mood: str):
    mood = mood.lower()
    suggestions = {
        "happy": ("Happiness is contagious!", "Celebrate your wins and help someone today."),
        "stressed": ("Breathe in, breathe out.", "Do one small thing at a time."),
        "bored": ("Your creativity is waiting!", "Try a new hobby or read something different."),
        "sad": ("You are not alone.", "Take a walk or talk to a friend."),
    }
    return suggestions.get(mood, ("Take a pause.", "Do one kind thing for yourself."))

@app.post("/mood", response_model=schemas.MoodTaskOut)
def get_mood_response(mood: schemas.MoodInput, db: Session = Depends(get_db)):
    quote, suggestion = mood_suggestion(mood.mood)
    task_data = schemas.MoodTaskCreate(
        mood=mood.mood,
        quote=quote,
        suggestion=suggestion,
        is_custom=False
    )
    return crud.create_task(db, task_data)

@app.get("/tasks", response_model=list[schemas.MoodTaskOut])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_all_tasks(db)

@app.put("/tasks/{task_id}", response_model=schemas.MoodTaskOut)
def complete(task_id: int, db: Session = Depends(get_db)):
    task = crud.complete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Deleted"}
