from pydantic import BaseModel
from typing import Optional

# Schema para a criação de uma tarefa
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

# Schema para a resposta (inclui o ID e o status)
class Task(TaskCreate):
    id: int
    is_completed: bool

    class Config:
        from_attributes = True