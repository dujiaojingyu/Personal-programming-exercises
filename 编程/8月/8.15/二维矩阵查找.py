__author__ = "Narwhale"

"""
在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递
增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有
该整数。
"""

def find(target,array):
    """二维数组中查找"""
    row = len(array)-1
    column = 0
    if row == 0:
        return False
    while row >= 0 and column <= len(array[1])-1:
        if target == array[row][column]:
            return True
        elif target > array[row][column]:
            column += 1
        else:
            row -= 1
    return False


# # -*- coding:utf-8 -*-
# class Solution(object):
#     # array 二维列表
#     def Find(self, target, array):
#         # write code here
#         x = 0
#         y = len(array)-1
#         if y == 0:
#             return False
#         while x <= len(array[1])-1 and y >= 0:
#             if target == array[y][x]:
#                 return True
#             if target > array[y][x]:
#                 x += 1
#             else:
#                 y -= 1
#         return False


b=[[1, 2, 3, 4 ],
 [5, 6, 7, 8 ],
 [9, 10,11,12],
 [13,14,15,16],
 [17,18,19,20]]
#array[4][0]

#

f = find(20,b)
print(f)

# s = Solution()
#
# print(s.Find(20,b))