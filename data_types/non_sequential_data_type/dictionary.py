# Dictionary Creation
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Dictionary Methods

# Accessing and Modifying Elements
print(my_dict['name'])         # Output: John
my_dict['age'] = 31            # Modify existing value
my_dict['country'] = 'USA'     # Add new key-value pair
print(my_dict)                 # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}

# Removing Elements
my_dict.pop('age')             # Removes and returns the value for the specified key
print(my_dict)                 # Output: {'name': 'John', 'city': 'New York', 'country': 'USA'}

my_dict.popitem()              # Removes and returns the last key-value pair
print(my_dict)                 # Output: {'name': 'John', 'city': 'New York'}

del my_dict['city']            # Removes the specified key-value pair
print(my_dict)                 # Output: {'name': 'John'}

my_dict.clear()                # Removes all items from the dictionary
print(my_dict)                 # Output: {}

# Other Methods
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
keys = my_dict.keys()          # Returns a view object of all keys
print(keys)                    # Output: dict_keys(['name', 'age', 'city'])

values = my_dict.values()      # Returns a view object of all values
print(values)                  # Output: dict_values(['John', 30, 'New York'])

items = my_dict.items()        # Returns a view object of all key-value pairs
print(items)                   # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

copy_dict = my_dict.copy()     # Returns a shallow copy of the dictionary
print(copy_dict)               # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

default_value = my_dict.get('country', 'Unknown')  # Returns the value for the specified key, or a default value if the key is not found
print(default_value)           # Output: Unknown

my_dict.update({'country': 'USA', 'city': 'San Francisco'})  # Updates the dictionary with key-value pairs from another dictionary
print(my_dict)                 # Output: {'name': 'John', 'age': 30, 'city': 'San Francisco', 'country': 'USA'}

default_set = my_dict.setdefault('language', 'English')  # Sets a default value for a key if it is not already in the dictionary
print(my_dict)                 # Output: {'name': 'John', 'age': 30, 'city': 'San Francisco', 'country': 'USA', 'language': 'English'}

