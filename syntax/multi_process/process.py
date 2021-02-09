# -*- coding: utf-8 -*-

"""
多进程

multiprocessing 是一个支持使用与 threading 模块类似的API来产生进程的包。
文档：https://docs.python.org/zh-cn/3.8/library/multiprocessing.html
"""

from multiprocessing import Process
import os
import time


def info(title):
    print(title)
    print('module_name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('mars',), daemon=True)
    p.start()
    # 可选参数timeout的默认值None，则该方法将阻塞，直到调用join()方法的进程终止
    p.join()
