import csv
from unittest.mock import Mock

import pytest

from app.calculation import CalculationFactory
from app.calculator.engine import Calculator
from app.calculator_config import CalculatorConfig


@pytest.fixture
def calc(tmp_path):
    config = CalculatorConfig(
        history_file=str(tmp_path / "history" / "history.csv"),
        log_file=str(tmp_path / "calc.log"),
    )
    return Calculator(config)


def test_default_config():
    assert Calculator().config.auto_save is True


def test_calculation_properties():
    calculation = CalculationFactory.create_calculation("add", 2, 3)
    assert calculation.operation == "Add"
    assert calculation.operand1 == 2
    assert calculation.operand2 == 3
    assert calculation.result == 5


def test_perform_operation_stores_history(calc):
    assert calc.perform_operation("add", 1, 1) == 2
    assert len(calc.history) == 1


def test_perform_operation_defaults_second_operand(calc):
    assert calc.perform_operation("sqrt", 9) == 3


def test_failed_operation_is_not_stored(calc):
    with pytest.raises(ZeroDivisionError):
        calc.perform_operation("divide", 1, 0)
    assert calc.history == []


def test_observers_are_notified(calc):
    observer = Mock()
    calc.add_observer(observer)
    calc.perform_operation("add", 1, 1)
    observer.update.assert_called_once_with(calc.history[0])


def test_show_history(calc):
    calc.perform_operation("add", 1, 1)
    entries = calc.show_history()
    assert len(entries) == 1
    assert entries[0].startswith("1. ")


def test_undo_and_redo(calc):
    calc.perform_operation("add", 1, 1)
    assert calc.undo() is True
    assert calc.history == []
    assert calc.redo() is True
    assert len(calc.history) == 1


def test_undo_empty_returns_false(calc):
    assert calc.undo() is False


def test_redo_empty_returns_false(calc):
    assert calc.redo() is False


def test_new_operation_clears_redo_stack(calc):
    calc.perform_operation("add", 1, 1)
    calc.undo()
    calc.perform_operation("add", 2, 2)
    assert calc.redo() is False


def test_clear_history(calc):
    calc.perform_operation("add", 1, 1)
    calc.clear_history()
    assert calc.history == []


def test_save_history_writes_csv(calc):
    calc.perform_operation("add", 1, 1)
    calc.save_history()
    with open(calc.config.history_file, newline="") as file:
        rows = list(csv.reader(file))
    assert rows[0] == ["operation", "operand1", "operand2", "result"]
    assert rows[1] == ["Add", "1", "1", "2"]


def test_save_history_bare_filename(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    calc = Calculator(CalculatorConfig(history_file="history.csv"))
    calc.save_history()
    assert (tmp_path / "history.csv").exists()