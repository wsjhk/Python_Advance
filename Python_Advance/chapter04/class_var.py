# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 11:22
# @Author  : huangjie
# @File    : class_var.py


class A:
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(2, 3)

# aa是类变量，是共享的，x,y是实例变量，a.aa中实例会向上查找，而A.x不会向下查找
A.aa = 11
a.aa = 100
print a.x, a.y, a.aa
print(A.aa)
# print(A.x)

b = A(3, 5)
print(b.aa)

