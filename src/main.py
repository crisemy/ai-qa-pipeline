from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Todo API - QA Automation Demo")

class TodoItem(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

todos: List[TodoItem] = [
    TodoItem(id=1, title="Comprar leche", completed=False),
    TodoItem(id=2, title="Estudiar RandomForest", completed=True),
]

@app.get("/todos/", response_model=List[TodoItem])
def get_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=TodoItem)
def get_todo(todo_id: int = Path(..., ge=1)):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.post("/todos/", response_model=TodoItem, status_code=201)
def create_todo(item: TodoItem):
    if any(t.id == item.id for t in todos):
        raise HTTPException(status_code=400, detail="ID already exists")
    todos.append(item)
    return item