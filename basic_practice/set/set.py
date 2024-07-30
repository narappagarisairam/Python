#set{}
'''A set is an unordered collection of unique elements. 
It does not allow duplicate elements and does not maintain any particular order. 
Sets are mutable, meaning you can add or remove elements after the set is created.'''

my_set = {1, 2, 3, 4, 5}
print(my_set)
#set() Constructor:
my_set = set([1, 2, 3, 4, 5])
print(my_set)
#emptyset
empty_set = set()

#Adding and Removing
my_set.add(6)  # my_set is now {1, 2, 3, 4, 5, 6}
print(my_set)
#set.remove(elem)
my_set.remove(3)  # my_set is now {1, 2, 4, 5, 6}
print(my_set)
#set.discard(elem)
my_set.discard(7)  # my_set remains {1, 2, 4, 5, 6}
print(my_set)
#set.pop()
element = my_set.pop()  # Removes and returns an arbitrary element
#to remove all the elements in set
#set.clear(element)
print(element)
#set.copy(): Returns a shallow copy of the set.
copy_set = my_set.copy()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
