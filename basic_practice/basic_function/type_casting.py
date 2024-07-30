#type functionsairam

x=input("enter the number")
print(x)
print(type(x))
y=int(input("enter the nuber"))
print(y)
print(type(y))
z=int(input("enter the number"))
print(z)
p=float(input("enter the float number"))
print(p)
t=eval(input("enter the number"))
print(t)
r=bool(input("enter the bool value"))
 output:
     enter the number 34
34
<class 'str'>
enter the nuber 32
32
<class 'int'>
enter the number 34
34
enter the float number 56
56.0
enter the number 43
43
enter the bool value t


#type casting
# converting integer to float
a = 5      # integer
b = float(a)
print(b)   # Output: 5.0
print(type(b))  # Output: <class 'float'>

 # converting float to integer
a = 5.5    # float
b = int(a)
print(b)   # Output: 5
print(type(b))  # Output: <class 'int'>

# converting string to integer
a = "10"   # string
b = int(a)
print(b)   # Output: 10
print(type(b))  # Output: <class 'int'>

# converting string to float
a = "10.5"  # string
b = float(a)
print(b)   # Output: 10.5
print(type(b))  # Output: <class 'float'>

# converting integer to string
a = 10     # integer
b = str(a)
print(b)   # Output: '10'
print(type(b))  # Output: <class 'str'>

 # converting float to string
a = 10.5   # float
b = str(a)
print(b)   # Output: '10.5'
print(type(b))  # Output: <class 'str'>
 
 output:
     5.0
<class 'float'>
5
<class 'int'>
10
<class 'int'>
10.5
<class 'float'>
10
<class 'str'>
10.5
<class 'str'>
(1, 2, 3)
<class 'tuple'>
[1, 2, 3]
<class 'list'>
abc
<class 'str'>
['a', 'b', 'c']
<class 'list'>
['a', 'b', 'c']
<class 'list'>
