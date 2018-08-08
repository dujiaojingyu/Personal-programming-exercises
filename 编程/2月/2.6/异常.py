__author__ = "Narwhale"

#异常结构
try:
    # 主代码块
    pass
except KeyError as e:
    # 异常时，执行该块
    pass
else:
    # 主代码块执行完，执行该块
    pass
finally:
    # 无论异常与否，最终执行该块
    pass

while True:
    num1 = input('num1:')
    num2 = input('num2:')
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
    except Exception as e:
        print ('出现异常，信息如下：',e)
