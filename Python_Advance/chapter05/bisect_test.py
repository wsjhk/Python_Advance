# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 14:41
# @Author  : huangjie
# @File    : bisect_test.py


import bisect

# 用来处理已排序的序列，用来维持已排序的序列，升序
# 二分查找，效率高
inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)

# 默认bisect.bisect() = bisect.bisect_right()
print(bisect.bisect(inter_list, 3))
print(bisect.bisect_left(inter_list, 3))
print(inter_list)

