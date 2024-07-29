# String Creation
my_string = "Hello, World!"

# String Methods
my_string.capitalize()    # Converts the first character to uppercase
my_string.lower()         # Converts all characters to lowercase
my_string.upper()         # Converts all characters to uppercase
my_string.title()         # Converts the first character of each word to uppercase
my_string.strip()         # Removes any leading and trailing characters (spaces by default)
my_string.replace('o', '0')  # Replaces all occurrences of a substring with another substring
my_string.split(',')      # Splits the string at the specified separator and returns a list
my_string.join(['Hello', 'World'])  # Concatenates the elements of an iterable to the end of the string
my_string.find('World')   # Finds the first occurrence of the specified substring
my_string.index('World')  # Finds the first occurrence of the specified substring and raises ValueError if not found
my_string.count('l')      # Counts the number of occurrences of a substring in the string
my_string.startswith('He')  # Returns True if the string starts with the specified substring
my_string.endswith('!')   # Returns True if the string ends with the specified substring
my_string.isalpha()       # Returns True if all characters in the string are alphabetic
my_string.isdigit()       # Returns True if all characters in the string are digits
my_string.isalnum()       # Returns True if all characters in the string are alphanumeric
my_string.isspace()       # Returns True if all characters in the string are whitespace
my_string.istitle()       # Returns True if the string is in title case

