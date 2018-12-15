# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 17:58
# @Author  : huangjie
# @File    : progress_queue.py


from multiprocessing import Process, Queue, Pool, Manager, Pipe
# import time
#
# # 共享变量不适用于多进程中
# # multiprocessing中的Queue不能用于Pool进程池
# # Pool中的进程间通信需要使用Manager中的Queue
#
# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
# if __name__ == "__main__":
#     queue = Queue(10)
#     # queue = Manager().Queue(10)
#     # pool = Pool(2)
#     # pool.apply_async(producer, args=(queue,))
#     # pool.apply_async(consumer, args=(queue,))
#     # pool.close()
#     # pool.join()
#
#     my_producer = Process(target=producer, args=(queue, ))
#     my_consumer = Process(target=consumer, args=(queue, ))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()

# 通过pipe实现进程间通信
# pipe性能高于queue
def producer(pipe):
    pipe.send("aaa")

def consumer(pipe):
    print(pipe.recv())

if __name__ == "__main__":
    recevie_pipe, send_pipe = Pipe()
    # pip只能使用于两个进程
    my_producer = Process(target=producer, args=(send_pipe,))
    my_consumer = Process(target=consumer, args=(recevie_pipe,))

    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()
