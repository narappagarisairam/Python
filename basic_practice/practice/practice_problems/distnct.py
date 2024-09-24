#6.	Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#using inbuilt method
def distinct(list1):
    result=set(list1)
    print(list(result))

list1=[1,2,3,1,2,3,4,3,5,6,3]
distinct(list1)


#without in built
def distinct(list1):
    d=[]
    for i in list1:
        if i not in d:
            d.append(i)
    print(d)
list1=[1,2,3,1,2,3,4,3,5,6,3]
distinct(list1)
