# -*- coding: utf-8 -*-

import logging

#
"""
日志类

其中：
  level=logging.DEBUG：控制台打印的日志级别
  filemode：模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志 a是追加模式，默认如果不写的话，就是追加模式
"""
class Logger(object):

    __instance = None

    def __init__(self, log_file_name, log_level, logger_name):
        self.__logger = logging.getLogger(logger_name)

        # 指定日志的最低输出级别，默认为WARN级别
        self.__logger.setLevel(log_level)

        # 创建一个handler用于写入日志文件
        file_handler = logging.FileHandler(log_file_name)

        # 创建一个handler用于输出控制台
        console_handler = logging.StreamHandler()

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '[%(asctime)s] - [%(filename)s file line:%(lineno)d] - %(levelname)s: %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 给logger添加handler
        self.__logger.addHandler(file_handler)
        self.__logger.addHandler(console_handler)

    @classmethod
    def get_log(cls):
        if not cls.__instance:
            cls.__instance = Logger(log_file_name='common.log', log_level=logging.DEBUG, logger_name="test")
        return cls.__instance.__logger
