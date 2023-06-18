#!/bin/python3

import scapy.all as scapy
#import scapy.layers.http 
print('Protokols: ARP, TCP, IP, или  None')
wifi = str(input('Your wifi addapter: '))
pr = str(input('Protokol:  '))
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=ps, filter=pr)



def ps(packet):    
    print(packet)


sniff(wifi)






