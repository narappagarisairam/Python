#5.	Write a Python program to reverse a string.
original=input("enther the string")
reverse=" "
for i in original:
    reverse=i+reverse
print(reverse)


original=input("enter thestring")
reverse=original[::-1]
print(reverse)
