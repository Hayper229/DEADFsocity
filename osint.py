#!/bin/python3

import socket
print('www.example.com/ example.com')
host = input('Domain: ')
re = f'Hostname: {host}\nIP address: {socket.gethostbyname(host)}'
print(re)

