# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 16:51
# @Author  : huangjie
# @File    : an_error.py


def add(a, b):
    a += b
    return a


class Company:
    # 在主函数中com2和com3的staffs是一样的，原因是这里声明时是一个空的list，com2和com3没有传递list
    # 会指向Company.__init__.__defaults__，共用了一个list。com1中传递了list，所以不会指向Company.__init__.__defaults__
    def __init__(self, name, staffs = []):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


if __name__ == "__main__":
    com1 = Company("com1", ["tom", "jerry"])
    com1.add("jack")
    com1.remove("tom")
    print(com1.staffs)

    com2 = Company("com2")
    com2.add("bb")
    print(com2.staffs)

    com3 = Company("com3")
    com3.add("bbb")
    print(com2.staffs)
    print(com3.staffs)
    print(com2.staffs is com3.staffs)

    print(Company.__init__.__defaults__)

    a = 1
    b = 2
    c = add(a, b)
    print(c)
    print(a, b)

    aa = [1, 2]
    bb = [3, 4]
    cc = add(aa, bb)
    print(cc)
    print(aa, bb)

    aaa = (1, 2)
    bbb = (3, 4)
    ccc = add(aaa, bbb)
    print(ccc)
    print(aaa, bbb)

