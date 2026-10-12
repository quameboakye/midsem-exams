import math

def addition(a: float, b : float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def subtraction(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b

def multiplication(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def division(a: float, b: float) -> float:
    """Returns the quotient of two numbers. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def modulus(a: float, b: float) -> float:
    """Returns the remainder of a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a % b


def sqrt(a: float) -> float:
    """Returns the square root of a number. Raises ValueError if a is negative."""
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)