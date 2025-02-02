#dicionary
''' A dictionary in Python is an unordered, mutable, and indexed collection of items. Each item in a dictionary is a pair consisting of a key and a value.

Keys: Must be immutable types (e.g., strings, numbers, tuples). They must be unique within the dictionary.
Values: Can be of any type and can be duplicated.'''

#dictionary using curly braces {} or the dict() constructor.
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

#using constructor
my_dict = dict(name='Alice', age=30, city='New York')

#accessing
print(my_dict['name'])  # Output: Alice

#adding or updating
my_dict['email'] = 'alice@example.com'  # Adds a new item
my_dict['age'] = 31  # Updates an existing item
print(my_dict)
#removing
del my_dict['city']  # Removes 'city' from the dictionary
print(my_dict)
email = my_dict.pop('email')  # Removes 'email' and returns its value
print(my_dict)
# methods 
#dict.copy()
new_dict = my_dict.copy()
print(new_dict)
#dict.fromkeys(seq, value)
new_dict = dict.fromkeys(['a', 'b'], 0)  # {'a': 0, 'b': 0}
print(new_dict)
#dict.get(key, default)
age = my_dict.get('age', 'Not found')  # Returns the value for 'age' or 'Not found'
print(new_dict)
#dict.items()
items = my_dict.items()  # dict_items([('name', 'Alice'), ('age', 31)])
print(items)
#dict.keys()
keys = my_dict.keys()  # dict_keys(['name', 'age'])
print(keys)
#dict.values()
values = my_dict.values()  # dict_values(['Alice', 31])
print(values)
#dict.clear()
my_dict.clear()
