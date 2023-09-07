# Functions
def greet(name):
    print("Hello,", name)

greet("Alice")
greet("Bob")

# Returning a value from a function
def add(x, y):
    return x + y

result = add(5, 3)
print("Result:", result)


# Function with a required argument
def greetUser(name,age):
    return f"Hello, {name} you are now {age}!"

print(greetUser("Alice",40))  #required args, in positioned order
print(greetUser(age=40, name="Alice")) #keyword args

# Function with a default argument
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Bob")) 
print(greet_with_title("Bob", "Dr.")) 

# Function with variable-length arguments
def sum_values(*args):
    total = 0
    for num in args:
        total += num
        return total

print(sum_values(1, 2, 3, 4, 5))

