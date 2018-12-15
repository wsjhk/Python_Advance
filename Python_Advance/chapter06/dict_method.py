# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 15:12
# @Author  : huangjie
# @File    : dict_method.py

# 查看dict源码中的常用方法
ex = dict()

a = {"abc":{"a":"b"},
     "bcd":{"c":"d"}
     }

# a.clear()

# copy返回浅拷贝，a的["abc"]["a"]会变为e
# new_dict = a.copy()
# new_dict["abc"]["a"] = "e"
# print(a)
# print(new_dict)

# copy返回深拷贝，a的["abc"]["a"]不会变
import copy
new_dict = copy.deepcopy(a)
new_dict["abc"]["a"] = "e"
print(a)
print(new_dict)

# fromkeys方法
new_list = ["a", "b"]
new_dict2 = dict.fromkeys(new_list, {"aaa": "bbb"})
print(new_dict2)

