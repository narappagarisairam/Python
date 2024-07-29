# if loop syntax example
x = 10
if x > 5:
    print("x is greater than 5")
#output:
x is greater than 5

# if else
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
#output
x is greater than 5

#secound example
x=int(input("enter the number"))
if x%2==0:
    print("even number")
else:
    print("odd number")

#output
enter the number 56
even number
#if elif else
x=int(input("enter the number"))
if x<0:
    print("enter valid number")
elif x%2==0:
    print("even number")
else:
    print("odd number")
#output
enter the number 55
odd number
#another example
x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
#output
x is equal to 5

