#!/usr/bin/

from base64 import b64decode

plaintext = "aHR0cHM6Ly9tZWdhLm56L2ZpbGUvb0U5Rm5ZS1kjVmZ%Qjd@QzdzVkNTVE14ZUhxaTdfRH#OVWhVSG5TXz$meXN2c0t&WHBOMA=="

w = ['l', 'I']

for a in w:
    for b in w:
        for c in w:
            for d in w:
                for e in w:
                    result = plaintext.replace('%', e).replace('@', d).replace('#', c).replace('$', b).replace('&', a)
                    print(b64decode(result).decode())

# for i in w:
#     print(plaintext.replace('%', i))

#! GOOD : https://mega.nz/file/oE9FnYKY#VfHB7HC7sVCSTMxeHqi7_DyNUhUHnS_9fysvsKHXpN0
#? BASE64 : aHR0cHM6Ly9tZWdhLm56L2ZpbGUvb0U5Rm5ZS1kjVmZIQjdIQzdzVkNTVE14ZUhxaTdfRHlOVWhVSG5TXzlmeXN2c0tIWHBOMA==