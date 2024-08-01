#how many factors for given number using for loop
x=int(input("enter the number"))
#z=x/2
count=1
for i in range(1,x):
    if x%i==0:
        count+=1  
print(count)
