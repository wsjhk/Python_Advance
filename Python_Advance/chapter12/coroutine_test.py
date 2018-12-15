# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 20:27
# @Author  : huangjie
# @File    : coroutine_test.py


def gen_func():
    # 1.可以产出值；2.可以接收值（调用方传递进来的值）
    html = yield "http://www.baidu.com"
    print(html)
    yield 2
    yield 3
    return "tom"

# 1.生成器不只可以产出值，还可以接收值
# 2.close和throw方法

if __name__ == "__main__":
    gen = gen_func()
    # 在调用send发送非None值之前，我们必须启动一次生成器，方式有两种：1.gen.send(None)，2.next()
    # url = gen.send(None)
    print(next(gen))
    # download url
    html = "tom"
    # send方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield
    # 1.启动生成器方式有两种：next(),send
    print(gen.send(html))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
