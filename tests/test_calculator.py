import pytest
from unittest.mock import patch
from decimal import Decimal
from app.calculator import Calculator, calculator


def test_calculator_class_methods():
    calc = Calculator()
    calc.clear_history()

    # Basic Operations via Calculator instance
    assert calc.perform_operation("add", Decimal("5"), Decimal("3")) == Decimal("8")
    assert calc.perform_operation("subtract", Decimal("10"), Decimal("4")) == Decimal("6")
    assert calc.perform_operation("multiply", Decimal("4"), Decimal("2")) == Decimal("8")
    assert calc.perform_operation("divide", Decimal("12"), Decimal("3")) == Decimal("4")
    assert calc.perform_operation("modulus", Decimal("10"), Decimal("3")) == Decimal("1")
    assert calc.perform_operation("sqrt", Decimal("16")) == Decimal("4")

    # History & Memento tracking using history property/show_history
    history = calc.history if hasattr(calc, "history") else calc.show_history()
    assert len(history) == 6

    assert calc.undo() is True
    history_after_undo = calc.history if hasattr(calc, "history") else calc.show_history()
    assert len(history_after_undo) == 5

    assert calc.redo() is True
    history_after_redo = calc.history if hasattr(calc, "history") else calc.show_history()
    assert len(history_after_redo) == 6

    calc.clear_history()
    history_cleared = calc.history if hasattr(calc, "history") else calc.show_history()
    assert len(history_cleared) == 0


def test_calculator_factory_runner():
    # Mock input to feed 'exit' so calculator() REPL doesn't block stdin
    with patch("builtins.input", side_effect=["exit"]):
        calculator()