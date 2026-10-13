import csv
import os
from typing import List

from app.calculation import Calculation, CalculationFactory
from app.calculator_config import CalculatorConfig
from app.history import HistoryObserver


class Calculator:
    def __init__(self, config: CalculatorConfig = None) -> None:
        self.config = config or CalculatorConfig()
        self.history: List[Calculation] = []
        self.undo_stack: List[Calculation] = []
        self.redo_stack: List[Calculation] = []
        self.observers: List[HistoryObserver] = []

    def add_observer(self, observer: HistoryObserver) -> None:
        self.observers.append(observer)

    def notify_observers(self, calculation: Calculation) -> None:
        for observer in self.observers:
            observer.update(calculation)

    def perform_operation(self, operation: str, a: float, b: float = 0.0) -> float:
        calculation = CalculationFactory.create_calculation(operation, a, b)
        result = calculation.execute()
        self.history.append(calculation)
        self.redo_stack.clear()
        self.notify_observers(calculation)
        return result

    def show_history(self) -> List[str]:
        return [f"{i}. {calc}" for i, calc in enumerate(self.history, start=1)]

    def clear_history(self) -> None:
        self.history.clear()
        self.undo_stack.clear()
        self.redo_stack.clear()

    def undo(self) -> bool:
        if not self.history:
            return False
        self.redo_stack.append(self.history.pop())
        return True

    def redo(self) -> bool:
        if not self.redo_stack:
            return False
        self.history.append(self.redo_stack.pop())
        return True

    def save_history(self) -> None:
        os.makedirs(os.path.dirname(self.config.history_file) or ".", exist_ok=True)
        with open(self.config.history_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["operation", "operand1", "operand2", "result"])
            for calc in self.history:
                writer.writerow([calc.operation, calc.operand1, calc.operand2, calc.result])