# -*- coding: utf-8 -*-

"""
TCP Server

ThreadingTCPServer实现的Socket服务器内部会为每个client创建一个 “线程”，该线程用来和客户端进行交互。
"""

from socketserver import ThreadingTCPServer
from socketserver import BaseRequestHandler


class ProxyServer(BaseRequestHandler):

    def handle(self):
        conn = self.request
        while True:
            try:
                data = conn.recv(1024)
                print('receive:', data.decode())
                conn.send(data.upper())
            except ConnectionResetError as e:
                print('关闭了正在占线的链接！')
                break


if __name__ == '__main__':
    server = ThreadingTCPServer(('127.0.0.1', 8009), ProxyServer)
    server.serve_forever()
