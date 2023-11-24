def f(n):
    n2=bin(n)[2:]
    if n%3==0:
        n2=n2+n2[-3:]
    else:
        n2=n2+bin(n%3*3)[2:]
    return int(n2, 2)
for n in range(100):
    r=f(n)
    if r>76:
        print(n)

