#reverse the number
n=int(input("enter the number"))
reverse=0
while n>0:
    m=n%10
    reverse=reverse*10+m
    n=n//10
print(reverse)
