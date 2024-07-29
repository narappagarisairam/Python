# Set Creation
my_set = {1, 2, 3, 4, 5}

# Set Methods

# Adding and Removing Elements
my_set.add(6)                 # Adds an element to the set
print(my_set)                 # Output: {1, 2, 3, 4, 5, 6}

my_set.remove(3)              # Removes the specified element from the set
print(my_set)                 # Output: {1, 2, 4, 5, 6}

my_set.discard(2)             # Removes the specified element from the set, does not raise an error if the element is not found
print(my_set)                 # Output: {1, 4, 5, 6}

my_set.pop()                  # Removes and returns an arbitrary element from the set
print(my_set)                 # Output: {4, 5, 6} (element removed may vary)

my_set.clear()                # Removes all elements from the set
print(my_set)                 # Output: set()

# Other Methods
my_set = {1, 2, 3, 4, 5}
another_set = {4, 5, 6, 7, 8}

union_set = my_set.union(another_set)  # Returns a new set with elements from both sets
print(union_set)             # Output: {1, 2, 3, 4, 5, 6, 7, 8}

intersection_set = my_set.intersection(another_set)  # Returns a new set with elements common to both sets
print(intersection_set)      # Output: {4, 5}

difference_set = my_set.difference(another_set)  # Returns a new set with elements in the first set but not in the second set
print(difference_set)        # Output: {1, 2, 3}

symmetric_difference_set = my_set.symmetric_difference(another_set)  # Returns a new set with elements in either set but not both
print(symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}

my_set.update(another_set)  # Updates the set with elements from another set
print(my_set)                 # Output: {1, 2, 3, 4, 5, 6, 7, 8}

my_set.intersection_update({4, 5, 9})  # Updates the set with the intersection of itself and another
print(my_set)                 # Output: {4, 5}

my_set.difference_update({5, 6})  # Updates the set with the difference of itself and another
print(my_set)                 # Output: {4}

my_set.symmetric_difference_update({3, 4, 7})  # Updates the set with the symmetric difference of itself and another
print(my_set)                 # Output: {3, 7}

is_subset = my_set.issubset({3, 4, 7, 8})  # Returns True if the set is a subset of another set
print(is_subset)             # Output: True

is_superset = my_set.issuperset({3})  # Returns True if the set is a superset of another set
print(is_superset)           # Output: True

is_disjoint = my_set.isdisjoint({1, 2})  # Returns True if the set has no elements in common with another set
print(is_disjoint)           # Output: True

