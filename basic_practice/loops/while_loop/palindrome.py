#palindrome number
n=int(input("enter the number"))
o=n
reverse=0
while n>0:
    m=n%10
    reverse=reverse*10+m
    n=n//10
if o==reverse:
    print("palindrome")
else:
    print("not a palindrome")
