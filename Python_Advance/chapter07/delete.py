# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 16:47
# @Author  : huangjie
# @File    : delete.py


# python中垃圾回收的算法是采用 引用计数，对象有多个便利贴是计数增加，del后会减少，直到计数器为0，才回收对象
a = object()
b = a
del a
print(b)
print(a)

# 垃圾回收，重载__del__魔法函数
class A:
    def __del__(self):
        pass

