# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 11:18
# @Author  : huangjie
# @File    : isinstance_type.py


class A:
    pass


class B(A):
    pass

b = B()
# isinstance会去继承关系中找，type不会
print(isinstance(b, B))
print(isinstance(b, A))
print(type(b) is A)
