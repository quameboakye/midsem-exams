from app.operations import addition, subtraction


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