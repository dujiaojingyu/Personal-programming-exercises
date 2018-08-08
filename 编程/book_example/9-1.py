# _*_ coding: utf-8 _*_
# 程序 9-1  (Python 3 version)
from urllib.parse import urlparse

url = 'http://www.chinahr.com/sou/?city=398&keyword=%E9%80%9A%E4%BF%A1%E5%B7%A5%E7%A8%8B%E5%B8%88&companyType=3&degree=0&refreshTime=0&workAge=0'

uc = urlparse(url)
print("NetLoc:", uc.netloc)
print("Path:", uc.path)

q_cmds = uc.query.split('&')
print("Query Commands:")
for cmd in q_cmds:
    print(cmd)
