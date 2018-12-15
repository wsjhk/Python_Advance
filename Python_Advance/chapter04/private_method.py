# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 12:39
# @Author  : huangjie
# @File    : private_method.py

from chapter04.class_method import date

class User:
    def __init__(self, birthday):
        # 使用"__"定义私有属性
        self.__birthday = birthday

    def get_age(self):
        # 返回年龄
        return 2018 - self.__birthday.year

if __name__ == "__main__":
    user = User(Date(1991, 03, 06))

    # 不能通过实例访问私有属性
    print(user.__birthday)

    # 但是通过这种变形还是可以访问的，无法做到绝对安全
    print(user._User__birthday)

    print(user.get_age())
