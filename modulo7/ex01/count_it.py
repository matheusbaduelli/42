#!/usr/bin/env python3

import sys


argvs = sys.argv

if len(sys.argv) == 1:
    print("none")

else:

    
    text_len = len(argvs) -1

    print(f"parameters: {text_len}")



    for i in argvs[1:]:
        print(f"{i} : {len(i)}")
