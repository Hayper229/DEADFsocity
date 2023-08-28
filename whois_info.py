#!/bin/python3

import whois
dom=input('[*] url or domain: ')
whois_info=whois.whois(dom)

print(whois_info)
print("Creation date")
print(whois_info["creation_date"])
