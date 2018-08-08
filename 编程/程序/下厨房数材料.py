lst = []
try:
    while 1:
        result = input()
        if result.isupper() and result !=0:
            L=result.split()
            for i in L:
                if i not in lst:
                    lst.append(i)
                else:
                    continue
            continue
        else:
            print(len(lst))
except EOFError:
    print(len(lst))