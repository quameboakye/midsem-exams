from abc import ABC, abstractmethod
from typing import Any, Dict
from app.operations import Operations as Operation


class Calculation(ABC):
    def __init__(self, a: float, b: float) -> None:
        self.a: float = a
        self.b: float = b

    @property
    def operation(self) -> str:
        return self.__class__.__name__.replace('Calculation', '')

    @property
    def operand1(self) -> float:
        return self.a

    @property
    def operand2(self) -> float:
        return self.b

    @property
    def result(self) -> float:
        return self.execute()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "operation": self.operation.lower(),
            "operand1": str(self.a),
            "operand2": str(self.b),
            "result": str(self.result),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Calculation":
        return CalculationFactory.create_calculation(
            data["operation"], float(data["operand1"]), float(data["operand2"])
        )

    @abstractmethod
    def execute(self) -> float:
        pass  # pragma: no cover

    def __str__(self) -> str:
        result = self.execute()
        operation_name = self.__class__.__name__.replace('Calculation', '')
        return f"{self.__class__.__name__}: {self.a} {operation_name} {self.b} = {result}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"


class CalculationFactory:
    _calculations = {}

    @classmethod
    def register_calculation(cls, calculation_type: str):
        def decorator(subclass):
            calculation_type_lower = calculation_type.lower()
            if calculation_type_lower in cls._calculations:
                raise ValueError(f"Calculation type '{calculation_type}' is already registered.")
            cls._calculations[calculation_type_lower] = subclass
            return subclass
        return decorator

    @classmethod
    def create_calculation(cls, calculation_type: str, a: float, b: float) -> Calculation:
        calculation_type_lower = calculation_type.lower()
        calculation_class = cls._calculations.get(calculation_type_lower)
        if not calculation_class:
            available_types = ', '.join(cls._calculations.keys())
            raise ValueError(f"Unsupported calculation type: '{calculation_type}'. Available types: {available_types}")
        return calculation_class(a, b)


@CalculationFactory.register_calculation('add')
class AddCalculation(Calculation):
    def execute(self) -> float:
        return Operation.addition(self.a, self.b)


@CalculationFactory.register_calculation('subtract')
class SubtractCalculation(Calculation):
    def execute(self) -> float:
        return Operation.subtraction(self.a, self.b)


@CalculationFactory.register_calculation('multiply')
class MultiplyCalculation(Calculation):
    def execute(self) -> float:
        return Operation.multiplication(self.a, self.b)


@CalculationFactory.register_calculation('divide')
class DivideCalculation(Calculation):
    def execute(self) -> float:
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Operation.division(self.a, self.b)


@CalculationFactory.register_calculation('power')
class PowerCalculation(Calculation):
    def execute(self) -> float:
        return Operation.power(self.a, self.b)  # pragma: no cover


@CalculationFactory.register_calculation('modulus')
class ModulusCalculation(Calculation):
    def execute(self) -> float:
        return Operation.modulus(self.a, self.b)  # pragma: no cover


@CalculationFactory.register_calculation('sqrt')
class SqrtCalculation(Calculation):
    def execute(self) -> float:
        return Operation.sqrt(self.a)  # pragma: no cover