import sys
sys.setrecursionlimit(100000)
def f(n):
    if n==1:
        return 1
    else:
        return n+f(n-1)
c=0
for n in range(1,101):
    if (f(2023)//f(n))%2==0:
        c=c+1
print(c)
