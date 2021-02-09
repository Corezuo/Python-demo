# -*- coding: utf-8 -*-

import threading

"""
线程锁

"""

balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(1000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


if __name__ == '__main__':
    run_thread(10)
    print(balance)
