# Function that raises an exception
def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid data type"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    finally:
        print("Operation completed.")

# Example usage
try:
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))

    result = divide(num1, num2)
    print(f"Result of division: {result}")
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
except KeyboardInterrupt:
    print("Operation aborted by user.")
