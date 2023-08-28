#!/bin/python3
import sys
import dns
import dns.resolver
domain=sys.argv[1]
result = dns.resolver.resolve(domain, 'A')
for ipval in result:
    print('IP', ipval.to_text())
