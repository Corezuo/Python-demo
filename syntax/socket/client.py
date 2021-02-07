# -*- coding: utf-8 -*-

"""
客户端
"""

import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(('localhost', 8009))

if __name__ == '__main__':
    while True:
        inp = input('place input:')
        sk.send(inp.encode('utf-8'))
        if inp == 'exit':
            break
    sk.close()

