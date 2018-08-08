__author__ = "Narwhale"

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,56,68,92,98,102,135,149]


def b_search(database,find_num):
    print('查找数字>>',find_num)

    if len(database) > 1:
        m = int(len(database)/2)
        if database[m] == find_num:
            print('找到数字了>>',database[m])

        elif database[m] > find_num:
            return b_search(database[0:m],find_num)
        else:
            return b_search(database[m+1:len(database)],find_num)


    else:
        if database[0]==find_num:
            print('找到数字了>>', database[0])

        else:
            print('没有找到要查找的数字')

b_search(data,85)