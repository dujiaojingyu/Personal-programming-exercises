f1 = open('yesterday','r',encoding='utf-8')
f2 = open('yesterday2','w',encoding='utf-8')
for line in f1:
    if '噢 昨日当我年少轻狂'in line:
        line = line.replace('噢 昨日当我年少轻狂','啦啦啦啦啦啦啦啦啦')
    f2.write(line)

f1.close()
f2.close()