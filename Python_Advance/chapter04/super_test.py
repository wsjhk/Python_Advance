# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 12:58
# @Author  : huangjie
# @File    : super_test.py


class A(object):
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        # python2中的用法，super函数只能用于新式类中，不能用于经典类，python3之后不管有没有继承object都是使用新式类的。
        super(B, self).__init__()
        # python3当中的简化用法，是一样的
        # super().__init__()

# 既然我们重写了B的构造函数，为什么还要去调用super？因为可以重用继承类的代码，如下MyThread类的实现。
# super的执行顺序是怎么样的？super的执行顺序是遵循mro查找算法的。

from threading import Thread

class MyThread(Thread):
    def __init__(self, name, user):
        # 这个super和下面的self.name = name是一样的，但是用super重用了Thread类的代码和逻辑
        super(MyThread, self).__init__(name=name)
        # self.name = name
        self.user = user



if __name__ == "__main__":
    b = B()

