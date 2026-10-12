from app.operations import Operations

# Maps each two-number command to the Operations method that handles it.
TWO_NUMBER_OPERATIONS = {
    "add": Operations.addition,
    "subtract": Operations.subtraction,
    "multiply": Operations.multiplication,
    "divide": Operations.division,
    "modulus": Operations.modulus,
    "power": Operations.power,
}

def calculator():

    print("Welcome to the calculator REPL! Type 'exit' to quit")

    while True:

        user_input = input(
            "Enter an operation (add, subtract, multiply, divide, modulus, power, sqrt) "
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
                result = Operations.sqrt(float(parts[1]))

            else:
                raise ValueError(
                    "Invalid input. Use '<operation> <num1> <num2>' "
                    "(add, subtract, multiply, divide, modulus, power) or 'sqrt <num>'."
                )

            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")