# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 11:59
# @Author  : huangjie
# @File    : class_method.py


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 实例方法
    def tomorrow(self):
        self.day += 1

    # 静态方法
    @staticmethod
    def pasre_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    # 静态方法，这种情况下是不需要传递或者返回Date类本身的，就使用静态方法，和类方法的区别
    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year) > 0 and (int(month) > 0 and int(month) < 12) and (int(day) > 0 and int(day) < 31):
            return True
        else:
            return False

    # 类方法，也是动态方法
    @classmethod
    def from_string(cls, date_str): # 这里的cls是规范的写法，当然改成其他也是可以的
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)

if __name__ == "__main__":
    new_day = Date(2018, 12, 01)
    new_day.tomorrow()
    print(new_day)

    # 2018-12-31
    date_str = "2018-12-31"
    year, month, day = tuple(date_str.split("-"))
    new_day = Date(int(year), int(month), int(day))
    print(new_day)

    # 用staticmethod完成初始化，替换掉上一段代码，是的调用更简洁，但是静态方法中的Date是硬编码，类名改变之后也必须要跟着改变，类方法解决。
    new_day = Date.pasre_from_string(date_str)
    print(new_day)

    # 用classmethod完成初始化，解决了硬编码问题
    new_day = Date.from_string(date_str)
    print(new_day)

    # 用staticmethod实现比classmethod好，无需传递cls。
    print(Date.valid_str("2018-12-32"))
