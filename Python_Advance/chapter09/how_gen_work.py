# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 15:20
# @Author  : huangjie
# @File    : how_gen_work.py


# 1.python中函数的原理
"""
python已切皆对象，栈帧对象，字节码对象
当foo调用子函数bar，又会创建一个栈帧
所有的栈帧都是分配在堆内存上，这就决定了栈帧可以独立于调用者存在
"""
import inspect
frame = None
def foo():
    bar()

def bar():
    global frame
    frame = inspect.currentframe()


import dis
print(dis.dis(foo))

foo()
print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)



def gen_func():
    yield 1
    name = "tom"
    yield 2
    age = 27
    return "abc"  # python高版本才支持生成器函数有返回

import dis
gen = gen_func()
print(dis.dis(gen))

print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)


# from collections import UserList
