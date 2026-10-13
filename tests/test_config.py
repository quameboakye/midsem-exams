import os
from pathlib import Path
from decimal import Decimal
import pytest

from app.calculator_config import CalculatorConfig, get_project_root
from app.exceptions import ConfigurationError


def test_get_project_root():
    root = get_project_root()
    assert isinstance(root, Path)
    assert root.exists()


def test_config_defaults(monkeypatch):
    monkeypatch.delenv("CALCULATOR_BASE_DIR", raising=False)
    monkeypatch.delenv("CALCULATOR_MAX_HISTORY_SIZE", raising=False)
    monkeypatch.delenv("CALCULATOR_AUTO_SAVE", raising=False)
    monkeypatch.delenv("CALCULATOR_PRECISION", raising=False)
    monkeypatch.delenv("CALCULATOR_MAX_INPUT_VALUE", raising=False)
    monkeypatch.delenv("CALCULATOR_DEFAULT_ENCODING", raising=False)

    config = CalculatorConfig()
    assert config.max_history_size == 1000
    assert config.auto_save is True
    assert config.precision == 10
    assert config.default_encoding == "utf-8"
    assert config.history_file.name == "calculator_history.csv"
    assert config.log_file.name == "calculator.log"


def test_config_custom_values():
    config = CalculatorConfig(
        max_history_size=500,
        auto_save=False,
        precision=5,
        max_input_value=Decimal("100"),
        default_encoding="ascii",
    )
    assert config.max_history_size == 500
    assert config.auto_save is False
    assert config.precision == 5
    assert config.max_input_value == Decimal("100")
    assert config.default_encoding == "ascii"


def test_config_log_file_property():
    config = CalculatorConfig()
    assert config.log_file.name == "calculator.log"
    assert config.log_file.parent == config.log_dir


def test_config_validation_success():
    config = CalculatorConfig()
    config.validate()


@pytest.mark.parametrize(
    "history_size, precision, max_input, error_msg",
    [
        (0, 10, Decimal("100"), "max_history_size must be positive"),
        (100, 0, Decimal("100"), "precision must be positive"),
        (100, 10, Decimal("0"), "max_input_value must be positive"),
    ],
)
def test_config_validation_failures(history_size, precision, max_input, error_msg):
    with pytest.raises(ConfigurationError, match=error_msg):
        CalculatorConfig(
            max_history_size=history_size,
            precision=precision,
            max_input_value=max_input,
        )