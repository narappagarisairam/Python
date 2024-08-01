#sum of the digits in a number
n=int(input("enter the number"))
sum=0
while n>0:
    m=n%10
    sum=sum+m
    n=n//10
print(sum)
