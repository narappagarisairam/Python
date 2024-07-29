#Membership operators in Python are used to test whether a value or variable is found in a sequence (such as a string, list, tuple, or set). Python provides two membership operators: in and not in.
#it is returns true or false
# in operator
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False
#example with string
my_string = "hello world"
print('h' in my_string)  # Output: True
print('z' in my_string)  # Output: False

#not in operator
my_list = [1, 2, 3, 4, 5]
print(3 not in my_list)  # Output: False
print(6 not in my_list)  # Output: True
#example with not in operator
my_string = "hello world"
print('h' not in my_string)  # Output: False
print('z' not in my_string)  # Output: True

