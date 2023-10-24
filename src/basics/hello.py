# Printing to screen
print("hello, world!")

# Accepting user input
name = input("Enter your name: ")
age = input("Enter your age: ")

# Concatenating strings
print("Welcome " + name + ", You are now " + age + "!")

# This is a single line comment

'''
This is 
multiple line comment
'''

# Basic arithmetic operations
num1 = 45  # Semicolon is optional
num2 = 55

sum = num1 + num2
avg = sum / 2

# Explicit type conversion
print("The sum of " + str(num1) + " and " + str(num2) + " is " +
       str(sum) + ", and their average is " + str(avg))

# Implicit type conversion using f-strings
print(f"The sum of {num1} and {num2} is {sum}, and their average is {avg}")

# Multiple value assignment
a = b = c = 45
f, g, h = 60, 45.89, "hey"

print("a, b, c =", a, b, c)
print("f, g, h =", f, g, h)

del a
del f, g
# print("a, f, g =", a, f, g)  # NameError: a is not defined

# Working with strings
strng = "hello world "

# Accessing string elements
print(strng[0])  # Output: h
print(strng[1:4])  # Output: ell
print(strng[1:])  # Output: ello world

# Repeating a string
new_str = strng * 2
print("new string =", new_str)  # Output: new string = hello worldhello world
