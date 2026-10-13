import datetime

import pytest

from app.calculation import Calculation, CalculationFactory
from app.calculator_memento import CalculatorMemento


def test_calculation_to_dict():
    calc = CalculationFactory.create_calculation("add", 2, 3)
    assert calc.to_dict() == {
        "operation": "add",
        "operand1": "2",
        "operand2": "3",
        "result": "5",
    }


def test_calculation_from_dict():
    calc = Calculation.from_dict(
        {"operation": "multiply", "operand1": "4", "operand2": "3", "result": "12"}
    )
    assert calc.operation == "Multiply"
    assert calc.operand1 == 4
    assert calc.result == 12


def test_calculation_from_dict_unknown_operation():
    with pytest.raises(ValueError):
        Calculation.from_dict({"operation": "nope", "operand1": "1", "operand2": "1"})


def test_memento_default_timestamp():
    memento = CalculatorMemento(history=[])
    assert isinstance(memento.timestamp, datetime.datetime)


def test_memento_to_dict():
    stamp = datetime.datetime(2026, 10, 12, 20, 0, 0)
    calc = CalculationFactory.create_calculation("add", 1, 1)
    data = CalculatorMemento(history=[calc], timestamp=stamp).to_dict()
    assert data["timestamp"] == stamp.isoformat()
    assert data["history"] == [calc.to_dict()]


def test_memento_round_trip():
    stamp = datetime.datetime(2026, 10, 12, 20, 0, 0)
    calc = CalculationFactory.create_calculation("subtract", 9, 4)
    restored = CalculatorMemento.from_dict(
        CalculatorMemento(history=[calc], timestamp=stamp).to_dict()
    )
    assert restored.timestamp == stamp
    assert len(restored.history) == 1
    assert restored.history[0].operation == "Subtract"
    assert restored.history[0].result == 5
