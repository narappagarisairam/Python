# print factorial  number n
x=int(input("enter the number"))
fact=1
for i in range(x):
    fact=fact*x
    x-=1
print(fact)
