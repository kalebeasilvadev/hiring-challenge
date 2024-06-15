import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.fixture(scope="session")
def test_login_json():
    response = client.post(
        "/auth/token", json={"username": "admin", "password": "admin"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    return response.json()


@pytest.fixture(scope="session")
def test_headers(test_login_json):
    return {"Authorization": f"Bearer {test_login_json['access_token']}"}


def test_create_user(test_headers):
    response = client.post(
        "/user/users/",
        headers=test_headers,
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword",
        },
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert "id" in response.json()
