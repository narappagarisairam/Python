#simple calcuator
x=int(input("enter the number 1"))
y=int(input("enter the number 2"))
print("choose the option")
a=print("choose a for addition")
b=print("choose b for subtraction")
c=print("choose c for multiplication")
d=print("choose d for division")
result=input("choose the option")
if result=='a':
    print("sum of {x}and{y} is",x+y)
elif result=='b':
    print("sub of  {x}and {y} is:",x-y)
elif result=='c':
    print("mult of {x}and {y}is :",x*y)
elif result=='d':
     print("mult of {x}and {y}is :",x*y)
else:
    print("invalid option")
