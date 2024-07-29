#write a function in four perameters
#with perameters with return type
def multi(x,y):
    z=x+y
    return z
x=multi(10,20)
print(x)
#output
30
#with perameters no return type
def multi(x,y):
    z=x+y
    print(z)
x=multi(10,20)
#output
30
#with out peremeters without return type
def multi():
    x=int(input("enter the x value"))
    y=int(input("enter the y value"))
    z=x+y
    print(z)
multi()
#output
enter the x value 56
enter the y value 56
112
#without arguments with return type
def multi():
    x=int(input("enter the x value"))
    y=int(input("enter the y value"))
    z=x+y
    return z
c=multi()
print(c)
#output
enter the x value 56
enter the y value 56
112
