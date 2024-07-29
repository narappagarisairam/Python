#variable length aruguments
# it will be in list.
def add(*arg):
    s=0
    for i in arg:
        s=s+i
    return(s)
result=add(10,20,40,50)
print(result)
#output
120
#keyword argments
def greeting(name,msg):
    print(f"hi{name}{msg}")
greeting(name="sairam",msg="good morning")
#output:
hisairamgood morning
#variable length keyword arguments
arg={"name":"sairam","msg":"goodmorning"}
def greeting(**arg):
    for i in arg.keys():
         print(i,arg[i])
greeting(**arg)
#output
name sairam
msggoodmorning
#default arguments
def greet(name,msg="goodmorning"):
    print(f"hi {name} {msg}")
greet("sairam")
#output
hi sairam goodmorning
#default key arguments
def greet(name,age,location="hyderbad"):
          print(f"hi {name} {age} {location}")
greet("sairam",24)
#output:
hi sairam 24 hyderbad

