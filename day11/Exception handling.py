# Day 11: Exception Handling
# Project: Error-proof Calculator

def calculator():
    print("Error-Proof Calculator")
    print("Available operations: +, -, *, /")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Handle division by zero
            if num2 == 0:
                raise ZeroDivisionError("You cannot divide by zero!")
            result = num1 / num2
        else:
            raise ValueError("Invalid operator! Please choose +, -, *, /")

        print(f"Result: {result}")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Math Error: {zde}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    finally:
        print("Thank you for using the calculator!")

# Run program
calculator()
