from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_login_form():
    response = client.post(
        "/auth/token", data={"username": "testuser", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_json():
    # Tentar fazer login com JSON
    response = client.post(
        "/auth/token", json={"username": "testuser", "password": "testpassword"}
    )
    print(response.text)
    assert response.status_code == 200
    assert "access_token" in response.json()
