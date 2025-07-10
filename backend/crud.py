from sqlalchemy.orm import Session
from backend import models, schemas

def get_all_tasks(db: Session):
    return db.query(models.MoodTask).all()

def create_task(db: Session, task: schemas.MoodTaskCreate):
    db_task = models.MoodTask(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def complete_task(db: Session, task_id: int):
    task = db.query(models.MoodTask).filter(models.MoodTask.id == task_id).first()
    if task:
        task.is_completed = True
        db.commit()
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(models.MoodTask).filter(models.MoodTask.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task
