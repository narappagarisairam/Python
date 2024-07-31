#electricity bill
x=int(input("enter the meter number "))
y=int(input("previous reading number"))
z=int(input("current reading number"))
if z>y:
    total=z-y
    print(total)
    if total <100:
        total=total*2.50
        print(total)
    elif total>100 and total<150:
        total=total*3.50
        print(total)
    elif total>150 and total<200:
        total=total*4.50
        print(total)
    elif total>200 and total<300:
        total=total*5.50
        print(total)
    else:
        total=total*6.50
        print(total)
else:
    print("invalid data input")
