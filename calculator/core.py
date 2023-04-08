class Calculator:
    def __init__(self, a: int | float = None, b: int | float = None) -> None:
        self.a = a
        self.b = b

    def add(self) -> int | float:
        """
        Add two numbers
        return: sum of two numbers
        """
        return self.a + self.b

    def subtract(self) -> int | float:
        """
        Subtract two numbers
        return: difference of two numbers
        """
        return self.a - self.b

    def multiply(self) -> int | float:
        """
        Multiply two numbers
        return: product of two numbers
        """
        return self.a * self.b

    def divide(self) -> int | float:
        """
        Divide two numbers
        return: quotient of two numbers
        """
        if self.b != 0:
            return self.a / self.b
        else:
            raise ZeroDivisionError("Cannot divide by zero")

    def square(self) -> int | float:
        """
        Square a number
        return: square of a number
        """
        return self.a**2
