__author__ = "Narwhale"

import pymysql

#创建连接
conn = pymysql.connect(host='192.168.10.1',port=3306,user='root',passwd='1111',db='test')
#创建游标
cursor = conn.cursor()

#执行SQL并返回受影响的行数

# effect_row = cursor.execute("select * from student;")
effect_row = cursor.execute("update student set name='hsjsfd' where id>2")

print(cursor.fetchall())
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()