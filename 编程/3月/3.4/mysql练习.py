__author__ = "Narwhale"
import pymysql

#创建连接
conn = pymysql.connect(host='192.168.10.1',port=3306,user='root',passwd='1111',db='test')
#创建游标
cursor = conn.cursor()

#执行操作并返回影响数
effect_row = cursor.execute("select * from student")

print(cursor.fetchall())

conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()