from starlette.testclient import TestClient

from main import app

client = TestClient(app)

data = dict(
    Pclass=0,
    Age=30,
    Sex="female"
)


def test_response_length():
    response = client.post("/predict", json=data)
    assert len(response.text) == 1


def test_survided_true():
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.text == '1'


def test_survided_false():
    data = dict(
        Pclass=2,
        Age=40,
        Sex="male"
    )
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.text == '0'
