__author__ = "Narwhala"

import random
code = ''
for i in range(5):
    if random.randrange(5) == i:        #不能用ranint（），因为与range()取值范围的不同 用==数字多，用!=字母多
        x = chr(random.randint(65,90))
    else:
        x = random.randint(0,9)
    code += str(x)
print(code)


import random
checkcode = ''
for i in range(4):
    current = random.randrange(0,4)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print (checkcode)