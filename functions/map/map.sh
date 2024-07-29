#map is used to change the every element in the given list
def square(x):
    return x*x
#a=4
#result=square(4)
#print(result)
L=[1,2,3,4,5,6,7,8,9]
for i in L:
    K=square(i)
    print(K)
#output
1 4 9 ...
 #using lambda 
 #in lambda function maping
L=[1,2,3,4,5,6,7,8,9]
result=list(map(lambda x:x*x,L))
print(result)
