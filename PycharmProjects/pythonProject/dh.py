import sys
sys.setrecursionlimit(100000)

def f(n,a):
    if n in a:
        return a[n]
    if n<2025:
        a[n]=n**2
    if 2025<=n<2050:
        a[n]=2*f(n-1,a)-f(n-2,a)+n
    if 2050<=n<=2100:
        a[n]=f(n-1,a)+2*f(n-2,a)+3*f(n-3,a)
    if n>2100:
        a[n]=2*f(n-1,a)+f(n-2,a)+n
    return a[n]
print(f(2020,{})+f(2200,{}))

