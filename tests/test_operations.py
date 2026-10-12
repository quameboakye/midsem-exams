from typing import Union

import pytest

from app.operations import Operations

Number = Union[int, float]


@pytest.mark.parametrize(
    "a, b, expected",
    [(2, 3, 5), (-1, 1, 0), (0, 0, 0), (2.5, 3.5, 6.0), (1982, 44, 2026)],
    ids=["positive", "negative_plus_positive", "zeros", "floats", "large_ints"],
)
def test_addition(a: Number, b: Number, expected: Number) -> None:
    """Test that Operations.addition(a, b) returns the expected sum."""
    result = Operations.addition(a, b)
    assert result == expected, f"Expected Operations.addition({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a, b, expected",
    [(5, 3, 2), (-1, -1, 0), (0, 0, 0), (2.5, 1.5, 1.0), (2026, 1982, 44)],
    ids=["positive", "negatives", "zeros", "floats", "large_ints"],
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    """Test that Operations.subtraction(a, b) returns a minus b."""
    result = Operations.subtraction(a, b)
    assert result == expected, f"Expected Operations.subtraction({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a, b, expected",
    [(2, 3, 6), (-1, 1, -1), (0, 5, 0), (2.5, 4, 10.0), (1982, 44, 87208)],
    ids=["positive", "negative_times_positive", "zero", "float_times_int", "large_ints"],
)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    """Test that Operations.multiplication(a, b) returns the expected product."""
    result = Operations.multiplication(a, b)
    assert result == expected, f"Expected Operations.multiplication({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a, b, expected",
    [(6, 3, 2), (1, 1, 1)],
    ids=["evenly_divisible", "identity"],
)
def test_division_positive(a: Number, b: Number, expected: Number) -> None:
    """Test that Operations.division(a, b) returns a divided by b."""
    result = Operations.division(a, b)
    assert result == expected, f"Expected Operations.division({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a",
    [10, 0, -5, 2.5],
    ids=["positive", "zero", "negative", "float"],
)
def test_division_by_zero(a: Number) -> None:
    """Test that dividing by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero.") as excinfo:
        Operations.division(a, 0)

    assert "Cannot divide by zero." in str(excinfo.value)


@pytest.mark.parametrize(
    "a, b, expected",
    [(10, 3, 1), (-10, 3, 2), (5.5, 2, 1.5)],
    ids=["positive", "negative_dividend", "float"],
)
def test_modulus(a: Number, b: Number, expected: Number) -> None:
    """Test that Operations.modulus(a, b) returns the remainder."""
    result = Operations.modulus(a, b)
    assert result == expected, f"Expected Operations.modulus({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a",
    [10, 0, -5, 5.5],
    ids=["positive", "zero", "negative", "float"],
)
def test_modulus_by_zero(a: Number) -> None:
    """Test that modulus by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero.") as excinfo:
        Operations.modulus(a, 0)

    assert "Cannot divide by zero." in str(excinfo.value)


@pytest.mark.parametrize(
    "value, expected",
    [(9, 3), (0, 0), (2.25, 1.5)],
    ids=["perfect_square", "zero", "float"],
)
def test_sqrt(value: Number, expected: Number) -> None:
    """Test that Operations.sqrt(value) returns the square root."""
    result = Operations.sqrt(value)
    assert result == expected, f"Expected Operations.sqrt({value}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "value",
    [-4, -1, -0.5],
    ids=["neg_int", "neg_one", "neg_float"],
)
def test_sqrt_negative(value: Number) -> None:
    """Test that sqrt of a negative number raises ValueError."""
    with pytest.raises(ValueError, match="Cannot take the square root of a negative number.") as excinfo:
        Operations.sqrt(value)

    assert "Cannot take the square root of a negative number." in str(excinfo.value)


@pytest.mark.parametrize(
    "a, b, expected",
    [(2, 3, 8), (5, 0, 1), (2, -1, 0.5), (0, 5, 0), (2.5, 2, 6.25)],
    ids=["positive", "zero_exponent", "negative_exponent", "zero_base", "float_base"],
)
def test_power(a: Number, b: Number, expected: Number) -> None:
    """Test that Operations.power(a, b) returns a raised to the power of b."""
    result = Operations.power(a, b)
    assert result == expected, f"Expected Operations.power({a}, {b}) to be {expected}, but got {result}"
