def f(s):
    while '12' in s or '322' in s or '222' in s:
        s = s.replace('12', '2', 1)
        s = s.replace('322', '21', 1)
        s = s.replace('222', '3', 1)
    return s
mx=0
for n in range(4,10000):
    s='1'+n*'2'
    s=f(s)
    m=(sum(map(int, s)))
    mx=max(mx,m)
print(mx)

