from itertools import permutations

v=[]
a=permutations('rrbbnnkq')
for i in a:
    s=''.join(i)
    if s.find('b')%2 != s.rfind('b')%2 and s.find('r') < s.find('k') < s.rfind('r'):
        v.append(s)
v=list(set(v))
print(len(v))