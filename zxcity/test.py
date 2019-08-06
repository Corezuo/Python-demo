# -*- coding: utf-8 -*-

import logging

#
"""
日志配置

其中：
  level=logging.DEBUG：控制台打印的日志级别
  filemode：模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志 a是追加模式，默认如果不写的话，就是追加模式
"""
logging.basicConfig(level=logging.DEBUG,
                    filename='common.log',
                    filemode='a',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

if __name__ == '__main__':
    logging.info("info message")

