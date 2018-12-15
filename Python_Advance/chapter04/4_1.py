# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 10:23
# @Author  : huangjie
# @File    : 4_1.py

class Cat(object):
    def say(self):
        print("i am a cat")


class Dog(object):
    def say(self):
        print("i am a dog")


class Duck(object):
    def say(self):
        print("i am a duck")


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]


company = Company(["tom", "bob", "jack"])

animal = Cat
animal().say()

animal_list = [Cat, Dog, Duck]
for an in animal_list:
    an().say()

a = ["bob"]
b = ["bob1"]
name_set = set()
name_set.add("bob3")

# extend方法的参数是一个iterable，所以只要是可迭代的对象都可以作为参数传递，即多态
a.extend(b)
a.extend(name_set)
a.extend(company)
print(a)


