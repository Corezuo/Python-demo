# -*- coding: utf-8 -*-

"""
管道

Pipe()函数返回一个由管道连接的连接对象，默认情况下是双工（双向）。返回的两个连接对象Pipe()表示管道的两端。
每个连接对象都有send()和recv()方法（相互之间的）。请注意，如果两个进程（或线程）同时尝试读取或写入管道的
同一端，则管道中的数据可能会损坏。当然，在不同进程中同时使用管道的不同端的情况下不存在损坏的风险。
"""

from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()


def run_process():
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()


if __name__ == '__main__':
    run_process()
