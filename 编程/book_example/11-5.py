# _*_ coding: utf-8 _*_
# 程序 11-5月 (Python 3 version)

from firebase import firebase
db_url = 'https://python01.firebaseio.com'
fdb = firebase.FirebaseApplication(db_url, None)

def disp_menu():
    print('统一发票号码管理')
    print('-------------')
    print('1. 输入开奖号码')
    print('2. 显示开奖号码')
    print('3. 删除开奖号码')
    print('0. 结束程序')
    print('-------------')
    ans = input('您的选择：')
    return int(ans)

def enter_lotto():
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

def disp_lotto():
    lottos = fdb.get('/invlotto', None)
    if lottos == None:
        print('没有任何开奖数据可供显示...')
        return
    inv_months = list(lottos.keys())
    print("现有数据如下：")
    for inv_month in inv_months:
        print("开奖月份：", inv_month)
        key_id = list(lottos[inv_month].keys())[0]
        print("1000万特别奖：{}".format(lottos[inv_month][key_id]['p1000w']))
        print(" 200万  特奖：{}".format(lottos[inv_month][key_id]['p200w'])) 
        print("  20万  头奖：", end="")
        for i in lottos[inv_month][key_id]['p20w']:
            print(str(i) + "   ", end="")
        print("\n    增开六奖：", end="")
        for i in lottos[inv_month][key_id]['p200']:
            print(str(i) + "   ", end="")
        print("\n")

def del_lotto():
    lottos = fdb.get('/invlotto', None)
    if lottos == None:
        print('没有任何开奖数据可供删除...')
        return
    inv_months = list(lottos.keys())
    print("现有可删除的数据如下：")
    for inv_month in inv_months:
        print(inv_month)
    target = input('请输入欲删除的月份(-1表示不删除)：')
    if target not in inv_months:
        print("输入错误，无此月份的数据...")
        return

    key_id = list(lottos[target].keys())[0]
    print(lottos[target][key_id])
    ans = input('你确定要删除以上这份数据吗？(y/n)')
    if ans == 'y' or ans == 'Y':
        fdb.delete('/invlotto/'+target, None)

while True:
    ans = disp_menu()
    if ans == 1:
        enter_lotto()
    elif ans == 2:
        disp_lotto()
    elif ans == 3:
        del_lotto()
    else:
        break
print("程序结束，谢谢使用") 
