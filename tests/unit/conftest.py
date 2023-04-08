import pytest
from calculator.core import Calculator
from app.app import app


@pytest.fixture(scope="module")
def calculator():
    return Calculator(2, 3)


@pytest.fixture
def custom_calculator(scope="module"):
    def _calculator(a, b):
        return Calculator(a, b)

    return _calculator


@pytest.fixture(scope="module")
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="module")
def json_headers():
    return {"Content-Type": "application/json"}


@pytest.fixture(scope="module")
def json_data():
    return {"a": 1, "b": 2}
