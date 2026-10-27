from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_api_confirm_success():
    response = client.post("/orders/O001/confirm")
    assert response.status_code == 200
    assert response.json()["status"] == "CONFIRMED"

def test_api_confirm_not_found():
    response = client.post("/orders/O999/confirm")
    assert response.status_code == 404

def test_api_confirm_twice_conflict():
    client.post("/orders/O013/confirm") # Primer intento
    response = client.post("/orders/O013/confirm") # Segundo intento
    assert response.status_code == 409
    assert "Solo DRAFT" in response.json()["detail"]