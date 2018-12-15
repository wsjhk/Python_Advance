# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 17:52
# @Author  : huangjie
# @File    : getattr.py


# __getattr__、__getattribute__
# __getattr__ 就是查找不到属性的时候调用,__getattribute__ 比 __getattr__更高级，优先级更高

from datetime import date

class User(object):
    def __init__(self, info = {}):
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    def __getattribute__(self, item):
        return "tom"


if __name__ == "__main__":
    user = User(info = {"name": "abc"})
    print(user.name)
    print(user.age)

