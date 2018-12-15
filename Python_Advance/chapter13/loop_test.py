# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 13:05
# @Author  : huangjie
# @File    : loop_test.py


# 事件循环+回调（驱动生成器）+epoll（IO多路复用）
# asyncio是python用于解决异步io编程的一整套方案
# tornado、gevent、twisted（scrapy，django channels）
# tornado（实现web服务器），django+flask（uwsgi，gunicorn+nginx）
# tornado可以直接部署，nginx+tornado

# 使用asyncio
# wait 和 gather的区别
# import asyncio
# import time
#
# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)
#     # time.sleep(2)
#     print("end get url")
#
#
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     tasks = [get_html("http://www.baidu.com") for i in range(10)]
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(time.time() - start_time)
#
#     tasks = [get_html("http://www.baidu.com") for i in range(10)]
#     # loop.run_until_complete(asyncio.gather(*tasks))
#     # print(time.time() - start_time)
#
#     group1 = [get_html("http://www.baidu.com") for i in range(2)]
#     group2 = [get_html("http://www.qq.com") for i in range(2)]
#     group1 = asyncio.gather(*group1)
#     group2 = asyncio.gather(*group2)
#     group2.cancel()
#     loop.run_until_complete(asyncio.gather(group1, group2))
#     print(time.time() - start_time)

# 获取协程的返回值
import asyncio
import time
from functools import partial

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    return "tom"

def callback(url, future):
    print("send email to tom")
    print(url)

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    get_future = asyncio.ensure_future(get_html("http://www.baidu.com"))
    # get_future.add_done_callback(callback)
    # callback函数有参数时，参数要放到future参数的前面，使用functool.partial偏函数来封装传参数
    get_future.add_done_callback(partial(callback, "http://www.baidu.com"))
    loop.run_until_complete(get_future)
    print(get_future.result())
    # 这里使用loop的方法和asyncio的方法等效，最终都是通过loop的方法来实现的
    # task = loop.create_task(get_html("http://www.baidu.com"))
    # task.add_done_callback(callback)
    # task.add_done_callback(partial(callback, "http://www.baidu.com"))
    # loop.run_until_complete(task)
    # print(task.result())
    print(time.time() - start_time)



