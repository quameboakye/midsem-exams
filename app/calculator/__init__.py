"""Calculator module initialization."""

from app.calculator.engine import Calculator


def calculator():
    """Factory function to launch the interactive calculator REPL."""
    from app.calculator_repl import calculator_repl
    calculator_repl()


__all__ = ["Calculator", "calculator"]