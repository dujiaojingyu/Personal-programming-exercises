__author__ = "Narwhale"


# -*- coding:utf-8 -*-
class Solution(object):
    # array 二维列表
    def Find(self, target, array):
        # write code here
        x = 0
        y = len(array)-1
        if y == 0:
            return False
        else:
            while x <= len(array[1])-1 and y >= 0:
                if target == array[y][x]:
                    return True
                if target > array[y][x]:
                    x += 1
                else:
                    y -= 1
            return False

b =[[],[]]

s = Solution()
print(s.Find(16,b))