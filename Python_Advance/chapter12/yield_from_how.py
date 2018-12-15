# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 21:29
# @Author  : huangjie
# @File    : yield_from_how.py


# pep380

# 1.RESULT = yield from EXPR 可以简化成下面这样
# 一些说明：
"""
_i: 子生成器，同时也是一个迭代器
_y: 子生成器生产的值
_r: yield from 表达式最终的值
_s: 调用方通过send()发送的值
_e: 异常对象

yield from 的具体语义很难理解，尤其是处理异常的那两点。在PEP 380 中阐述了 yield from 的语义。
还使用伪代码（使用 Python 句法）演示了 yield from 的行为。
若想研究那段伪代码，最好将其简化，只涵盖 yield from 最基本且最常见的用法：yield from 出现在委派生成器中，
客户端代码驱动着委派生成器，而委派生成器驱动着子生成器。为了简化涉及到的逻辑，假设客户端没有在委派生成器上调用throw(...) 或 close() 方法。
而且假设子生成器不会抛出异常，而是一直运行到终止，让解释器抛出 StopIteration 异常。上面示例中的脚本就做了这些简化逻辑的假设。
下面的伪代码，等效于委派生成器中的 RESULT = yield from EXPR 语句（这里针对的是最简单的情况：不支持 .throw(...) 和 .close() 方法，
而且只处理 StopIteration 异常）：

"""
EXPR = list
def abc():
    _i = iter(EXPR) # EXPR是一个可迭代对象，_i其实是子生成器
    try:
        _y = next(_i)   # 预激子生成器，把产出的第一个值存在_y中
    except StopIteration as _e:
        _r = _e.value   # 如果抛出了StopIteration异常，那么就将异常对象的value保存在_r，这是最简单的情况的返回
    else:
        while 1:    # 尝试执行这个循环，委托生成器会阻塞
            _s = yield _y   # 生产子生成器的值，等待调用方send()值，发送过来的值保存到_s中
            try:
                _y = _i.send(_s)    # 转发_s，并且尝试向下执行
            except GeneratorExit as _e:
                _r = _e.value   # 如果子生成器抛出异常，那么就获取异常对象的value保存到_r，退出循环，恢复委托生成器
                break

    RESULT = _r # _r就是整个yield from表达式返回的值

"""
但是，现实情况要复杂一些，因为要处理客户对 throw(...) 和 close() 方法的调用，而这两个方法执行的操作必须传入子生成器。
此外，子生成器可能只是纯粹的迭代器，不支持 throw(...) 和 close() 方法，因此 yield from 结构的逻辑必须处理这种情况。
如果子生成器实现了这两个方法，而在子生成器内部，这两个方法都会触发异常抛出，这种情况也必须由 yield from 机制处理。
调用方可能会无缘无故地让子生成器自己抛出异常，实现 yield from 结构时也必须处理这种情况。
最后，为了优化，如果调用方调用 next(...) 函数或 .send(None) 方法，都要转交职责，在子生成器上调用next(...) 函数；
仅当调用方发送的值不是 None 时，才使用子生成器的 .send(...) 方法。
下面的伪代码，是考虑了上述情况之后，语句：RESULT = yield from EXPR的等效代码：
"""
def abc_2():
    _i = iter(EXPR)
    try:
        _y = next(_i)
    except StopIteration as _e:
        _r = _e.value
    else:
        while 1:
            try:
                _s = yield _y
            except GeneratorExit as _e:
                try:
                    _m = _i.close
                except AttributeError:
                    pass
                else:
                    _m()
                raise _e
            except BaseException as _e:
                _x = sys.exc_info()
                try:
                    _m = _i.throw
                except AttributeError:
                    raise _e
                else:
                    try:
                        _y = _m(*_x)
                    except StopIteration as _e:
                        _r = _e.value
                        break
            else:
                try:
                    if _s is None:
                        _y = next(_i)
                    else:
                        _y = _i.send(_s)
                except StopIteration as _e:
                    _r = _e.value
                    break
    RESULT = _r

