import numpy as np
import re
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c = np.where(a == b)
print(c)
print(np.where((a < 10) & (a > 2)))
num = 0
mo = re.compile(r'13810012093')
while True:
    cmd = input()
    if cmd == 'exit':
        break
    else:
        match = re.search(mo, cmd)
        num += 1       
        if match:
            print('Find result:', match.group()) 
        else:
            print('NOT MATCH, pelase type in again')
        print('The tick is %d' % (num))
        print('Enter exit to quit')
