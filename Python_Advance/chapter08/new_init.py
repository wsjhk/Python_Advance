# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 10:01
# @Author  : huangjie
# @File    : new_init.py


class User(object):
    def __new__(cls, *args, **kwargs):
        print("in new")

        # 如果不return，则不会执行__init__函数
        return super(User, cls).__new__(cls)

    def __init__(self, name):
        print("in init")
        self.name = name

# new是用来控制对象的生成过程，在对象生成之前
# init是用来完善对象的
# 如果new方法不返回对象，则不会调用init函数
if __name__ == "__main__":
    user = User("tom")


