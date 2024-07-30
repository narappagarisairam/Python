# tuple denoted ()
'''Ordered: Elements in a tuple have a defined order.
Immutable: Elements in a tuple cannot be changed after the tuple is created.
Heterogeneous: A tuple can contain elements of different data types.'''

# Creating an empty tuple
empty_tuple = ()

# Creating a tuple with elements
tuple1 = (1, 2, 3)
tuple2 = ("sai", "ram", "raj")
tuple3 = (1, "win", 3.14)
print(tuple1)
print(tuple2)
print(tuple3)
# Creating a tuple without parentheses (tuple packing)
tuple4 = 1, 2, 3
print(tuple4)
# Creating a tuple with a single element (note the comma)
single_element_tuple = (1,)
print(single_element_tuple)
# Creating an empty tuple
empty_tuple = ()

# Creating a tuple with elements
tuple1 = (1, 2, 3)
tuple2 = ("sairam", "sunny", "murali")
tuple3 = (1, "siva", 3.14)

# Creating a tuple without parentheses (tuple packing)
tuple4 = 1, 2, 3

# Creating a tuple with a single element (note the comma)
single_element_tuple = (1,)

#concatination
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

#repitation
tuple1 = (1, 2, 3)
repeated_tuple = tuple1 * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)

#slicing
tuple1 = (1, 2, 3, 4, 5)
sliced_tuple = tuple1[1:4]
print(sliced_tuple)  # Output: (2, 3, 4)

#unpacking
tuple1 = (1, 2, 3)
a, b, c = tuple1
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

#nested tuple
nested_tuple = (1, (2, 3), 4)
print(nested_tuple[1])  # Output: (2, 3)
print(nested_tuple[1][1])  # Output: 3


#operations of tuple
#count
tuple1 = (1, 2, 3, 2, 2)
count_of_twos = tuple1.count(2)
print(count_of_twos)  # Output: 3

#index
tuple1 = (1, 2, 3, 2, 2)
index_of_two = tuple1.index(2)
print(index_of_two)  # Output: 1

