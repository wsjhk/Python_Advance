# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 12:48
# @Author  : huangjie
# @File    : self_ex.py


# 自省是通过一定的机制查询到对象的内部结构
from chapter04.class_method import date

class Person:
    """
    人
    """
    name = "str"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == "__main__":
    user = Student("广石化")

    # 通过__dict__查询属性
    print(user.__dict__)
    user.__dict__["school_addr"] = "茂名市"
    print(user.school_addr)
    print(Person.__dict__)
    print(user.name)

    a = [1, 2]
    print(dir(a))

