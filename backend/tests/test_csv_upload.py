from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_upload_file():
    response = client.post(
        "/csv/uploadfile/",
        files={"file": ("test.csv", "column1,column2\nvalue1,value2\nvalue3,value4")},
    )
    assert response.status_code == 200
    assert response.json()["filename"] == "test.csv"
