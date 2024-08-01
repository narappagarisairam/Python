#print sum of one to n numbers
x=int(input("enter the number"))
sum=0
for i in range(x):
    sum=sum+x
    x-=1
print(sum)
