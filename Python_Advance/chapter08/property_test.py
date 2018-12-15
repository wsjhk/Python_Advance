# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 17:27
# @Author  : huangjie
# @File    : property_test.py


# if __name__ == "__main__":方式在其他文件中import该文件时是不会执行的，如果不写这个主函数，import时会执行所有代码
from datetime import date, datetime

class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    def get_age(self):
        return datetime.now().year - self.birthday.year

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self.age = value



if __name__ == "__main__":
    user = User("tom", date(year=1991, month=1, day=1))
    user.age = 30
    print(user.get_age())
    print(user._age)
    print(user.age)

