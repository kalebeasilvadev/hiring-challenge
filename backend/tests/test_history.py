import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.fixture(scope="session")
def test_login_json():
    response = client.post("/auth/token", json={"username": "admin", "password": "admin"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    return response.json()


@pytest.fixture(scope="session")
def test_headers(test_login_json):
    return {"Authorization": f"Bearer {test_login_json['access_token']}"}


def test_read_uploads(test_headers):
    response = client.get("/history/uploads/", headers=test_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
