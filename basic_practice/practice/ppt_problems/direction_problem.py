
#direction problem 
def direction(name):
    m=len(name)
    n=0
    e=0
    w=0
    s=0
    for i in range(m):
        if name[i]=='N':
            n+=1
        elif name[i]=='E':
            e+=1
        elif name[i]=='W':
            w+=1
        elif name[i]=='S':
            s+=1
    if s==n and w==e:
        return True
    else:
        return False

name1="NENESSW"
d=direction(name1)
print(d)
            
