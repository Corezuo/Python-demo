# -*- coding: utf-8 -*-

"""
多线程

Python2标准库中提供了两个模块支持多线程，thread和threading。其中，threading是对thread的封装，
thread有一些缺点在threading有了补充；在Python3中推荐直接使用threading。

GIL锁：在解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得锁，
然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行
代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程泡在100核CPU上，也只能用到1核。

Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。
"""

import threading
import time


def task(thread_name):
    time.sleep(3)
    print("thread_name %s" % thread_name)


if __name__ == '__main__':
    t = threading.Thread(target=task("thread1"))
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
