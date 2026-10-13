from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CalculatorConfig:
    auto_save: bool = True
    history_file: str = "history/calculator_history.csv"
    log_file: str = "logs/calculator.log"
    max_input_value: Decimal = Decimal("1e999")
