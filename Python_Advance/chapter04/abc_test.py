# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 10:48
# @Author  : huangjie
# @File    : abc_test.py


# 我们去检查某个类是否有某种方法

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

com = Company(["bob1", "bob2"])
print(hasattr(com, "__len__"))
# print(len(com))

# 我们在某些情况之下希望判定某个对象的类型
# from collections.abc import Sized
# isinstance(com, Sized)
# print(len(com))

# 我们需要强制某个子类必须实现某些方法
# 实现一个web框架，集成cache（redis，cache，memcache）
# 需要设计一个抽象基类，指定子类必须实现某些方法

# 如何去模拟一个抽象基类
class CacheBase():
    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


class RedisCache(CacheBase):
    def set(self, key, value):
        pass

# 如果RedisCache没有实现set方法就会抛异常
redis_cache = RedisCache()
redis_cache.set("key", "value")


import abc

class CacheBase1():
    __metaclass__ = abc.ABCMeta # python2的写法，python3直接class CacheBase1(metaclass=abc.ABCMeta)即可

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache1(CacheBase1):
    def set(self, key, value):
        pass

# 如果RedisCache1没有实现set和get方法在初始化的时候就会抛异常并提示没有实现哪些方法
redis_cache1 = RedisCache1()
