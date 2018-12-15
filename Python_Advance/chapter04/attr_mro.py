# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 11:28
# @Author  : huangjie
# @File    : attr_mro.py


class A(object):
    name = "A"
    def __init__(self):
        self.name = "obj"


a = A()
# 如果A这个类中没有实现self.name这个实例变量，a.name会打印出类变量name，也就是会向上查找
print(a.name)
# 打印类继承的顺序
print(A.__mro__)

# 创建一个经典类，在多继承时使用深度继承
class B:
    def __init__(self):
        print("init")

    def __call__(self):
        sig = "C"
        C(self, sig)

    @classmethod
    def abc(cls, sig):
        print(sig + " ==> B")

# 创建一个新式类，在多继承时使用广度继承
class C(object):
    def __init__(self, app, sig):
        app.abc(sig)

a = B()
a()
