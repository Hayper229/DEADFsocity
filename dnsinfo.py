#!/bin/python3

import dns
import dns.resolver
domain=input('[*] Domain: ')
result = dns.resolver.resolve(domain, 'A')
for ipval in result:
    print('IP', ipval.to_text())
