import math
from abc import ABC, abstractmethod
from decimal import Decimal
from app.exceptions import OperationError


class Operations:
    @staticmethod
    def addition(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @staticmethod
    def modulus(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a % b

    @staticmethod
    def sqrt(a: float) -> float:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)

    @staticmethod
    def power(a: float, b: float) -> float:
        return a ** b


class Operation(ABC):
    @abstractmethod
    def execute(self, a: Decimal, b: Decimal = Decimal('0')) -> Decimal:
        pass  # pragma: no cover

    def __str__(self) -> str:
        return self.__class__.__name__


class Addition(Operation):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return Decimal(str(Operations.addition(float(a), float(b))))


class Subtraction(Operation):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return Decimal(str(Operations.subtraction(float(a), float(b))))


class Multiplication(Operation):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return Decimal(str(Operations.multiplication(float(a), float(b))))


class Division(Operation):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        try:
            return Decimal(str(Operations.division(float(a), float(b))))
        except ValueError as e:
            raise OperationError(str(e))


class Modulus(Operation):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        try:
            return Decimal(str(Operations.modulus(float(a), float(b))))
        except ValueError as e:
            raise OperationError(str(e))


class Sqrt(Operation):
    def execute(self, a: Decimal, b: Decimal = Decimal('0')) -> Decimal:
        try:
            return Decimal(str(Operations.sqrt(float(a))))
        except ValueError as e:
            raise OperationError(str(e))


class Root(Sqrt):
    pass


class Power(Operation):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return Decimal(str(Operations.power(float(a), float(b))))


class OperationFactory:
    _operations = {
        'add': Addition(),
        'subtract': Subtraction(),
        'multiply': Multiplication(),
        'divide': Division(),
        'modulus': Modulus(),
        'sqrt': Sqrt(),
        'root': Root(),
        'power': Power()
    }

    @classmethod
    def create_operation(cls, operation_name: str) -> Operation:
        op = cls._operations.get(operation_name.lower())
        if not op:
            raise OperationError(f"Unknown operation: {operation_name}")
        return op