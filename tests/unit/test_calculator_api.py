import pytest
from app.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def json_headers():
    return {"Content-Type": "application/json"}


def test_add(client, json_headers, json_data):
    response = client.post("/api/add/", headers=json_headers, json=json_data)
    assert response.status_code == 200
    assert response.json == 3


def test_subtract(client, json_headers, json_data):
    response = client.post("/api/subtract/", headers=json_headers, json=json_data)
    assert response.status_code == 200
    assert response.json == -1


def test_multiply(client, json_headers, json_data):
    response = client.post("/api/multiply/", headers=json_headers, json=json_data)
    assert response.status_code == 200
    assert response.json == 2


def test_divide(client, json_headers, json_data):
    response = client.post("/api/divide/", headers=json_headers, json=json_data)
    assert response.status_code == 200
    assert response.json == 0.5


def test_divide_by_zero(client, json_headers):
    response = client.post("/api/divide/", headers=json_headers, json={"a": 1, "b": 0})
    assert response.status_code == 400
    assert response.json == "Cannot divide by zero"
