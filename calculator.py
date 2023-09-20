def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def calculator():
    while True:
        try:
            print("Options:")
            print("Enter '+' for addition")
            print("Enter '-' for subtraction")
            print("Enter '*' for multiplication")
            print("Enter '/' for division")
            print("Enter 'q' to end the program")

            choice = input(": ").lower()
            if choice == "q":
                break

            if choice not in ("+", "-", "*", "/"):
                raise ValueError("Invalid input")

            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if choice == "+":
                result = add(x, y)
                print("Result:", result)
            elif choice == "-":
                result = subtract(x, y)
                print("Result:", result)
            elif choice == "*":
                result = multiply(x, y)
                print("Result:", result)
            elif choice == "/":
                result = divide(x, y)
                print("Result:", result)

        except ValueError as e:
            print("Error:", e)
        except ZeroDivisionError as e:
            print("Error:", e)


if __name__ == "__main__":
    calculator()
