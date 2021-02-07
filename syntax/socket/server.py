# -*- coding: utf-8 -*-

"""
服务端
"""
import socket

server = socket.socket()
server.bind(('127.0.0.1', 4000))

# 开始监听 表示可以使用五个链接排队
server.listen(5)
while True:
    conn, addr = server.accept()
    print(conn, addr)
    while True:
        try:
            data = conn.recv(1024)
            print('receive:', data.decode())
            conn.send(data.upper())
        except ConnectionResetError as e:
            print('关闭了正在占线的链接！')
            break
    conn.close()
