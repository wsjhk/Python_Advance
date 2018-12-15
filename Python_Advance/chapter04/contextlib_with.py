# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 13:36
# @Author  : huangjie
# @File    : contextlib_with.py


import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    yield {}
    print("file end")

with file_open("bob.txt") as f_opened:
    print("file processing")

