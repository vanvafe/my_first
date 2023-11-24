
c=[]
f=open('17_10100.txt')
a=f.readlines()
f.close()
a=list(map(int, a))
mx=max(x  for x in a  if x%100==13)
for x,y,z in zip(a, a[1:], a[2:]):
    if (100<=x<=999)+(100<=y<=999)+(100<=z<=999)==2:
        if x+y+z<=mx:
            c.append(x+y+z)
print(max(c),len(c))
