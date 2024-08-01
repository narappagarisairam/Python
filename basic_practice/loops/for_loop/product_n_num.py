# print product of one to n numbers
x=int(input("enter the number"))
product=1
for i in range(x):
    product=product*x
    x-=1
print(product)
