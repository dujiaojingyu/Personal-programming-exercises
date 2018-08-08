# _*_ coding: utf-8 _*_
#程序 8-5月.py (Python 3 version)

import sys, ast

if len(sys.argv)<2:
    print("使用方法：python 8-5月.py 成绩文件")
    exit(1)

scores = dict()
with open(sys.argv[1],'r') as fp:
    filedata = fp.read()
    scores = ast.literal_eval(filedata)
print("以下是{}成绩文件的字典类型:".format(sys.argv[1]))
print(scores)