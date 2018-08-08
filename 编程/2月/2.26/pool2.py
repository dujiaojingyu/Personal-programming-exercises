__author__ = "Narwhale"

from multiprocessing import Pool
import os,time
def f(i):
    time.sleep(1)
    print('子进程号---->>',os.getpid())
    return i+100

def Bar(arg):
    print('执行了Bar函数-->>',os.getpid())


if __name__ =='__main__':
    pool = Pool(5)  #允许进程池同时放入5个进程
    print('主进程--->>', os.getpid())
    for i in range(10):
        pool.apply_async(func=f,args=(i,),callback=Bar) # 并行
        #pool.apply_async(func=f,args=(i,))    #串行
    print("结束")
    pool.close()
    pool.join()
