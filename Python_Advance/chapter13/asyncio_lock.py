# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 14:38
# @Author  : huangjie
# @File    : asyncio_lock.py

# total = 0
#
# async def add():
#     global total
#     for i in range(1000000):
#         total += 1
#
# async def desc():
#     global total
#     for i in range(1000000):
#         total -= 1
#
# if __name__ == "__main__":
#     import asyncio
#     tasks = [add(), desc()]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(total)

import asyncio
from asyncio import Lock, Queue

lock = Lock()
cache = {}

async def get_stuff(url):
    # await lock.acquire()
    # with await lock:
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET', url)
        cache[url] = stuff
        return stuff
    # lock.release()


async def parse_stuff():
    stuff = await get_stuff()

async def use_stuff():
    stuff = await get_stuff()


