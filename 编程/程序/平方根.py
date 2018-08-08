#正数时
num = float(input("请输入所求数字："))
num_sqrt = num ** 0.5
print(num_sqrt)


#负数或者复数时
import cmath
num = int(input("请输入所求数字："))
num_sqrt = cmath.sqrt(num)
print('{0}的平方根为{1:0.3f} + {2:0.3f}j'.format(num,num_sqrt.real,num_sqrt.imag))


