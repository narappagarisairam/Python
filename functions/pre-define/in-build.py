#The print() function outputs text or other data to the console.
print("Hello, World!")
output
hello world
#The input() function reads a line of text from the user.
name = input("Enter your name: ")
print("Hello, " + name + "!")
output:
    Enter your name: Alice
Hello, Alice!

#The type() function returns the type of an object.
x = 10
print(type(x))

y = "Hello"
print(type(y))
output:
    <class 'int'>
<class 'str'>

#The eval() function parses the expression passed to it and runs Python expression (code) within the program.
expression = "2 + 3 * 5"
result = eval(expression)
print(result)
#output:
17


