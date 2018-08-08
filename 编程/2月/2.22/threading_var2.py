__author__ = "Narwhale"

import threading
class Mytype(threading.Thread):
    def __init__(self,n):
        super(Mytype,self).__init__()
        self.n = n

    def run(self):
        print('task',self.n)

t1 = Mytype('t1')
t2 = Mytype('t2')

t1.start()
t2.start()