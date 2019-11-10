# -*- coding: utf-8 -*-

"""
自定义异常，继承异常基类 RuntimeError
"""


class CustomError(RuntimeError):
    def __init__(self, *arg):
        self.args = arg
