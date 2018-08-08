__author__ = "Narwhale"

import threading,time

def run(n):
    print('task',n)
    time.sleep(2)

t_objs = []
start_time = time.time()
for i in range(50):
    t = threading.Thread(target=run,args=('t%s'%i,))
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()

print('run time....:',time.time()-start_time)
print('run done....')