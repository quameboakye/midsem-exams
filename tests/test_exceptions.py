import pytest
from app.exceptions import (
    CalculatorError,
    OperationError,
    ValidationError,
    HistoryError,
    ConfigurationError,
)


def test_calculator_error_base():
    err = CalculatorError("Base error")
    assert str(err) == "Base error"
    assert isinstance(err, Exception)


def test_derived_exceptions():
    op_err = OperationError("Invalid operation")
    val_err = ValidationError("Invalid input")
    hist_err = HistoryError("History load failed")
    config_err = ConfigurationError("Config missing")

    assert isinstance(op_err, CalculatorError)
    assert isinstance(val_err, CalculatorError)
    assert isinstance(hist_err, CalculatorError)
    assert isinstance(config_err, CalculatorError)