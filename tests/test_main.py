# test_main.py

from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item():
    response = client.get("/items/1?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "query": "test"}

def test_read_item_without_query():
    response = client.get("/items/2")
    assert response.status_code == 200
    assert response.json() == {"item_id": 2, "query": None}
