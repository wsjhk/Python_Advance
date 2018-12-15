# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 13:20
# @Author  : huangjie
# @File    : with_test.py


# try except finally
# try和return结合使用的时候，返回的值会压如到堆栈中，在最终返回的时候从堆栈中取出一个返回。
# 在这个例子中如果吧finally的return注释掉就会返回其他值。
def exe_try():
    try:
        print("code started")
        raise KeyError
        return 1
    except KeyError as e:
        print("Key error")
        return 2
    else:
        print("other error")
        return 3
    finally:
        print("finally")
        # return 4

# 上下文管理器协议
class Sample():
    def __enter__(self):
        print("enter")
        # 获取资源
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit")

    def do_something(self):
        print("doing something")


if __name__ == "__main__":
    result = exe_try()
    print(result)

    with Sample() as sample:
        sample.do_something()


