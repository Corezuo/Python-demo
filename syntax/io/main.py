# -*- coding: utf-8 -*-

"""
文件的读写操作
Created by zfh on 2018/11/19
"""

import os

# os模块的基本功能
print("操作系统类型：", os.name)
print("环境变量：", os.environ)
print("PATH: ", os.environ.get("PATH"))
print("脚本工作的路径：", os.getcwd())
# 运行shell命令
os.system("echo hello")

# 操作文件和目录
print("当前绝对路径：", os.path.abspath('.'))
path = os.path.join(os.path.abspath("."), "demo")
print("合并路径：", path)
# 创建目录
os.mkdir(path)
# 删除目录
os.rmdir(path)
# 新建文件
path = "F:/mypy/syntax/main2.py"
t = os.path.split(path)
print("拆分路径返回tuple: ", t)
print("文件扩展名：", os.path.splitext(path))

# 打开一个文件，若不存在则创建
open(path, 'w')
# 删除文件
os.remove(path)

# open("info.log", 'w')
fileSize = os.path.getsize("info.log")
print("文件大小: ", fileSize)

# 已读写模式打开
f = open("info.log", "a+")
# print("读取4个字节：", f.read(4))
print("读取一行：", f.readline())

# 写文件
f.write("\nhello world4")
f.close()
