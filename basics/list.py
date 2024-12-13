# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements in a list
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3

# Slicing a list
slice_list = my_list[1:4]
print(slice_list)  # Output: [2, 3, 4]

# Appending elements to a list
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Inserting elements at a specific index
my_list.insert(2, 7)
print(my_list)  # Output: [1, 2, 7, 3, 4, 5, 6]

# Removing elements from a list
my_list.remove(3)  # Removes the first occurrence of 3
print(my_list)  # Output: [1, 2, 7, 4, 5, 6]

# Popping elements from a list
popped_element = my_list.pop()  # Removes and returns the last element
print(popped_element)  # Output: 6
print(my_list)  # Output: [1, 2, 7, 4, 5]

# Finding the index of an element
index = my_list.index(7)
print(index)  # Output: 2

# Counting occurrences of an element
count = my_list.count(4)
print(count)  # Output: 1

# Sorting a list
my_list.sort(reverse=True)
print(my_list)  # Output: [1, 2, 4, 5, 7]

# Reversing a list
my_list.reverse()
print(my_list)  # Output: [7, 5, 4, 2, 1]

#convert tuple into list
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3, 4, 5]

