class CalculatorError(Exception):
    """Base exception class for calculator errors."""
    pass


class OperationError(CalculatorError):
    """Raised when an error occurs during operation execution."""
    pass


class ValidationError(CalculatorError):
    """Raised when input validation fails."""
    pass


class HistoryError(CalculatorError):
    """Raised when an error occurs in history operations."""
    pass


class ConfigurationError(CalculatorError):
    """Raised when configuration validation fails."""
    pass