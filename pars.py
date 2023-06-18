#!/bin/python3

import requests
from time import sleep 

url = str(input('[+] URL: '))

print("[*] sending requests response ")
sleep(2)
print("[*] sending requests response. ")
sleep(1)
print("[*] sending requests response.. ")
sleep(1)
print("[*] sending requests response... ")
sleep(1)
print("[OK] sending requests response  ")
sleep(1)
print("[+] data acquisition ")
sleep(2)
print("[+] data acquisition. ")
sleep(1)
print("[+] data acquisition.. ")
sleep(1)
print("[+] data acquisition... ")
sleep(1)
print("[OK]  data acquisition ")
sleep(1)
print("[+] data processing ")
sleep(1)
print("[+] data processing. ")
sleep(1)
print("[$_<]data processing.. ")
sleep(1)
print("[$_ ] data processing... ")
sleep(1)
print("[OK] data processing ")
sleep(1)
print("[OK] saving data ")
print('file name: result1\n')
print('Type: {txt}')
response = requests.get(url)

with open('result1.txt', 'w') as file:
     file.write(response.text)


# sending requests response = отправка запросов ответ
# data acquisition = получение данных
# data processing  = обработка данных
