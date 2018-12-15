# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 19:34
# @Author  : huangjie
# @File    : iterable.py


# 什么是迭代协议
# 迭代器是什么？迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下标的访问方式不一样，迭代器是不能返回的，迭代器提供了一种惰性方式数据的方式
# [] list，__iter__可迭代，迭代器必须实现__next__函数，可迭代和迭代器的区别
from collections.abc import Iterable, Iterator

a = [1,2]
print(a, Iterable)
print(a, Iterator)




