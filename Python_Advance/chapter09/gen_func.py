# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 15:07
# @Author  : huangjie
# @File    : gen_func.py


# 生成器函数，函数里只要有yield关键字
def gen_fun():
    yield 1
    yield 2
    yield 3

def func():
    return 1

# 斐波那契实现
def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)

def fib1(index):
    re_list = []
    n,a,b = 0,0,1
    while n < index:
        re_list.append(b)
        a,b = b,a+b
        n += 1
    return re_list

def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1

for data in gen_fib(10):
    print (data)


if __name__ == "__main__":
    # 生成器对象，python编译字节码的时候就产生了
    gen = gen_fun()
    for value in gen:
        print(value)

    re = func()

    print(fib(10))
    print(fib1(10))



