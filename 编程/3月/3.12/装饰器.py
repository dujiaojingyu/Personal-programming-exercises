__author__ = "Narwhale"
import time
def timer(fun):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = fun()
        stop_time = time.time()
        print(stop_time-start_time)
        return res
    return wrapper


@timer
def foo():
    time.sleep(2)
    print('ahahaj')


foo()
