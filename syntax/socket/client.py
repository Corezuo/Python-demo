# -*- coding: utf-8 -*-

"""
客户端
"""

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 4000))
while True:
    msg = 'hello server！'
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print('recv:', data.decode())
client.close()

