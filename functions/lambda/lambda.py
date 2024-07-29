#max of two numbers
z=lambda x,y:x if x>y else y
x=10
y=20
print(z(x,y))

#output
20
#min of two numbers
z=lambda x,y:x if x<y else y
x=10
y=20
print(z(x,y))
#output
10
#max of three
z=lambda x,y,z: (x if (x>y and x>z) else y if  y>z else z)
x=10
y=20
d=30
print(z(x,y,d))
#output
30
#min of three
z=lambda x,y,z: (x if (x<y and x<z) else y if  y<z else z)
x=10
y=20
d=30
print(z(x,y,d))
#output
10
#sum of two
z=lambda x,y: x+y
x=10
y=20
print(z(x,y))
#output
30
#product of two
z=lambda x,y: x*y
x=10
y=20
print(z(x,y))
#output
200
#leap year
z=lambda x: "leap year" if x%4==0 else "not a leap year"
x=2024
print(z(x))
#output
leap year
#positive negative number
z=lambda x:"positive number" if x>0 else "negative number"
x=-5
print(z(x))
#output
negative number
#even or odd
z=lambda x:"even" if x%2==0 else "odd number"
x=66
print(z(x))
#output
even
