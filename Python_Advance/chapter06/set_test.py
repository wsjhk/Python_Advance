# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 16:10
# @Author  : huangjie
# @File    : set_test.py


# set集合frozenset(不可变集合)无序，不重复
s = set("abcde")
ss = set(['a', 'b', 'c', 'd', 'e'])
sss = {'a', 'b'}
sss.add('c')
print(s)
print(ss)
print(sss)

s1 = frozenset("abcde")
print(s1)


# 向set添加数据,集合的运算操作set源码实现中的魔法函数实现
another_set = set("def")
s.update(another_set)
re_set = s.difference("cef")
re_set = s - another_set
re_set = s & another_set
re_set = s | another_set
print(s)
print(re_set)

