#!/usr/bin/python3

from factordb.factordb import FactorDB
import gmpy2

c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e = 65537

f = FactorDB(n)
f.connect()
p, q = f.get_factor_list()
ph = (p-1)*(q-1)
d = gmpy2.invert(e, ph)
plaintext = pow(c, d, n)
print("Flag: {}".format(bytearray.fromhex(format(plaintext, 'x')).decode()))
