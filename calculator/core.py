class Calculator:
    def __init__(self) -> None:
        pass

    def add(self, a: int | float, b: int | float) -> int | float:
        """
        Add two numbers
        param a: first number
        param b: second number
        return: sum of two numbers
        """
        return a + b

    def subtract(self, a: int | float, b: int | float) -> int | float:
        """
        Subtract two numbers
        param a: first number
        param b: second number
        return: difference of two numbers
        """
        return a - b

    def multiply(self, a: int | float, b: int | float) -> int | float:
        """
        Multiply two numbers
        param a: first number
        param b: second number
        return: product of two numbers
        """
        return a * b

    def divide(self, a: int | float, b: int | float) -> int | float:
        """
        Divide two numbers
        param a: first number
        param b: second number
        return: quotient of two numbers
        """
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError("Cannot divide by zero")

    def square(self, a: int | float) -> int | float:
        """
        Square a number
        param a: number
        return: square of a number
        """
        return a * a

    def sqrt(self, a: int | float) -> int | float:
        """
        Square root of a number
        param a: number
        return: square root of a number
        """
        return a**0.5

    def percent(self, a: int | float, b: int | float) -> int | float:
        """
        Percentage of a number
        param a: number
        param b: percentage
        return: percentage of a number
        """
        return a * b / 100
