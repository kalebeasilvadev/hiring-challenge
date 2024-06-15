from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_login_json():
    response = client.post(
        "/auth/token",
        json={"username": "admin", "password": "admin"},
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
