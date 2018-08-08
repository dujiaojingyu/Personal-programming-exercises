# _*_ coding: utf-8 _*_
#程序 8-6.py (Python 3 version)

def disp_area():
    i = 0
    for a in climate_data:
        print("{:>2}:{:<6}\t".format(i,a[0]), end="")
        i += 1
        if not (i % 5): print()
    print()

def disp_temp(data):
    print("显示城市:", data[0])
    print("---------------------")
    for i in range(1,12):
        print("{:>2}月平均温度:>.1f}度".format(i, float(data[i])))
    print("---------------------")

target_file = 'climate.txt'
with open(target_file, 'r', encoding='utf-8') as fp:
    raw_data = fp.readlines()
climate_data=[]
for item in raw_data:
    climate_data.append(item.rstrip('\n').split('\t'))

while True:
    disp_area()
    area = int(input("请输入你要查询平均温度的城市：(-1结束)"))
    if area == -1: break
    disp_temp(climate_data[area])
    x = input("请按Enter键回主菜单")