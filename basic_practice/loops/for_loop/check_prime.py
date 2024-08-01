#check number weather number is prime number
x=int(input("enter the number"))
count=1
for i in range(1,x):
     if x%i==0:
        count+=1  
if count==2:
     print("prime number")
else:
     print("non-prime number")
