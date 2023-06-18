#!/bin/python3
import requests
from threading import Thread
import os
from colorama import init
init()
from colorama import Fore, Back, Style

#print(Style.BRIGHT + 



print(Fore.GREEN + '''

 ____  _____    _    ____  _____               _ _
|  _ \| ____|  / \  |  _ \|  ___|__  ___   ___(_) |_ _   _
| | | |  _|   / _ \ | | | | |_ / __|/ _ \ / __| | __| | | |
| |_| | |___ / ___ \| |_| |  _|\__ \ (_) | (__| | |_| |_| |
|____/|_____/_/   \_\____/|_|  |___/\___/ \___|_|\__|\__, |
                                                     |___/
''')
print('''[+] 1 Dos Requests response on tls 1-3 and http
[+] 2 DosFlood http, https 
[+] 3 TCPDosFlood http, https
[+] 4 source ip address site 
[+] 5 Sniffer 
[+] 6 Scanner 
[+] 7 Parser
[+] 8 PNum
[+] 9 SlowLoris 
''')


a = int(input('Enter: '))

if a == 1:
  os.system('./Rdos.py')
if a == 2:
    os.system('./DosFM.py')
if a == 3:
   os.system('./TCPflood.py')
if a == 4:
    os.system('./osint.py')
if a == 5:
    os.system('./sniff.py')
if a == 6:
    os.system('./scanner.py')
if a == 7:
    os.system('./pars.py')
if a == 8:
    os.system('./ph.py')
if a == 9:
   ip = input('IP: ')
   sock = input('Sockets: ')
if a == 9:
    os.system('python3 SlowLoris.py  ' + ip + ' -s  ' + sock)
if a > 9:
    print('[!] Selection Error')
