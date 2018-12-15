# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 10:13
# @Author  : huangjie
# @File    : metaclass_test.py


# 类也是对象，type创建类的类
def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company


def say(self):
    return "i am user"
    # return self.name

class BaseClass(object):
    def answer(self):
        return "i am baseClass"

# type动态创建类
User = type("User", (BaseClass,), {"name": "user", "say": say})


class MateClass(type):
    def __new__(cls, *args, **kwargs):
        return super(MateClass, cls).__new__(cls, *args, **kwargs)

# 什么是元类，元类是创建类的类，对象<-class(对象)<-type
class MyUser(object):
    __metaclass__ = MateClass

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "user"

# python中类的实例化过程，会首先寻找metaclass，通过metaclass去创建user类
# 去创建类对象，实例

if __name__ == "__main__":
    MyClass = create_class("user")
    my_obj = MyClass()
    print(type(my_obj))

    my_obj1 = User()
    print(my_obj1.name)
    print(my_obj1.say())
    print(my_obj1.answer())

    my_obj2 = MyUser("jerry")
    print(my_obj2)

