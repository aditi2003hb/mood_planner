from pydantic import BaseModel

class MoodInput(BaseModel):
    mood: str

class MoodTaskCreate(BaseModel):
    mood: str
    quote: str
    suggestion: str
    is_custom: bool = False

class MoodTaskOut(BaseModel):
    id: int
    mood: str
    quote: str
    suggestion: str
    is_custom: bool
    is_completed: bool

    class Config:
        orm_mode = True
