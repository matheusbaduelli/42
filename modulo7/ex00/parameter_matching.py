#!/usr/bin/env python3

import sys


argvs = sys.argv


if len(sys.argv) == 1:
    print("none")

else:

    
    text = sys.argv[1]

    text2 = input("What was the parameter? ")

    if text == text2:
        print("Good job!")
    else:
        print("Nope, sorry...")



