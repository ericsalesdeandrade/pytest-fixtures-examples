import pytest
from calculator.core import Calculator

@pytest.fixture
def calculator():
    return Calculator(2, 3)


## Basic Calculator Testing with Predefined Fixture
def test_add(calculator):
    assert calculator.add() == 5


def test_subtract(calculator):
    assert calculator.subtract() == -1


def test_multiply(calculator):
    assert calculator.multiply() == 6


def test_divide(calculator):
    assert calculator.divide() == 0.6666666666666666


def test_divide_by_zero(calculator):
    calculator.b = 0
    with pytest.raises(ZeroDivisionError):
        calculator.divide()


# Advanced Calculator Testing with Dynamic Fixture
def test_add_advanced(custom_calculator):
    assert custom_calculator(10, 20).add() == 30


def test_subtract_advanced(custom_calculator):
    assert custom_calculator(10, 20).subtract() == -10


def test_multiply_advanced(custom_calculator):
    assert custom_calculator(10, 20).multiply() == 200


def test_divide_advanced(custom_calculator):
    assert custom_calculator(10, 20).divide() == 0.5


def test_divide_by_zero_advanced(custom_calculator):
    with pytest.raises(ZeroDivisionError):
        custom_calculator(10, 0).divide()
