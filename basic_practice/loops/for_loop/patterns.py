#patterns
n=5
for i in range(1,n):
    for j in range(1,i):
        print(j,end="")
    print()
    output:
        1
12
123


n=5
for i in range(0,n):
    for j in range(0,i):
        print(i,end="")
    print()
output:
    1
22
333
4444

n=3
current=1
for i in range (1,n+1):
    for j in range(i):
        print(current,end="")
        current+=1

    print()

    output:-
    1
23
456
