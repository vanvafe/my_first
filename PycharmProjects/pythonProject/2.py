#5знач в 20ричной
#2 цифры кратны 5
#след не меньше пред
from itertools import product
c=0
def check(i):
    if i.count('0')+i.count('5')+i.count('a')+i.count('f')==2 and i[0]!='0':
        if int(i[0], 20)<=int(i[1], 20)<=int(i[2], 20)<=int(i[3], 20)<=int(i[4], 20):
            return True
for i in product('0123456789abcdefghij', repeat = 5):
    if check(i):
        c+=1
print(c)