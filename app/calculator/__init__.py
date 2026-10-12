from app.operations import (
    addition,
    subtraction,
    multiplication,
    division,
    modulus,
    sqrt,
)

TWO_NUMBER_OPERATIONS = {
    'add': addition,
    'subtract': subtraction,
    'multiply': multiplication,
    'divide': division,
    'modulus': modulus,
}


def calculator():

    print("Welcome to the calculator REPL! Type 'exit' to quit")

    while True:

        user_input = input(
            "Enter an operation (add, subtract, multiply, divide, modulus, sqrt) "
            "followed by numbers: "
        )

        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        try:

            parts = user_input.split()
            operation = parts[0] if parts else ""

            if operation in TWO_NUMBER_OPERATIONS and len(parts) == 3:
                result = TWO_NUMBER_OPERATIONS[operation](float(parts[1]), float(parts[2]))

            elif operation == 'sqrt' and len(parts) == 2:
                result = sqrt(float(parts[1]))

            else:
                raise ValueError(
                    "Invalid input. Use '<operation> <num1> <num2>' "
                    "(add, subtract, multiply, divide, modulus) or 'sqrt <num>'."
                )

            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")
