#!/usr/bin/python3

cipher = "112 105 99 111 67 84 70 123 103 48 48 100 95 107 49 116 116 121 33 95 110 49 99 51 95 107 49 116 116 121 33 95 57 98 51 98 55 51 57 50 125 10"
cipher = cipher.split(' ')

# print(cipher)

for x in cipher:
    print(chr(int(x)), end='')


# def dead(why):
#     print(why, "╭∩╮（︶︿︶） Your'e dead ╭∩╮")
#     exit(0)