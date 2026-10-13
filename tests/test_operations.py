import pytest
from decimal import Decimal
from typing import Any, Dict, Type

from app.exceptions import OperationError
from app.operations import (
    Operation,
    Addition,
    Subtraction,
    Multiplication,
    Division,
    Modulus,
    Sqrt,
    Power,
    OperationFactory,
)


class TestOperation:
    def test_str_representation(self):
        class TestOp(Operation):
            def execute(self, a: Decimal, b: Decimal = Decimal('0')) -> Decimal:
                return a

        assert str(TestOp()) == "TestOp"


class BaseOperationTest:
    operation_class: Type[Operation]
    valid_test_cases: Dict[str, Dict[str, Any]]
    invalid_test_cases: Dict[str, Dict[str, Any]]

    def test_valid_operations(self):
        operation = self.operation_class()
        for name, case in self.valid_test_cases.items():
            a = Decimal(str(case["a"]))
            b = Decimal(str(case.get("b", "0")))
            expected = Decimal(str(case["expected"]))
            result = operation.execute(a, b)
            assert result == expected, f"Failed case: {name}"

    def test_invalid_operations(self):
        operation = self.operation_class()
        for name, case in self.invalid_test_cases.items():
            a = Decimal(str(case["a"]))
            b = Decimal(str(case.get("b", "0")))
            error = case.get("error", OperationError)
            error_message = case.get("message", "")

            with pytest.raises(error, match=error_message):
                operation.execute(a, b)


class TestAddition(BaseOperationTest):
    operation_class = Addition
    valid_test_cases = {
        "positive_numbers": {"a": "5", "b": "3", "expected": "8.0"},
        "negative_numbers": {"a": "-5", "b": "-3", "expected": "-8.0"},
        "mixed_signs": {"a": "-5", "b": "3", "expected": "-2.0"},
        "zero_sum": {"a": "5", "b": "-5", "expected": "0.0"},
        "decimals": {"a": "5.5", "b": "3.3", "expected": "8.8"},
    }
    invalid_test_cases = {}


class TestSubtraction(BaseOperationTest):
    operation_class = Subtraction
    valid_test_cases = {
        "positive_numbers": {"a": "5", "b": "3", "expected": "2.0"},
        "negative_numbers": {"a": "-5", "b": "-3", "expected": "-2.0"},
        "mixed_signs": {"a": "-5", "b": "3", "expected": "-8.0"},
        "zero_result": {"a": "5", "b": "5", "expected": "0.0"},
        "decimals": {"a": "5.5", "b": "3.3", "expected": "2.2"},
    }
    invalid_test_cases = {}


class TestMultiplication(BaseOperationTest):
    operation_class = Multiplication
    valid_test_cases = {
        "positive_numbers": {"a": "5", "b": "3", "expected": "15.0"},
        "negative_numbers": {"a": "-5", "b": "-3", "expected": "15.0"},
        "mixed_signs": {"a": "-5", "b": "3", "expected": "-15.0"},
        "multiply_by_zero": {"a": "5", "b": "0", "expected": "0.0"},
        "decimals": {"a": "5.5", "b": "3.3", "expected": "18.15"},
    }
    invalid_test_cases = {}


class TestDivision(BaseOperationTest):
    operation_class = Division
    valid_test_cases = {
        "positive_numbers": {"a": "6", "b": "2", "expected": "3.0"},
        "negative_numbers": {"a": "-6", "b": "-2", "expected": "3.0"},
        "mixed_signs": {"a": "-6", "b": "2", "expected": "-3.0"},
        "decimals": {"a": "5.5", "b": "2", "expected": "2.75"},
        "divide_zero": {"a": "0", "b": "5", "expected": "0.0"},
    }
    invalid_test_cases = {
        "divide_by_zero": {
            "a": "5",
            "b": "0",
            "error": OperationError,
            "message": "Cannot divide by zero."
        },
    }


class TestModulus(BaseOperationTest):
    operation_class = Modulus
    valid_test_cases = {
        "standard_modulus": {"a": "10", "b": "3", "expected": "1.0"},
        "exact_division": {"a": "10", "b": "5", "expected": "0.0"},
    }
    invalid_test_cases = {
        "modulus_by_zero": {
            "a": "5",
            "b": "0",
            "error": OperationError,
            "message": "Cannot divide by zero."
        },
    }


class TestSqrt(BaseOperationTest):
    operation_class = Sqrt
    valid_test_cases = {
        "square_root": {"a": "9", "expected": "3.0"},
        "decimal_square_root": {"a": "2.25", "expected": "1.5"},
    }
    invalid_test_cases = {
        "negative_number": {
            "a": "-9",
            "error": OperationError,
            "message": "Cannot take the square root of a negative number."
        },
    }


class TestPower(BaseOperationTest):
    operation_class = Power
    valid_test_cases = {
        "positive_base_and_exponent": {"a": "2", "b": "3", "expected": "8.0"},
        "zero_exponent": {"a": "5", "b": "0", "expected": "1.0"},
        "one_exponent": {"a": "5", "b": "1", "expected": "5.0"},
        "decimal_base": {"a": "2.5", "b": "2", "expected": "6.25"},
        "zero_base": {"a": "0", "b": "5", "expected": "0.0"},
    }
    invalid_test_cases = {}


class TestOperationFactory:
    def test_create_valid_operations(self):
        operation_map = {
            'add': Addition,
            'subtract': Subtraction,
            'multiply': Multiplication,
            'divide': Division,
            'modulus': Modulus,
            'sqrt': Sqrt,
            'root': Sqrt,
            'power': Power,
        }

        for op_name, op_class in operation_map.items():
            operation = OperationFactory.create_operation(op_name)
            assert isinstance(operation, op_class)
            operation = OperationFactory.create_operation(op_name.upper())
            assert isinstance(operation, op_class)

    def test_create_invalid_operation(self):
        with pytest.raises(OperationError, match="Unknown operation: invalid_op"):
            OperationFactory.create_operation("invalid_op")