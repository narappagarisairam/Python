#  to check number is prime
num = int(input("enter the number"))
if num > 1:
    i = 2
    while i <= num // 2:
        if num % i == 0:
            print("not prime number")
            break
        i += 1
    else:
        print(" prime number.")
else:
    print("not prime number.")
