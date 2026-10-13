from decimal import Decimal
import pytest

from app.exceptions import ValidationError
from app.input_validators import InputValidator, parse_number, validate_number


def test_parse_number_valid():
    assert parse_number(10) == Decimal("10")
    assert parse_number("3.14") == Decimal("3.14")
    assert parse_number(Decimal("5.5")) == Decimal("5.5")


def test_parse_number_invalid():
    with pytest.raises(ValidationError, match="Invalid numeric input"):
        parse_number("invalid_number")


def test_validate_number_alias():
    assert validate_number("42") == Decimal("42")


def test_input_validator_class_methods():
    assert InputValidator.parse_number("100") == Decimal("100")
    assert InputValidator.validate_number("200") == Decimal("200")

    with pytest.raises(ValidationError, match="Invalid numeric input"):
        InputValidator.parse_number("abc")