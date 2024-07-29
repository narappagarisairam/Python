#from functool import reduce
#method 1
L=[1,3,5,7,9]
s=0
for i in L:
    s=s+i
print("sum is",s)
#output
sum is 25

#method 2
#using reduse
from functools import reduce
def fun(x,y):
    return x+y
L=[1,3,5,7,9]
result=reduce(fun,L)
print(result)
#output
25

#using lambda function
L=[1,3,5,7,9]
result=reduce(lambda x,y:x+y,L)
print(result)
#output
25
