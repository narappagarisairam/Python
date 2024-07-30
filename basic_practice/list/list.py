#list
'''Ordered: The items in a list have a defined order.
   Mutable: You can change the items in a list after it has been created.
Heterogeneous: A list can contain items of different data types.'''
'''
Basic List Operations
Creating a list: my_list = [1, 2, 3]
Accessing elements: my_list[0] (returns the first element)
Modifying elements: my_list[0] = 10 (changes the first element to 10)
Appending elements: my_list.append(4) (adds 4 to the end of the list)
Removing elements: my_list.remove(2) (removes the first occurrence of 2)'''

int_list = [1, 2, 3, 4, 5]
print(int_list)  # Output: [1, 2, 3, 4, 5]

string_list = ["apple", "banana", "cherry"]
print(string_list)  # Output: ['apple', 'banana', 'cherry']

mixed_list = [1, "apple", 3.14, True]
print(mixed_list)  # Output: [1, 'apple', 3.14, True]

nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(nested_list)  # Output: [[1, 2, 3], ['a', 'b', 'c'], [True, False]]

empty_list = []
print(empty_list)  # Output: []

# length
len(int_list)  # Output: 5

#append
int_list.append(6)
print(int_list)  # Output: [1, 2, 3, 4, 5, 6]

#insert
int_list.insert(1, 1.5)
print(int_list)  # Output: [1, 1.5, 2, 3, 4, 5, 6]

#remove
int_list.remove(1.5)
print(int_list)  # Output: [1, 2, 3, 4, 5, 6]

#pop
int_list.pop()  # Output: 6
print(int_list)  # Output: [1, 2, 3, 4, 5]

#slice
sliced_list = int_list[1:4]
print(sliced_list)  # Output: [2, 3, 4]

#count
count = int_list.count(2)
print(count)  # Output: 1

#index method
index = int_list.index(3)
print(index)  # Output: 2

#reverse method
int_list.reverse()
print(int_list)  # Output: [5, 4, 3, 2, 10]

#sort method
int_list.sort()
print(int_list)  # Output: [2, 3, 4, 5, 10]

# clear method
int_list.clear()
print(int_list)  # Output: []

