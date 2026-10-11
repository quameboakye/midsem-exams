import pytest
from app.operations import addition, subtraction, multiplication, division


def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
    assert addition(2.5, 3.5) == 6.0 
    assert addition(1982, 44) == 2026  

def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(-1, -1) == 0
    assert subtraction(0, 0) == 0
    assert subtraction(2.5, 1.5) == 1.0
    assert subtraction(2026, 1982) == 44

def test_multiplication():
    from app.operations import multiplication
    assert multiplication(2, 3) == 6
    assert multiplication(-1, 1) == -1
    assert multiplication(0, 5) == 0
    assert multiplication(2.5, 4) == 10.0
    assert multiplication(1982, 44) == 87208

def test_division_positive():
    assert division(6, 3) == 2
    assert division(1, 1) == 1

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        division(10, 0)
   