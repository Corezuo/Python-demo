# -*- coding: utf-8 -*-

"""
工作进程池

multiprocessing 模块引入了 Pool 对象，它允许以不同的方式将任务分配到工作进程的方法。
"""

from multiprocessing import Pool
from multiprocessing.context import TimeoutError
import os
import time


def f(x):
    return x * x


def run_process():
    with Pool(processes=5) as p:
        print(p.map(f, [1, 2, 3]))

        # evaluate "f(20)" asynchronously
        res = p.apply_async(f, (20,))
        print(res.get(timeout=1))

        # evaluate "f(20)" asynchronously
        res = p.apply_async(os.getpid, ())
        print(res.get(timeout=1))

        # make a single worker sleep for 10 secs
        res = p.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=3))
        except TimeoutError:
            print("got a multiprocessing.TimeoutError")


if __name__ == '__main__':
    run_process()
