__author__ = "Narwhale"


# practice = __import__('practice.index')        #不建议使用
#
# print(practice.index.C().name)
#

import importlib

index = importlib.import_module('practice.index')
print(index.C().name)

