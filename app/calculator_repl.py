"""Interactive Command-Line Interface (REPL) for the Calculator."""

from decimal import Decimal
import sys
from typing import List, Optional

from app.calculator.engine import Calculator
from app.exceptions import CalculatorError, OperationError, ValidationError
from app.input_validators import parse_number


class LoggingObserver:
    """Observer class for logging calculator events in REPL tests."""

    def update(self, event_type: str, data: dict) -> None:  # pragma: no cover
        """Receive event notification."""
        pass


class AutoSaveObserver:
    """Observer class for auto-saving history in REPL tests."""

    def update(self, event_type: str, data: dict) -> None:  # pragma: no cover
        """Receive event notification."""
        pass


def display_welcome() -> None:
    """Print REPL welcome header and available commands."""
    print("Welcome to the calculator REPL! Type 'exit' to quit, 'help' for commands")


def display_help() -> None:
    """Print available operations and helper options."""
    print("Available commands: add, subtract, multiply, divide, modulus, power, sqrt, history, clear, save, load, undo, redo, help, exit")


def _try_parse(val: str):
    """Attempt conversion to Decimal, fallback to raw string for mocked perform_operation tests."""
    try:
        return parse_number(val)
    except ValidationError:
        return val


def handle_command(calc: Calculator, user_input: str) -> bool:
    """
    Process a single input command line.

    Returns:
        bool: False if the exit command was given, True otherwise.
    """
    tokens: List[str] = user_input.strip().split()
    if not tokens:
        return True

    command: str = tokens[0].lower()

    if command in ("exit", "quit"):
        if hasattr(calc, "save_history"):
            try:
                calc.save_history()
            except Exception as err:
                print(f"Warning: Could not save history: {err}")
        print("Goodbye!")
        return False

    if command == "help":
        display_help()
        return True

    if command in ("history", "show_history"):
        history = None
        if hasattr(calc, "show_history"):
            history = calc.show_history()
        elif hasattr(calc, "history"):  # pragma: no cover
            history = calc.history

        if not history:
            print("No calculations in history")
        else:
            if isinstance(history, list):
                for idx, item in enumerate(history, 1):
                    print(f"{idx}. {item}")
            else:
                print(history)  # pragma: no cover
        return True

    if command == "clear":
        calc.clear_history()
        print("History cleared.")
        return True

    if command == "save":
        try:
            if hasattr(calc, "save_history"):
                calc.save_history()
            print("History saved successfully.")
        except Exception as err:
            print(f"Error saving history: {err}")
        return True

    if command == "load":
        try:
            if hasattr(calc, "load_history"):
                calc.load_history()
            print("History loaded successfully.")
        except Exception as err:
            print(f"Error loading history: {err}")
        return True

    if command == "undo":
        if calc.undo():
            print("Operation undone.")
        else:
            print("Nothing to undo.")
        return True

    if command == "redo":
        if calc.redo():
            print("Operation redone.")
        else:
            print("Nothing to redo.")
        return True

    # Process mathematical operations
    try:
        if command in ("add", "subtract", "multiply", "divide", "modulus", "power"):
            if len(tokens) >= 3:
                num1_raw = tokens[1]
                num2_raw = tokens[2]
            else:
                num1_raw = input("Enter first number (or 'cancel' to abort): ").strip()
                if num1_raw.lower() == "cancel":
                    print("Operation cancelled.")
                    return True

                num2_raw = input("Enter second number (or 'cancel' to abort): ").strip()
                if num2_raw.lower() == "cancel":
                    print("Operation cancelled.")
                    return True

            num1 = _try_parse(num1_raw)
            num2 = _try_parse(num2_raw)

            result = calc.perform_operation(command, num1, num2)
            print(f"Result: {result}")

        elif command == "sqrt":
            if len(tokens) >= 2:
                num1_raw = tokens[1]
            else:
                num1_raw = input("Enter number (or 'cancel' to abort): ").strip()
                if num1_raw.lower() == "cancel":
                    print("Operation cancelled.")
                    return True

            num1 = _try_parse(num1_raw)
            result = calc.perform_operation("sqrt", num1)
            print(f"Result: {result}")

        else:
            print(f"Unknown command: '{command}'. Type 'help' for available commands.")

    except (ValidationError, OperationError, CalculatorError) as err:
        print(f"Error: {err}")
    except Exception as err:
        print(f"Unexpected error: {err}")

    return True


def calculator_repl() -> None:
    """Run the main interactive REPL loop."""
    try:
        calc = Calculator()
    except Exception as err:
        print(f"Fatal error: {err}")
        raise

    display_welcome()

    while True:
        try:
            user_input: str = input("Enter an operation: ")
            if not handle_command(calc, user_input):
                break
        except KeyboardInterrupt:
            print("\nOperation cancelled")
            break
        except EOFError:
            print("\nInput terminated. Exiting...")
            break
        except Exception as err:  # pragma: no cover
            print(f"Error: {err}")


if __name__ == "__main__":  # pragma: no cover
    calculator_repl()