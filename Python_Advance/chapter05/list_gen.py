# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 14:55
# @Author  : huangjie
# @File    : list_gen.py


# 列表生成式（列表推导式）
# 1. 提取出1-20直接的奇数
odd_list = []
for i in range(21):
    if i%2 == 1:
        odd_list.append(i)

odd_list = [i for i in range(21) if i % 2 == 1]

# 2. 逻辑复杂的情况
def hadle_item(item):
    return item * item

odd_list = [hadle_item(i) for i in range(21) if i % 2 == 1]

# 列表生成式性能高于列表操作
print(type(odd_list))
print(odd_list)

# 生成器表达式
odd_gen = (i for i in range(21) if i % 2 == 1)

odd_list = list(odd_gen)
print(type(odd_list))
print(odd_list)

print(type(odd_gen))
for item in odd_gen:
    print(item)


# 字典推导式
my_dict = {"tom": 22, "bob": 21}
reversed_dict = {value:key for key, value in my_dict.items()}
print(reversed_dict)

# set推导式
# my_set = set(my_dict.keys())
my_set = {key for key, value in my_dict.items()}
print(type(my_set))
print(my_set)

