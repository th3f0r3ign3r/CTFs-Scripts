#!/usr/bin/python3

from sys import argv
from Crypto.Util.number import long_to_bytes

with open(argv[1]) as cipher:
    xn = cipher.read().strip('[]').split(', ')
    
for i in xn:
    try:
        print(long_to_bytes(int(i) ))
    except:
        pass
    #     print(long_to_bytes(int(i)).decode())