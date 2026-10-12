

from typing import Union

import pytest

from app.operations import Operations

Number = Union[int, float]


# ---------------------------------------------------------------------------
# Addition
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (2.5, 3.5, 6.0),
        (1982, 44, 2026),
    ],
    ids=["positive", "negative_plus_positive", "zeros", "floats", "large_ints"],
)
def test_addition(a: Number, b: Number, expected: Number) -> None:
    """
    Test that Operations.addition(a, b) returns the expected sum.

    Parameters:
        a: first number
        b: second number
        expected: the sum we expect Operations.addition(a, b) to return
    """
    result = Operations.addition(a, b)
    assert result == expected, f"Expected Operations.addition({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------------------------------------
# Subtraction
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (-1, -1, 0),
        (0, 0, 0),
        (2.5, 1.5, 1.0),
        (2026, 1982, 44),
    ],
    ids=["positive", "negatives", "zeros", "floats", "large_ints"],
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    """
    Test that Operations.subtraction(a, b) returns a minus b.

    Parameters:
        a: the number to subtract from
        b: the number being subtracted
        expected: the difference we expect Operations.subtraction(a, b) to return
    """
    result = Operations.subtraction(a, b)
    assert result == expected, f"Expected Operations.subtraction({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------------------------------------
# Multiplication
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (-1, 1, -1),
        (0, 5, 0),
        (2.5, 4, 10.0),
        (1982, 44, 87208),
    ],
    ids=["positive", "negative_times_positive", "zero", "float_times_int", "large_ints"],
)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    """
    Test that Operations.multiplication(a, b) returns the expected product.

    Parameters:
        a: first number
        b: second number
        expected: the product we expect Operations.multiplication(a, b) to return
    """
    result = Operations.multiplication(a, b)
    assert result == expected, f"Expected Operations.multiplication({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------------------------------------
# Division
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),
        (1, 1, 1),
    ],
    ids=["evenly_divisible", "identity"],
)
def test_division_positive(a: Number, b: Number, expected: Number) -> None:
    """
    Test that Operations.division(a, b) returns a divided by b when b is not zero.

    Parameters:
        a: the dividend
        b: the divisor (non-zero)
        expected: the quotient we expect Operations.division(a, b) to return
    """
    result = Operations.division(a, b)
    assert result == expected, f"Expected Operations.division({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a",
    [10, 0, -5, 2.5],
    ids=["positive", "zero", "negative", "float"],
)
def test_division_by_zero(a: Number) -> None:
    """
    Test that dividing any number by zero raises a ValueError and that the
    error message clearly tells the user what went wrong.

    Parameters:
        a: the dividend (the divisor is always 0 in this test)

    Example: test_division_by_zero(-5) calls Operations.division(-5, 0), which must
    raise ValueError("Cannot divide by zero.").
    """
    
    with pytest.raises(ValueError, match="Cannot divide by zero.") as excinfo:
        # Attempt to divide 'a' by 0, which should raise a ValueError.
        Operations.division(a, 0)

    
    assert "Cannot divide by zero." in str(excinfo.value), (
        f"Expected error message 'Cannot divide by zero.' "
        f"but got '{excinfo.value}'"
    )


# ---------------------------------------------------------------------------
# Modulus
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 3, 1),
        (-10, 3, 2), 
        (5.5, 2, 1.5),
    ],
    ids=["positive", "negative_dividend", "float"],
)
def test_modulus(a: Number, b: Number, expected: Number) -> None:
    """
    Test that Operations.modulus(a, b) returns the remainder of a divided by b.

    Parameters:
        a: the dividend
        b: the divisor (non-zero)
        expected: the remainder we expect Operations.modulus(a, b) to return
    """
    result = Operations.modulus(a, b)
    assert result == expected, f"Expected Operations.modulus({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a",
    [10, 0, -5, 5.5],
    ids=["positive", "zero", "negative", "float"],
)
def test_modulus_by_zero(a: Number) -> None:
    """
    Test that taking any number modulo zero raises a ValueError and that the
    error message clearly tells the user what went wrong.

    Parameters:
        a: the dividend (the divisor is always 0 in this test)

    Example: test_modulus_by_zero(10) calls Operations.modulus(10, 0), which must
    raise ValueError("Cannot divide by zero.").
    """
    
    with pytest.raises(ValueError, match="Cannot divide by zero.") as excinfo:
        # Attempt a modulus by zero, which should raise a ValueError.
        Operations.modulus(a, 0)

    assert "Cannot divide by zero." in str(excinfo.value), (
        f"Expected error message 'Cannot divide by zero.' "
        f"but got '{excinfo.value}'"
    )


# ---------------------------------------------------------------------------
# Square root
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "value, expected",
    [
        (9, 3),
        (0, 0),
        (2.25, 1.5),
    ],
    ids=["perfect_square", "zero", "float"],
)
def test_sqrt(value: Number, expected: Number) -> None:
    """
    Test that Operations.sqrt(value) returns the square root of a non-negative number.

    Parameters:
        value: a number that is zero or greater
        expected: the square root we expect Operations.sqrt(value) to return
    """
    result = Operations.sqrt(value)
    assert result == expected, f"Expected Operations.sqrt({value}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "value",
    [-4, -1, -0.5],
    ids=["neg_int", "neg_one", "neg_float"],
)
def test_sqrt_negative(value: Number) -> None:
    """
    Test that taking the square root of a negative number raises a ValueError
    and that the error message clearly tells the user what went wrong.

    Parameters:
        value: a negative number

    Example: test_sqrt_negative(-4) calls Operations.sqrt(-4), which must raise
    ValueError("Cannot take the square root of a negative number.").
    """
    
    with pytest.raises(ValueError, match="Cannot take the square root of a negative number.") as excinfo:
        
        Operations.sqrt(value)


    assert "Cannot take the square root of a negative number." in str(excinfo.value), (
        f"Expected error message 'Cannot take the square root of a negative number.' "
        f"but got '{excinfo.value}'"
    )