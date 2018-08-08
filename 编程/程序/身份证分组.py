lst = []
while 1:
    ID_number = input()
    l = len(ID_number)
    if l !=0:
        lst.append(ID_number.replace(' ', ''))
    else:
        break
for item in lst:
    itemLen = len(item)
    if itemLen <= 6:
        print(item)
    elif itemLen >6 and itemLen <=14:
        print(item[0:6],item[6:])
    elif itemLen >14 and itemLen <=18:
        print(item[0:6],item[6:14],item[14:])
    else:
        print('ID number ilegal!')