#!/usr/bin/python3

import argparse
from string import punctuation

punct = punctuation + "’ 1234567890"

parser = argparse.ArgumentParser(description="Substitution Cipher Decoder")
parser.add_argument('-d', metavar='String', type=str, help='Cipher Text')
parser.add_argument('-f', metavar='File', type=str, help='Cipher Text File')
parser.add_argument('-k', metavar='key', type=int, help='Substitute Number')
parser.add_argument('-r', metavar='range', type=str, help='Substitute Range')
args = parser.parse_args()

def cesear_gen(text_cipher, k=None, rang=None):
    print('[*] ' + text_cipher, end='\n\n')
    text_cipher = list(text_cipher.lower())

    if k == None and rang == None and len(text_cipher) != 0:
        for i in range(1, 26):
            text = []

            for t in text_cipher:
                if t in punct:
                    text.append(t)
                else:
                    text.append(norm.index(t)+i)

            for v in text:
                if str(v) in punct: pass
                else:
                    while v > 25:
                        text[text.index(v)] = v - 26
                        v-=26

            result = []

            for t in text:
                if type(t) == str and t in punct:
                    result.append(t)
                else:
                    while t > 25:
                        text[text.index(t)] = t - 26
                        t -= 26
                    result.append(norm[t])

            print('# ' + ''.join(result), end='\n\n')

    elif k != None and rang == None and len(text_cipher) != 0:
        text = []

        for t in text_cipher:
            if t in punct:
                text.append(t)
            else:
                text.append(norm.index(t)+k)

        for v in text:
            if str(v) in punct: pass
            else:
                while v > 25:
                    text[text.index(v)] = v - 26
                    v-=26

        result = []

        for t in text:
            if type(t) == str and t in punct:
                result.append(t)
            else:
                while t > 25:
                    text[text.index(t)] = t - 26
                    t -= 26
                result.append(norm[t])

        print('# ' + ''.join(result), end='\n\n')

    elif k == None and rang != None and len(text_cipher) != 0:
        rang = rang.split('-')

        for r in range(int(rang[0]), int(rang[1])+1):
            text = []

            for t in text_cipher:
                if t in punct:
                    text.append(t)
                else:
                    text.append(norm.index(t)+r)

            for v in text:
                if str(v) in punct:
                    pass
                else:
                    while v > 25:
                        text[text.index(v)] = v - 26
                        v -= 26

            result = []

            for t in text:
                if type(t) == str and t in punct:
                    result.append(t)
                else:
                    while t > 25:
                        text[text.index(t)] = t - 26
                        t -= 26
                    result.append(norm[t])

            print('# ' + ''.join(result), end='\n\n')
    else:
        print('Something went wrong !')

norm = list('abcdefghijklmnopqrstuvwxyz')

if args.d != None and args.k != None and args.f == None and args.r == None:
    cesear_gen(args.d, args.k)

elif args.d != None and args.f == None and args.k == None and args.r == None:
    cesear_gen(args.d)

elif args.f != None and args.k != None and args.d == None and args.r == None:
    with open(args.f, 'r') as file:
        lines = file.readlines()
        lines = ''.join(lines).replace('\n', '')
        cesear_gen(lines,args.k)

elif args.f != None and args.d == None and args.k == None and args.r == None:
    with open(args.f, 'r') as file:
        lines = file.readlines()
        lines = ''.join(lines).replace('\n', '')
        cesear_gen(lines)

elif args.f != None and args.k == None and args.r != None and args.d == None:
    with open(args.f, 'r') as file:
        lines = file.readlines()
        lines = ''.join(lines).replace('\n', '')
        cesear_gen(lines, rang=args.r)
        cesear_gen(lines)

elif args.f == None and args.k == None and args.r != None and args.d != None:
        cesear_gen(args.d, rang=args.r)
        
else:
    parser.print_help()
