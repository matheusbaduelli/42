#!/usr/bin/env python3


import sys
args = sys.argv[1:]

if not args:
    print("none")


for word in args:
    if word.find("ism", max(0,len(word)-3)) !=-1:
        continue
    print(word + "ism")

