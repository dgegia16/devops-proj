from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_status_fields():
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert "hostname" in data
    assert data["disk_total_gb"] > 0

