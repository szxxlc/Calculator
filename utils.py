"""Module with basic calculator functions: add, subtract, multiply, divide."""


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Divide two numbers."""
    return a / b


def to_binary(n: int) -> str:
    """Convert an integer (0–100) to its binary representation.

    Raises:
        TypeError: If input is not an integer.
        ValueError: If number is not in range 0 to 100.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0 or n > 100:
        raise ValueError("Number must be in range 0 to 100")
    return bin(n)[2:]
