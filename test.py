from Crypto.Random import random
from Crypto.Util.number import bytes_to_long

FLAG = b'CTFae{}'


def get_padding():
    seed = 256
    e = random.randint(2, 2**2024)
    return e


m = bytes_to_long(FLAG)

padd = []
while m:
    padding = get_padding()
    me = (padding << 1) + (m % 2)
    padd.append(me)
    m //= 2
print(padd)
