# Import the math_operations module
import src.math_operations as math_operations
import src.math_operations as math
a= input
# Use functions from the module
result1 = math_operations.add(5, 3)
result2 = math_operations.subtract(10, 4)
result3 = math.multiply(2, 6)
result4 = math.divide(8, 2)

# Access the module variable
pi = math_operations.pi

# Print the results and module variable
print("Addition:", result1) #8
print("Subtraction:", result2)
print("Multiplication:", result3)
print("Division:", result4)
print("Module Variable:", pi)
