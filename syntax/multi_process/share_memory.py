# -*- coding: utf-8 -*-

"""
共享内存

可以使用Value或Array将数据存储在共享内存映射中。
"""

from multiprocessing import Process, Value, Array


def f(n, a):
    n.value = 3.1415
    for i in range(len(a)):
        a[i] = -a[i]


def run_process():
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])


if __name__ == '__main__':
    run_process()
