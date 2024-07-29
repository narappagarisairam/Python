#simple calculater
def add(x,y):
    z=x+y
    return z
def sub(x,y):
    z=x-y
    return z
def multi(x,y):
    z=x*y
    return z
def div(x,y):
    z=x/y
    return z
x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
opt=int(input("enter the option"))
if opt==1:
    t=add(x,y)
   
elif opt==2:
    t=sub(x,y)
  
elif opt==3:
    t=multi(x,y)
   
else:
    t=div(x,y)
print(t)
#output
enter the value of x 57
enter the value of y 65
enter the option 66
0.8769230769230769
