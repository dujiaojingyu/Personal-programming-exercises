__author__ = "Narwhala"
import time

print(time.time())                    #返回当前时间的时间戳
print(time.altzone)                     #返回与utc时间的时间差,以秒计算  -32400
print(time.asctime())                   #返回时间格式"Fri Jan 26 20:38:48 2018",
print(time.gmtime())                     #gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time
print(time.mktime(time.localtime()))       #将一个struct_time转化为时间戳
print(time.asctime())                    #把一个表示时间的元组或者struct_time表示为这种形式：'Fri Jan 26 20:38:48 2018'。如果没有参数，将会将time.localtime()作为参数传入。
print(time.asctime(time.gmtime()))        # 把一个表示时间的元组或者struct_time表示为这种形式：'Fri Jan 26 20:38:48 2018'。如果没有参数，将会将time.localtime()作为参数传入。
print(time.ctime())                      #把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。

string_2_struct = time.strptime("2018-01-26 20:38:48","%Y-%m-%d %H:%M:%S") #将 日期字符串 转成 struct时间对象格式
print(string_2_struct)

print(time.gmtime(time.time() - 86640))  # 将utc时间戳转换成struct_time格式
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) ) #将utc struct_time格式转成指定的字符串格式


import datetime

print(datetime.datetime.now())
print(datetime.date.fromtimestamp(time.time()))          # 时间戳直接转成日期格式2018-01-26
print(datetime.datetime.now()+datetime.timedelta(6))       #当前时间+6天
print(datetime.datetime.now()-datetime.timedelta(6))            #当前时间-6天
print(datetime.datetime.now()+datetime.timedelta(hours=6))        #当前时间+6小时
print(datetime.datetime.now()+datetime.timedelta(minutes=30))      #当前时间+30分
c_time  = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2))                              #时间替换