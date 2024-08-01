#print prime number between 1 to n
x=int(input("enter the number"))
for i in range(2,x+1):
    for x in range(2,int(i**0.5)+1):
     if x%i==0:
         break
else:
    print(i)
