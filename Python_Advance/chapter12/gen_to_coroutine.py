# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 21:59
# @Author  : huangjie
# @File    : gen_to_coroutine.py

# 生成器是可以暂停的函数
import inspect

def gen_func():
    value = yield 1
    # 第一返回值给调用方，第二调用方通过send方式返回值给gen
    return "tom"


if __name__ == "__main__":
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))


# # 1.用同步的方式编写异步的代码，在适当的时候暂停函数并在适当的时候启动函数
# import socket
# from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
# selector = DefaultSelector()
# def get_socket_data():
#     yield "tom"
#
# def downloader(url):
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.setblocking(False)
#     try:
#         client.connect(('127.0.0.1', 80))
#     except BlockingIOError as e:
#         pass
#
#     selector.register(client.fileno(), EVENT_WRITE, connected)
#     source = yield from get_socket_data()
#     data = source.decode("utf8")
#     html_data = data.split("\r\n\r\n")[1]
#     print(html_data)
#
# def download_html():
#     html = yield from downloader()
