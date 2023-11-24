c=[]
f=open('17_8954.txt')
a=f.readlines()
f.close()
a=list(map(int, a))
ms=max(x for x in a if hex(x)[-2:]=='0f')
for x,y in zip(a, a[1:]):
    if (x%7==0)+(y%7==0)==1:
        if (x+y)%ms==0:
            c.append(x+y)
print(len(c), max(c))
