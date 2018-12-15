# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 22:15
# @Author  : huangjie
# @File    : async_await.py

# python为了将语义变得更加明确，就引入了async和await关键词用于定义原生的协程
# import types
#
# @types.coroutine
# def downloader(url):
#     yield "tom"

async def downloader(url):
    return "tom"

async def download_url(url):
    html = await downloader(url)
    return html

if __name__ == "__main__":
    coro = download_url("http://www.imooc.com")
    # next(None) # 原生的协程不能用next方式调用
    coro.send(None)

