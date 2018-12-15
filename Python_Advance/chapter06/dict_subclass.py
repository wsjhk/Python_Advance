# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 15:53
# @Author  : huangjie
# @File    : dict_subclass.py


# # 不建议继承list和dict
# class Mydict(dict):
#     def __setitem__(self, key, value):
#         super(Mydict, self).__setitem__(key, value * 2)
#
# # 不会执行子类中的__setitem__方法
# my_dict = Mydict(one=1)
#
# # 会执行子类中的__setitem__方法
# my_dict["one"] = 1
# print(my_dict)

from collections import UserDict

class Mydict(UserDict):
    def __setitem__(self, key, value):
        super(Mydict, self).__setitem__(key, value * 2)

# 会执行子类中的__setitem__方法
my_dict = Mydict(one=1)

# 会执行子类中的__setitem__方法
my_dict["one"] = 1
print(my_dict)

# defaultdict中的__missing__方法会在没有key的情况下设置一个key，值为空的dict
from collections import defaultdict

my_dict = defaultdict(dict)
my_value = my_dict["tom"] # my_value:{}


