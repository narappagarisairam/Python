#student pass or fail
x=int(input("enter a physics marks"))
y=int(input("enter the maths marks"))
z=int(input("enter the chemistry"))
if x<35 and y<35 and z<35:
    print("student fail")
else:
    print("student pass")
    total=x+y+z
    print("total marks",total)
    avg=total/3
    print("average is",avg)
    if avg >75:
        print("first class")
    elif avg>60:
        print("second class")
    else:
        print("third class")
