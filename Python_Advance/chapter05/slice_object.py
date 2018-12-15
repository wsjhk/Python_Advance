# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 14:02
# @Author  : huangjie
# @File    : slice_object.py

# 实现不可修改的序列
import numbers

class Group(object):
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        # return self.staffs[item]
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


staffs = ["tom", "bob", "jack"]
group = Group(company_name="abc", group_name="jhk", staffs=staffs)
sub_group = group[:2]
print(sub_group.staffs)
sub_group = group[0]
print(sub_group.staffs)

print(len(group))

if "tom" in group:
    print("yes")

reversed(group)

for user in group:
    print(user)



