# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 16:17
# @Author  : huangjie
# @File    : thread_condition.py

import threading

# 条件变量，用于复杂的线程同步
# class XiaoAi(threading.Thread):
#     def __init__(self, lock):
#         super(XiaoAi, self).__init__(name="小爱")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print ("{} : 在".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print ("{} : 好啊".format(self.name))
#         self.lock.release()
#
#
# class TianMao(threading.Thread):
#     def __init__(self, lock):
#         super(TianMao, self).__init__(name="天猫精灵")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print ("{} : 小爱同学".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print ("{} : 我们来对故事吧".format(self.name))
#         self.lock.release()

# 通过condition完成协同读诗
from threading import Condition
class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super(XiaoAi, self).__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:# 或者使用self.cond.acquire()和self.cond.release()
            self.cond.wait()
            print ("{} : 在".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print ("{} : 好啊".format(self.name))
            self.cond.notify()



class TianMao(threading.Thread):
    def __init__(self, cond):
        super(TianMao, self).__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        with self.cond: # 或者使用self.cond.acquire()和self.cond.release()
            print ("{} : 小爱同学".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print ("{} : 我们来对故事吧".format(self.name))
            self.cond.notify()
            self.cond.wait()

if __name__ == "__main__":
    cond = Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    # 1.启动顺序很重要
    # 2.在调用with cond之后才能调用wait或者notify方法
    # 3.condition有两层锁，一把底层锁会在线程调用了wait方法的时候释放，
    # 上面的锁会在每次调用wait的时候分配一把并放入到cond的等待队列中，等待notify方法的唤醒。
    xiaoai.start()
    tianmao.start()

