# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 19:50
# @Author  : huangjie
# @File    : type_object_class.py

a = 1
b = "abc"
print(type(1))
print(type(int))
print(type(b))
print(type(str))

# type -> int -> 1
# type -> class -> obj

# object是最顶层基类
# type也是一个类，同时type也是一个对象


class Student:
    pass

class MyStudent(Student):
    pass

stu = Student()
print(type(stu))
print(type(Student))
print(int.__bases__)
print(str.__bases__)
print(Student.__bases__)
print(MyStudent.__bases__)
print(type.__bases__)
print(object.__bases__)
print(type(object))


