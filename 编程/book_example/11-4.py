# _*_ coding: utf-8 _*_
# 程序 11-4 (Python 3 version)

from firebase import firebase
db_url = 'https://python01.firebaseio.com'
fdb = firebase.FirebaseApplication(db_url, None)

while True:
    inv_lotto = dict()
    inv_month = input('请输入开奖月份(例：201511，输入-1结束):')
    if int(inv_month) == -1 :
        break
    exist_data = fdb.get('/invlotto/'+inv_month, None)
    if exist_data != None:
        print("该月份已有数据，请重新输入")
        continue
    inv_lotto['p1000w'] = input('请输入特别奖1000万的号码：')
    inv_lotto['p200w'] = input('请输入特奖200万的号码：')
    inv_lotto['p20w'] = list()
    while True:
        p20w = input('请输入头奖20万的号码（输入-1结束）：')
        if int(p20w) == -1:
            break
        inv_lotto['p20w'].append(p20w)
    inv_lotto['p200'] = list()
    while True:
        p200 = input('请输入增开六奖的号码（输入-1结束)：')
        if int(p200) == -1:
            break
        inv_lotto['p200'].append(p200)
    print("以下是您输入的内容：")
    print("开奖月份:", inv_month)
    print("1000万特别奖:", inv_lotto['p1000w'])
    print("200万特奖:", inv_lotto['p200w'])
    print("20万头奖:", end="")
    for n in inv_lotto['p20w']:
        print(n + "  ", end="")
    print("\n200元增开六奖:", end="")
    for n in inv_lotto['p200']:
        print(n + "  ", end="")
    ans = input("\n是否写入Firebase网络数据库？(y/n)")
    if ans == 'y' or ans == 'Y':
        fdb.post('/invlotto/' + inv_month, inv_lotto)
    