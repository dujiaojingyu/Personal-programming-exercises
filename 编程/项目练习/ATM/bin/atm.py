__author__ = "Narwhale"
'''
客户运行模块
'''
import os,sys

base_dir = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))  #返回此文件路径
print(base_dir)
sys.path.append(base_dir)           #添加路径到环境变量
from core import main

if __name__ == '__main__':
    main.run()
