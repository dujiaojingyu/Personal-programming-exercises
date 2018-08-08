# _*_ coding: utf-8 *_*
# 程序 9-4 (Python 3 version)

import requests, re

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
url = 'http://xxx.xxx.xxx'

html = requests.get(url).text

emails = re.findall(regex,html)
for email in emails:
    print(email)
