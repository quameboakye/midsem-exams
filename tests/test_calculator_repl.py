import pytest

from app.calculator import calculator


@pytest.fixture
def run_repl(monkeypatch, capsys, tmp_path):
    monkeypatch.chdir(tmp_path)

    def _run(inputs):
        iterator = iter(inputs)
        monkeypatch.setattr("builtins.input", lambda _: next(iterator))
        calculator()
        return capsys.readouterr().out

    return _run


def test_add_and_exit(run_repl):
    output = run_repl(["add 1 1", "exit"])
    assert "Result: 2.0" in output
    assert "Goodbye" in output


def test_sqrt(run_repl):
    assert "Result: 3.0" in run_repl(["sqrt 9", "exit"])


def test_help(run_repl):
    assert "Available commands" in run_repl(["help", "exit"])


def test_history_shows_calculations(run_repl):
    output = run_repl(["add 1 1", "history", "exit"])
    assert "Calculation History:" in output
    assert "1. " in output


def test_history_empty(run_repl):
    assert "No calculations in history." in run_repl(["history", "exit"])


def test_undo_and_redo(run_repl):
    output = run_repl(["add 1 1", "undo", "redo", "exit"])
    assert "Operation undone" in output
    assert "Operation redone" in output


def test_nothing_to_undo_or_redo(run_repl):
    output = run_repl(["undo", "redo", "exit"])
    assert "Nothing to undo" in output
    assert "Nothing to redo" in output


def test_clear(run_repl):
    assert "History cleared" in run_repl(["clear", "exit"])


def test_invalid_input(run_repl):
    assert "Error: Invalid input" in run_repl(["", "exit"])


def test_non_numeric_input(run_repl):
    assert "Error:" in run_repl(["add a b", "exit"])


def test_divide_by_zero(run_repl):
    assert "Error:" in run_repl(["divide 1 0", "exit"])
