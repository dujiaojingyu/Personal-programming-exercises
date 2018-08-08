# _*_ coding: utf-8 _*_
# 程序 9-3 (Python 3 version)

import requests

url = 'http://www.xxx.edu.cn/exam/check_001_NO_0_2015.html'
name = input("请输入要查询的姓名:")
html = requests.get(url).text
if name in html:
    print("恭喜名列金榜")
else:
    print("不好意思，榜单中找不到{}".format(name))