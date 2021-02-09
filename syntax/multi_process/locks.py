# -*- coding: utf-8 -*-

""""
进程间同步-锁

对于所有在threading存在的同步原语，multiprocessing中都有类似的等价物。
"""

from multiprocessing import Process, Lock


def f(lock, i):
    lock.acquire()
    try:
        print('hello world', i)
    finally:
        lock.release()


def run_process():
    lock = Lock()
    for num in range(10):
        Process(target=f, args=(lock, num)).start()


if __name__ == '__main__':
    run_process()
