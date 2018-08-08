__author__ = "Narwhale"

from urllib import request
import gevent,time
from gevent import monkey
monkey.patch_all()  #把当前程序的所有的io操作单独做上标记
def f(url):
    print('GET%s'%url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d 数据接收来自%s.' % (len(data), url))
start_time = time.time()
gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://github.com/'),
])
print('总共时间:',time.time()-start_time)