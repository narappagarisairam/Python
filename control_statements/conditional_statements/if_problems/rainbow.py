#rainbow colour
num=int(input("enter the number from 1 to 7 :"))
if num <= 0:
    print("its invalid")
else:
    print("choose your colours in Rainbow")
    if num==1:
        print("the colour is VIOLET")
    elif num==2:
        print("the colour is  INDIGO")
    elif num==3:
        print("the colour is  BLUE")
    elif num==4:
        print("the colour is GREEN")
    elif num==5:
        print("the colour is YELLOW")
    elif num==6:
        print("the colour is ORANGE")
    elif num==7:
        print("the colour is RED")
    else:
        print(" you are choosing invalid Rainbow colour")
