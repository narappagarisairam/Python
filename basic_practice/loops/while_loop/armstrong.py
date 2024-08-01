#armstrong number
n=int(input("enter the number"))
o=n
arm=0
while n>0:
    m=n%10
    arm=arm+m**3
    n=n//10
if o==arm:
    print("armstrong number")
else:
     print("not armstrong number") 
