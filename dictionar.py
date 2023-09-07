# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values using keys
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 25

# Adding a new key-value pair
my_dict["occupation"] = "Engineer"
print(my_dict)  # Output: {'name': 'Alice', 
#   'age': 25, 'city': 'New York', 'occupation': 
# 'Engineer'}

# Updating values
my_dict["age"] = 26
print(my_dict)  # Output: {'name': 'Alice', 
#   'age': 26, 'city': 'New York', 'occupation':
#    'Engineer'}

# Removing a key-value pair
removed_value = my_dict.pop("city")
print(removed_value)  # Output: New York
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'occupation': 'Engineer'}

# Checking if a key exists
exists = "age" in my_dict
print(exists)  # Output: True

# Getting all keys and values
keys = my_dict.keys()
values = my_dict.values()
print(keys)  # Output: dict_keys(['name', 'age', 'occupation'])
print(values)  # Output: dict_values(['Alice', 26, 'Engineer'])

# Getting key-value pairs (items)
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 26), ('occupation', 'Engineer')])
# Looping through keys and values
for key in my_dict:
    print(key, my_dict[key])

dict_type = type(my_dict)
print(dict_type)  # Output: <class 'dict'>
# Clearing the dictionary
my_dict.clear()
print(my_dict)  # Output: {}

