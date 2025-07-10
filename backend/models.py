from sqlalchemy import Column, Integer, String, Boolean
from backend.database import Base

class MoodTask(Base):
    __tablename__ = "mood_tasks"

    id = Column(Integer, primary_key=True, index=True)
    mood = Column(String)
    quote = Column(String)
    suggestion = Column(String)
    is_custom = Column(Boolean, default=False)
    is_completed = Column(Boolean, default=False)
