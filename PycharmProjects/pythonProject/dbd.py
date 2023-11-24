t=int(input())
for i in range(t):
    s=input()
    if all(s.count(x)==2 for x in s):
        print('Yes')
    else:
        print('No')
