# -*- coding: utf-8 -*-

"""
Pool对象

multiprocessing 模块引入了 Pool 对象，它提供了一种快捷的方法，赋予函数并行化处理一系列输入值的能力，
可以将输入数据分配给不同进程处理（数据并行）。
"""

from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
