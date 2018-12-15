# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 13:47
# @Author  : huangjie
# @File    : sequence_test.py

my_list = []
my_list.append(1)
my_list.append("a")

# from collections import abc
# 理解abc抽象序列继承关系

a = [1,2]
# +左右两边要是同一种数据类型
c = a + [3,4]

# +=左右两边可以不是同一种数据类型，通过abc模块的__all__中的MutableSequence中的__iadd__魔法函数来实现的
a += [3,4]
a += (3,4)

a.extend(range(3))
a.append((1,2))

print(c)
print(a)

