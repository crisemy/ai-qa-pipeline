import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["title"] == "Buy Milk"

def test_get_todo_exists():
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_get_todo_not_found():
    response = client.get("/todos/999")
    assert response.status_code == 404

def test_create_todo():
    new_todo = {"id": 3, "title": "Test new todo", "completed": False}
    response = client.post("/todos/", json=new_todo)
    assert response.status_code == 201
    assert response.json()["title"] == "Test new todo"