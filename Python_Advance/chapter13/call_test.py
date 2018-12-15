# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 13:56
# @Author  : huangjie
# @File    : call_test.py


import asyncio

def callback(sleep_times, loop):
    print("success time {}".format(loop.time()))

def stoploop(loop):
    loop.stop()

# call_soon, call_later, call_at
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.call_soon(callback, 4, loop)
    loop.call_later(2, callback, 2, loop)
    loop.call_later(1, callback, 1, loop)
    loop.call_later(3, callback, 3, loop)
    now = loop.time()
    loop.call_at(now + 2, callback, 2, loop)
    loop.call_at(now + 1, callback, 1, loop)
    loop.call_at(now + 3, callback, 3, loop)
    # 需要停止loop，如果不停止程序不会stop
    # loop.call_soon(stoploop, loop)
    loop.run_forever()




