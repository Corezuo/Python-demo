# -*- coding: utf-8 -*-

"""
队列

Queue 类是一个近似 queue.Queue 的克隆，支持进程之间的通信。
"""

from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, 'hello'])


def run_process():
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()


if __name__ == '__main__':
    run_process()
