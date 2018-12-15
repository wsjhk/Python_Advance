# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 18:00
# @Author  : huangjie
# @File    : attr_desc.py

'''
如果user是某个类的实例，那么user.age(等价于getattr(user, 'age'))
首先调用__getattribute__，如果类定义了__getattr__方法。
那么在__getattribute__抛出 AttributeError 的时候就会调用到__getattr__，
面对于描述符(__get__)的调用，则是发生在__getattribute__内部的。
user=User()，那么user.age顺序如下：
（1）如果"age"是出现在User或其基类的__dict__中，且age是data descriptor，那么调用其__get__方法，否则
（2）如果"age"出现在user的__dict__中，那么直接返回obj.__dict__['age']，否则
（3）如果"age"出现在User或其基类的__dict__中
    （3.1）如果age是non-data descriptor，那么调用其__get__方法，否则
    （3.2）返回__dict__['age']
（4）如果User有__getattr__方法，调用__getattr__方法，否则
（5）抛出AttributeError
'''

from datetime import date, datetime
import numbers

class IntField(object):
    # 属性描述符
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value

    def __delete__(self, instance):
        pass


class NondataIntField(object):
    # 非数据描述符
    def __get__(self, instance, owner):
        return self.value


class User(object):
    age = IntField()
    # age = NondataIntField()

if __name__ == "__main__":
    user = User()

    # user.age = "abc"
    # user.age = -1
    user.age = 30
    print(user.age)
    print(user.__dict__)
    print(getattr(user, 'age'))
