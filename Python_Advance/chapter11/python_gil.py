# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 18:28
# @Author  : huangjie
# @File    : python_gil.py

# gil global interpreter lock (cpython)
# python中一个线程对应于c语言中的一个线程
# gil使得同一时刻只有一个线程在一个cpu上执行字节码，无法将多个线程映射到多个cpu上执行
# gil会根据执行的字节码行数和时间片释放gil，gil在遇到io操作时会主动释放

# import dis
#
# def add(a):
#     a = a+1
#     return a
#
# print(dis.dis(add))

total = 0

def add():
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
# 每次执行结果都不一样
print(total)
