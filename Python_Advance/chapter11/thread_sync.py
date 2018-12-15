# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 15:45
# @Author  : huangjie
# @File    : thread_sync.py

from threading import Lock, RLock # RLock可重入锁

total = 0
# Lock在同一线程中不能连续使用acquire，RLock可以，但是需要acquire和release操作次数一样
# lock = Lock()
lock = RLock()

def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        total += 1
        lock.release()
        lock.release()

def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
# 每次执行结果都一样
print(total)

# 1.用锁会影响性能
# 2.锁会引起死锁


