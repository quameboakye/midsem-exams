from dataclasses import dataclass


@dataclass
class CalculatorConfig:
    auto_save: bool = True
    history_file: str = "history/calculator_history.csv"
    log_file: str = "logs/calculator.log"