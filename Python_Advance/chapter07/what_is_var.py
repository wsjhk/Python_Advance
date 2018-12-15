# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 16:37
# @Author  : huangjie
# @File    : what_is_var.py

# python和java中的变量本质上不一样，python的变量实质上是一个指针，像是便利贴

# 1.a贴在1上面
# 2.先生成对象然后贴便利贴
a = 1
a = "abc"

a = [1,2,3]
b = a
b.append(4)
print(a)
print(id(a), id(b))
print(a is b)

aa = [1,2,3,4]
bb = [1,2,3,4]
# 对应int和str类型，python内部做了优化，重复赋值不会新生成对象
aaa = 1
bbb = 1
print(id(aa), id(bb))
print(aa is bb)
print(aa == bb)

print(id(aaa), id(bbb))
print(aaa is bbb)
