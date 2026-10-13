"""Input validation utilities for calculator operands and commands."""

from decimal import Decimal, InvalidOperation
from numbers import Number
from typing import Union

from app.exceptions import ValidationError


def parse_number(val: Union[str, int, float, Decimal]) -> Decimal:
    """
    Parse an input into a Decimal number.

    Args:
        val: The value to parse into Decimal.

    Returns:
        Decimal: The parsed Decimal representation.

    Raises:
        ValidationError: If the input cannot be converted to Decimal.
    """
    if isinstance(val, Decimal):
        return val

    try:
        return Decimal(str(val))
    except (InvalidOperation, TypeError, ValueError) as err:
        raise ValidationError(f"Invalid numeric input: '{val}'") from err


def validate_number(val: Union[str, int, float, Decimal]) -> Decimal:
    """Validate and return a Decimal number."""
    return parse_number(val)


class InputValidator:
    """Class wrapper providing static validation methods for calculator inputs."""

    @staticmethod
    def parse_number(val: Union[str, int, float, Decimal]) -> Decimal:
        """Parse input value into a Decimal."""
        return parse_number(val)

    @staticmethod
    def validate_number(val: Union[str, int, float, Decimal]) -> Decimal:
        """Validate input value as a Decimal."""
        return validate_number(val)