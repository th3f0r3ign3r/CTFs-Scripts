#!/usr/bin/python3

def check(x):
    return pow(x,3) + 10 * pow(x,2) + x * 7 + 6

cipher = [317336, 1696274, 425598, 1007448, 1069008, 1340288, 346128, 663858, 392496,
          2013024, 734808, 1233758, 1268616, 1069008, 1233758, 948296, 142008, 1653936,
          948296, 516368, 133974, 1612308, 1133024, 948296, 392496, 1739328, 1452776, 948296,
          641264, 133974, 497274, 1783104, 1268616, 1452776, 1199544, 948296, 1531158, 133974,
          1377114, 1918824, 1452776, 133974, 1414608, 1268616, 1007448, 1377114, 1653936, 948296,
          556008, 619188, 948296, 1037924, 619188, 1739328, 1696274, 1133024, 392496, 133974, 1612308,
          1069008, 1268616, 1452776, 1199544, 290184, 47064, 2110256]

flag =  []

for a in cipher:
    for b in range(1,1000):
        if check(b) == a:
            flag.append(chr(b))

# print(flag)

plaintext = "".join(flag)

print(plaintext)

#! FLAG: AtHackCTF{Which_1s_M0re_Fun_S0Lving_p0lyn0mials_OR_bRuteF0rcing?!}