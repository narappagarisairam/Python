 checking prime numbers in a given limit
s = int(input("Enter the starting limit: "))
e = int(input("Enter the ending limit: "))
current = s

while current <= e:
    if current > 1:  
        i = 2
        while i <= current // 2:
            if current % i == 0:
                break
            i += 1
        else:
            print(current, end=' ')
    current += 1
