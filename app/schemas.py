from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    completed: bool

class Task(TaskBase):
    id: int
    completed: bool

    class Config:
        from_attributes = True
