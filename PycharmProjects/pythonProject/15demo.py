for a in range(1000):
    flag=True
    for x in range(500):
        for y in range(500):
            h=(x+2*y<a) or (y>x) or (x>60)
            if not h:
                flag=False
    if flag:
        print(a)



