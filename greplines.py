#!/usr/bin/python3

#! Passord Special Char :  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

from re import *
from sys import argv

pattern = r"^[\w!\"# $%&'()*+,-./:;<=>?@[\]^_`{|}~]"

with open(argv[1]) as wordlist:
    lines = wordlist.readlines()
    # print(lines)
    for line in lines:
        line = line.strip('\n')
        # print('Hello ' + line)
        if len(line) == 45:
            print(line)
            # result = match(pattern, line)
            # if result:
            #     print(line)
        else:
            pass

#? Final Passord : uqHQKFPU%1_<=&MCD'\%4c8%LaiC>A/_9d)3&1!!U5oOs6-U
