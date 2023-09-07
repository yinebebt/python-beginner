# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

# Slicing a tuple
slice_tuple = my_tuple[1:4]
print(slice_tuple)  # Output: (2, 3, 4)

# Length of a tuple
length = len(my_tuple)
print(length)  # Output: 5

# Concatenating tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4)

# Multiplying a tuple
multiplied_tuple = my_tuple * 2
print(multiplied_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Checking if an element exists in a tuple
exists = 3 in my_tuple
print(exists)  # Output: True

# Finding the index of an element in a tuple
index = my_tuple.index(4)
print(index)  # Output: 3

# Counting occurrences of an element in a tuple
count = my_tuple.count(2)
print(count)  # Output: 1

# Nested tuples
nested_tuple = ((1, 2), (3, 4))
print(nested_tuple[0][1])  # Output: 2

# Unpacking tuples
x, y, z = my_tuple
print(x, y, z)  # Output: 1 2 3

my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

