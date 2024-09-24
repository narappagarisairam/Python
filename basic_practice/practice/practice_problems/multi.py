# Write a Python function to multiply all the numbers in a list.
def multi(list1):
    mul=1
    for i in list1:
        mul=mul*i
    print(mul)
list1=[1,2,3,4,5]
multi(list1)


from functools import *
def multi(list1):
    result=reduce(lambda x,y: x*y,list1)
    print(result)
list1=[1,2,3,4,5]
multi(list1)
