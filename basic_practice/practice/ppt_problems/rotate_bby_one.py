#basic problems
#rorate a list by one
l=[1,2,3,4,5]#[5,1,2,3,4]
rotated=[]
n=len(l)
rotated.append(n-1)
for i in range(n-1):
    rotated.append(i)
print(rotated)
    
    

