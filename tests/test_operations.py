import pytest
from app.operations import addition, subtraction, multiplication, division, modulus, sqrt


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
def test_addition(a, b, expected):
    assert addition(a, b) == expected


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
def test_subtraction(a, b, expected):
    assert subtraction(a, b) == expected


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
def test_multiplication(a, b, expected):
    assert multiplication(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),
        (1, 1, 1),
    ],
    ids=["evenly_divisible", "identity"],
)
def test_division_positive(a, b, expected):
    assert division(a, b) == expected


@pytest.mark.parametrize(
    "a",
    [10, 0, -5, 2.5],
    ids=["positive", "zero", "negative", "float"],
)
def test_division_by_zero(a):
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        division(a, 0)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 3, 1),
        (-10, 3, 2),  # Python's modulo takes the sign of the divisor
        (5.5, 2, 1.5),
    ],
    ids=["positive", "negative_dividend", "float"],
)
def test_modulus(a, b, expected):
    assert modulus(a, b) == expected


@pytest.mark.parametrize(
    "a",
    [10, 0, -5, 5.5],
    ids=["positive", "zero", "negative", "float"],
)
def test_modulus_by_zero(a):
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        modulus(a, 0)


@pytest.mark.parametrize(
    "value, expected",
    [
        (9, 3),
        (0, 0),
        (2.25, 1.5),
    ],
    ids=["perfect_square", "zero", "float"],
)
def test_sqrt(value, expected):
    assert sqrt(value) == expected


@pytest.mark.parametrize(
    "value",
    [-4, -1, -0.5],
    ids=["neg_int", "neg_one", "neg_float"],
)
def test_sqrt_negative(value):
    with pytest.raises(ValueError, match="Cannot take the square root of a negative number."):
        sqrt(value)