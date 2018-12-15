# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 19:45
# @Author  : huangjie
# @File    : all_is_object.py


def ask(name="jhk"):
    print(name)


class Person:
    def __init__(self):
        print("jhk")


def print_type(item):
    print(type(item))


def decotator_func():
    print("dec start")
    return ask

# 1.赋值给一个变量
my_func = ask
my_func("wsjhk")

my_class = Person
my_class()

# 2.可以添加到集合对象中
# 3.可以作为参数传递给函数
obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for item in obj_list:
    print_type(item())

# 4.可以当做函数的返回值
my_ask = decotator_func()
my_ask("tom")
