# _*_ coding: utf-8 _*_
# 10-2.py (Python 3 version)

from mysql import connector

db = connector.connect(
    host='db4free.net',
    user='juntest',
    passwd='****',
    database='juntest')
cur = db.cursor()
cur.execute('select * from PRICES;')
rows = list()
for row in cur:
  rows.append(row)

for i in range(0,10):
  print("日期：{}, 92无铅：{}, 95无铅：{}, 98无铅：{}".\
      format(rows[i][0], rows[i][1], rows[i][2], rows[i][3]))