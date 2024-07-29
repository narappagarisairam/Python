#nested if loop syntax and example
x = 10
if x > 5:
    print("x is greater than 5")
    if x > 8:
        print("x is also greater than 8")
    else:
        print("x is not greater than 8")
else:
    print("x is not greater than 5")
#output
x is greater than 5
x is also greater than 8
#second example
x = 7
if x > 5:
    print("x is greater than 5")
    if x > 8:
        print("x is also greater than 8")
    else:
        print("x is not greater than 8")
else:
    print("x is not greater than 5")
#output
x is greater than 5
x is not greater than 8

