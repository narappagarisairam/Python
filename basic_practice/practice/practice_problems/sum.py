#write a function to sum all the elements in agiven list
def sum(list1):
    sum=0
    for i in list1:
        sum=sum+i
    print(sum)
list1=[1,2,3,4,5,6,7,8,9,10]
sum(list1)

from functools import *
def sum(list1):
    result=reduce(lambda x,y: x+y,list1)
    print(result)
list1=[1,2,3,4,5,6,7,8,9,10]
sum(list1)
