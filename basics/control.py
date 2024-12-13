# If-else control statement
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# For loop
for i in range(5):
    print("Iteration:", i)

# While loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# Nested loop
for i in range(3):
    for j in range(2):
        print(i, j)

# Break and continue statements
for num in range(100):
    if num == 5:
        break
    if num % 2 == 0:
        continue
    print(num)

# loop through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# loop through dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)