# function in function
#even numbers using filter
def iseven(x):
    if x%2==0:
        return True
    else:
        return False
L=[2,3,4,5,6,7,8,9,10]
L1=list(filter(iseven,L))
print(L1)
# using lambda 
L=[54,33,31,76,77,73,37]
L1=list(filter(lambda x:x%2==0,L)) #insted of that function in above using lambda is more effictive
print(L1)

