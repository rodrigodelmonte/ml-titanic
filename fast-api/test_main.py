from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_survided_true():
    data = dict(
        Pclass=0,
        Parch=1,
        Age=30,
        Sex="female"
    )
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.text == '1'


def test_survided_false():
    data = dict(
        Pclass=2,
        Parch=0,
        Age=40,
        Sex="male"
    )
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.text == '0'
