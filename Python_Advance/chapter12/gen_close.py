# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 20:40
# @Author  : huangjie
# @File    : gen_close.py


def gen_func():
    # 1.可以产出值；2.可以接收值（调用方传递进来的值）
    try:
        html = yield "http://www.baidu.com"
    except GeneratorExit as e:
        pass
    yield 2
    yield 3
    return "tom"

# 1.生成器不只可以产出值，还可以接收值
# 2.close和throw方法

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()
    print(next(gen))
    # GeneratorExit是继承BaseException, Exception