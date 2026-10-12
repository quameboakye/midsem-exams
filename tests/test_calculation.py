import pytest
from app.calculation import (
    Calculation,
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
)


@pytest.mark.parametrize(
    "calc_type, a, b, expected, cls",
    [
        ("add", 2, 3, 5, AddCalculation),
        ("subtract", 5, 3, 2, SubtractCalculation),
        ("multiply", 4, 3, 12, MultiplyCalculation),
        ("divide", 10, 2, 5, DivideCalculation),
    ],
)
def test_factory_creates_and_executes(calc_type, a, b, expected, cls):
    calc = CalculationFactory.create_calculation(calc_type, a, b)
    assert isinstance(calc, cls)
    assert calc.execute() == expected


def test_factory_is_case_insensitive():
    calc = CalculationFactory.create_calculation("ADD", 1, 2)
    assert isinstance(calc, AddCalculation)


def test_divide_by_zero():
    calc = CalculationFactory.create_calculation("divide", 5, 0)
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calc.execute()


def test_unsupported_calculation_type():
    with pytest.raises(ValueError, match="Unsupported calculation type"):
        CalculationFactory.create_calculation("unknown", 1, 2)


def test_duplicate_registration():
    with pytest.raises(ValueError, match="already registered"):
        @CalculationFactory.register_calculation("add")
        class DuplicateAdd(Calculation):
            def execute(self):
                return 0  # pragma: no cover


def test_str():
    calc = CalculationFactory.create_calculation("add", 2, 3)
    assert str(calc) == "AddCalculation: 2 Add 3 = 5"


def test_repr():
    calc = CalculationFactory.create_calculation("add", 2, 3)
    assert repr(calc) == "AddCalculation(a=2, b=3)"