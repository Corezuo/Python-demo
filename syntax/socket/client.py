# -*- coding: utf-8 -*-

"""
客户端
"""

import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(('localhost', 4000))

if __name__ == '__main__':
    while True:
        inp = input('place input: ')
        sk.send(inp.encode('utf-8'))

        data = sk.recv(1024)
        print('recv:', data.decode())
        if inp == 'exit':
            break
    sk.close()
