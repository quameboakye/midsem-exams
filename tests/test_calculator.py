import pytest
from app.calculator import calculator


def run_calculator(monkeypatch, capsys, commands):
    """Feed commands to the REPL one at a time and return everything it printed."""
    inputs = iter(commands)
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(inputs))
    calculator()
    return capsys.readouterr().out


@pytest.mark.parametrize(
    "command, expected",
    [
        ("add 2 3", "Result: 5.0"),
        ("subtract 5 3", "Result: 2.0"),
        ("multiply 4 3", "Result: 12.0"),
        ("divide 10 4", "Result: 2.5"),
        ("modulus 10 3", "Result: 1.0"),
        ("sqrt 9", "Result: 3.0"),
    ],
)
def test_operations(monkeypatch, capsys, command, expected):
    out = run_calculator(monkeypatch, capsys, [command, "exit"])
    assert expected in out


def test_welcome_and_exit(monkeypatch, capsys):
    out = run_calculator(monkeypatch, capsys, ["exit"])
    assert "Welcome to the calculator REPL!" in out
    assert "Goodbye!" in out


def test_divide_by_zero(monkeypatch, capsys):
    out = run_calculator(monkeypatch, capsys, ["divide 5 0", "exit"])
    assert "Error: Cannot divide by zero." in out


def test_modulus_by_zero(monkeypatch, capsys):
    out = run_calculator(monkeypatch, capsys, ["modulus 5 0", "exit"])
    assert "Error: Cannot divide by zero." in out


def test_sqrt_negative(monkeypatch, capsys):
    out = run_calculator(monkeypatch, capsys, ["sqrt -4", "exit"])
    assert "Error: Cannot take the square root of a negative number." in out


def test_non_numeric_input(monkeypatch, capsys):
    out = run_calculator(monkeypatch, capsys, ["add two 3", "exit"])
    assert "Error:" in out


def test_unknown_operation(monkeypatch, capsys):
    out = run_calculator(monkeypatch, capsys, ["power 2 3", "exit"])
    assert "Error: Invalid input" in out


def test_wrong_number_of_arguments(monkeypatch, capsys):
    out = run_calculator(monkeypatch, capsys, ["add 2", "sqrt 4 5", "exit"])
    assert out.count("Error: Invalid input") == 2


def test_empty_input(monkeypatch, capsys):
    out = run_calculator(monkeypatch, capsys, ["", "exit"])
    assert "Error: Invalid input" in out
