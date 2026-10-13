import logging
import os

from app.calculator.engine import Calculator
from app.calculator_config import CalculatorConfig
from app.history import LoggingObserver, AutoSaveObserver

TWO_NUMBER_OPERATIONS = {"add", "subtract", "multiply", "divide", "modulus", "power"}

PROMPT = (
    "Enter an operation (add, subtract, multiply, divide, modulus, power, sqrt) "
    "followed by numbers: "
)

HELP_TEXT = (
    "Available commands:\n"
    "  add, subtract, multiply, divide, modulus, power <num1> <num2>\n"
    "  sqrt <num>\n"
    "  history  - show past calculations\n"
    "  undo     - undo the last calculation\n"
    "  redo     - redo the last undone calculation\n"
    "  clear    - clear the history\n"
    "  help     - show this message\n"
    "  exit     - quit"
)


def setup_logging(config: CalculatorConfig) -> None:
    os.makedirs(os.path.dirname(config.log_file) or ".", exist_ok=True)
    logging.basicConfig(
        filename=config.log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def calculator():
    config = CalculatorConfig()
    setup_logging(config)

    calc = Calculator(config)
    calc.add_observer(LoggingObserver())
    calc.add_observer(AutoSaveObserver(calc))

    print("Welcome to the calculator REPL! Type 'exit' to quit, 'help' for commands")

    while True:
        user_input = input(PROMPT).strip()
        command = user_input.lower()

        if command == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        if command == 'help':
            print(HELP_TEXT)
            continue

        if command == 'history':
            entries = calc.show_history()
            if entries:
                print("Calculation History:")
                for entry in entries:
                    print(entry)
            else:
                print("No calculations in history.")
            continue

        if command == 'undo':
            print("Operation undone" if calc.undo() else "Nothing to undo")
            continue

        if command == 'redo':
            print("Operation redone" if calc.redo() else "Nothing to redo")
            continue

        if command == 'clear':
            calc.clear_history()
            print("History cleared")
            continue

        try:
            parts = user_input.split()
            operation = parts[0].lower() if parts else ""

            if operation in TWO_NUMBER_OPERATIONS and len(parts) == 3:
                result = calc.perform_operation(operation, float(parts[1]), float(parts[2]))
            elif operation == 'sqrt' and len(parts) == 2:
                result = calc.perform_operation('sqrt', float(parts[1]))
            else:
                raise ValueError(
                    "Invalid input. Use '<operation> <num1> <num2>' "
                    "(add, subtract, multiply, divide, modulus, power) or 'sqrt <num>'."
                )

            print(f"Result: {result}")

        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")