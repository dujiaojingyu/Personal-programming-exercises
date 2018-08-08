# _*_ coding: utf-8 _*_
# 程序 9-2  (Python 3 version)

import requests

url = 'http://www.moe.gov.cn/'

html = requests.get(url).text.splitlines()
for i in range(0,15):
    print(html[i])
