# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 20:50
# @Author  : huangjie
# @File    : yield_from_test.py


# python3.3新加了yield from语法

from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    "tom": "http://www.baidu.com",
    "tom1": "http://www.qq.com",
}

# yield from iterable
# def g1(iterable):
#     yield iterable
#
# def g2(iterable):
#     yield from iterable
#
# for value in g1(range(10)):
#     print(value)
#
# for value in g2(range(10)):
#     print(value)


def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable
        # for value in my_iterable:
        #     yield value


for value in my_chain(my_list, my_dict, range(5, 10)):
    print(value)


# 1.main 调用方g1（委托生成器） gen 子生成器
# 2. yield from 会在调用方与子生成器之间建立一个双向通道
final_result = {}

def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name + "销量：", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums

def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)   # yield from 建立了sales_num和main的双向通道
        print(key + "销量统计完成！！!")

def main():
    data_sets = {
        "tom牌面膜": [1200, 1500, 3000],
        "tom牌手机": [28, 55, 98, 108],
        "tom牌大衣": [280, 560, 778, 70],
    }
    for key, data_set in data_sets.items():
        print("start key:", key)
        m = middle(key)
        m.send(None) # 预激middle协程
        for value in data_set:
            m.send(value) # 给协程传递每一组值
        m.send(None)
    print("final_result:", final_result)


if __name__ == "__main__":
    main()


