__author__ = "Narwhale"
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    '''测试employee.py文件'''

    def setUp(self):
        '''创建姓名及工资，供使用测试方法使用'''
        self.eric = Employee('eric', 'matthes', 65000)
    def test_give_default(self):
        '''测试默认年薪增加'''
        self.eric.give_raise()
        self.assertEqual(self.eric.salary,70000)
    def test_give_custom_raise(self):
        '''测试其他年薪增加'''
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.salary,75000)
