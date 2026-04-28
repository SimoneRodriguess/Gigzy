from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI(
    title="Gigzy API",
    description="Demand-driven hyperlocal micro-gig marketplace",
    version="0.1.0"
)

# Temporary in-memory storage
TASKS = []

class Task(BaseModel):
    title: str
    description: str
    category: str
    location: str
    budget: float

class TaskResponse(Task):
    id: str

@app.get("/")
def home():
    return {
        "message": "Welcome to Gigzy API 🚀",
        "status": "running"
    }

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: Task):
    new_task = {
        "id": str(uuid.uuid4()),
        **task.dict()
    }
    TASKS.append(new_task)
    return new_task

@app.get("/tasks", response_model=List[TaskResponse])
def get_tasks():
    return TASKS
