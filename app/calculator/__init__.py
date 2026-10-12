from app.operations import addition, subtraction, multiplication, division


def calculator():

    print("Welcome to the calculator REPL! Type 'exit' to quit")


    while True:

        user_input = input("Enter an operation (add, subtract, multiply, divide) followed by two numbers: ")

        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        try:

            parts = user_input.split()

            if len(parts) != 3:
                
                raise ValueError("Invalid input format. Please provide an operation and two numbers.")

            operation, num1_str, num2_str = parts
            num1 = float(num1_str)
            num2 = float(num2_str)

            if operation == 'add':
                result = addition(num1, num2)
            elif operation == 'subtract':
                result = subtraction(num1, num2)
            elif operation == 'multiply':
                result = multiplication(num1, num2)
            elif operation == 'divide':
                result = division(num1, num2)
            else:
                raise ValueError("Unknown operation. Please use add, subtract, multiply, or divide.")

            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")