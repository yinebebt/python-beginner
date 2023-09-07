# Opening a file in write mode
try:
    file = open('example.txt', 'w')
    # 2. Writing data to the file
    file.write('Hello, world!')
    file.close()
except IOError as e:
    print(f"An error occurred: {e}")

# 3. Opening a file in read mode
try:
    file = open('example.txt', 'r')
    # 4. Reading data from the file
    content = file.read()
    print(f"File content: {content}")
except FileNotFoundError:
    print("The file does not exist.")
except IOError as e:
    print(f"An error occurred: {e}")


# Using 'with' to open and automatically close a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(f"File content: {content}")
