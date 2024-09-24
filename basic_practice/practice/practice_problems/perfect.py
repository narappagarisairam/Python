#7.	Write a Python function to check whether a number is "Perfect" or not. 
def perfect(num):
    sum=0
    for i in range(1,num//2+1):
        if num%i==0:
            sum=sum+i
    if sum==num:
        print("it is a perfect number")
    else: 
        print("it is not perfect number")

num=int(input("enter the number"))
perfect(num)
