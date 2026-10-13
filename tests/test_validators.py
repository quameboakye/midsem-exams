from decimal import Decimal

import pytest

from app.calculator_config import CalculatorConfig
from app.exceptions import (
    CalculatorError,
    ConfigurationError,
    OperationError,
    ValidationError,
)
from app.input_validators import InputValidator


@pytest.fixture
def config():
    return CalculatorConfig(max_input_value=Decimal("1000"))


def test_valid_integer_string(config):
    assert InputValidator.validate_number("5", config) == Decimal("5")


def test_valid_number_with_spaces(config):
    assert InputValidator.validate_number("  2.5  ", config) == Decimal("2.5")


def test_valid_float_input(config):
    assert InputValidator.validate_number(3.5, config) == Decimal("3.5")


def test_negative_number(config):
    assert InputValidator.validate_number("-7", config) == Decimal("-7")


def test_value_is_normalized(config):
    assert str(InputValidator.validate_number("2.500", config)) == "2.5"


def test_value_at_limit_is_allowed(config):
    assert InputValidator.validate_number("1000", config) == Decimal("1000")


def test_value_over_limit_raises(config):
    with pytest.raises(ValidationError, match="exceeds maximum"):
        InputValidator.validate_number("1001", config)


def test_negative_value_over_limit_raises(config):
    with pytest.raises(ValidationError, match="exceeds maximum"):
        InputValidator.validate_number("-1001", config)


def test_non_numeric_raises(config):
    with pytest.raises(ValidationError, match="Invalid number format"):
        InputValidator.validate_number("abc", config)


def test_exception_hierarchy():
    assert issubclass(ValidationError, CalculatorError)
    assert issubclass(OperationError, CalculatorError)
    assert issubclass(ConfigurationError, CalculatorError)
