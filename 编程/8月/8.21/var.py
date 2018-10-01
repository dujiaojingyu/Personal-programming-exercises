__author__ = "Narwhale"

import re
st = input("输入字符串:").strip()
num = re.findall(r'\d+\.?\d*',st)
result = ''.join(num)
print(result)
