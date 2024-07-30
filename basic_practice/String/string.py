#string 
#it denote in double codes and also single codes
str1 = "Hello"
str2 = 'world'

#Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # "Hello World"
print(result)
#Repetition
str1 = "Hi"
result = str1 * 3  # "HiHiHi"
print(result)
#Slicing
str1 = "Hello, World!"
result = str1[0:5]  # "Hello"
print(result)
#Case Conversion
#to upper case
str1 = "Hello, World!"
upper_str = str1.upper()  # "HELLO, WORLD!"
print(upper_str)
#to lower case
str1 = "Hello, World!"
lower_str = str1.lower()  # "hello, world!"
print(lower_str)
#capitalize
str1 = "hello, world!"
capitalized_str = str1.capitalize()  # "Hello, world!"
print(capiticalzed_str)
#substring
#find method
str1 = "Hello, World!"
index = str1.find("World")  # 7

#index method
str1 = "Hello, World!"
index = str1.index("World")  # 7

#remove white space (stripping white spacing)
#strip():
str1 = "   Hello, World!   "
stripped_str = str1.strip()  # "Hello, World!"

#lstrip()
str1 = "   Hello, World!   "
lstripped_str = str1.lstrip()  # "Hello, World!   "

#rstrip
str1 = "   Hello, World!   "
rstripped_str = str1.rstrip()  # "   Hello, World!"

#Replacing Substrings
#replace().
str1 = "Hello, World!"
new_str = str1.replace("World", "Python")  # "Hello, Python!"

#Splitting and Joining
#splitting
str1 = "Hello, World!"
split_list = str1.split(", ")  # ['Hello', 'World!']

#joining
list_of_strs = ['Hello', 'World!']
joined_str = ", ".join(list_of_strs)  # "Hello, World!"
