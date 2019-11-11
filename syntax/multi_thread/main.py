# -*- coding: utf-8 -*-

"""
多线程

Python2标准库中提供了两个模块支持多线程，thread和threading。其中，threading是对thread的封装，
thread有一些缺点在threading有了补充；在Python3中推荐直接使用threading，
"""

import threading


# 为线程定义一个函数
import time


def task(thread_name):
    time.sleep(3)
    print("thread_name %s" % thread_name)


t = threading.Thread(target=task("thread1"))
t.start()


