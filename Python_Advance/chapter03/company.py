# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 20:54
# @Author  : huangjie
# @File    : company.py


class Company(object):
    def __init__(self, employee_list, num):
        self.employee = employee_list
        self.num = num

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    def __str__(self):
        return ".".join(self.employee)

    def __repr__(self):
        return ".".join(self.employee)

    def __abs__(self):
        return abs(self.num)

    def __neg__(self):
        return (-self.num)


company = Company(["tom", "bob", "jack"], 1)
company1 = company[:2]

# 没有__getitem__魔法函数时
emploee = company.employee
for em in emploee:
    print(em)

#有__getitem__魔法函数时会和for循环取数据知道抛异常结束，如果注释掉该魔法函数运行会抛异常。
for em1 in company1:
    print(em1)

# len函数会首先调用__len__魔法函数，如果没有就会调用__getitem__，如果也没有就会抛异常
print(len(company))

# 实际上是调用了print(str(company))，调用了__str__这个魔法函数
print(company)

# 代码执行之后什么也不会输出，实际上是调用了__repr__这个魔法函数，在IDE不会显示，但是在ipython工具中执行会有输出
company

# __neg__是在-company的时候调用
print(abs(company))
print -company


# 二元运算符__add__实现
class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        re_vector = MyVector(self.x + other.x, self.y + other.y)
        return re_vector

    def __str__(self):
        return "x:{x}, y:{y}".format(x = self.x, y = self.y)

first_vec = MyVector(1, 2)
second_vec = MyVector(2, 3)
print(first_vec + second_vec)
