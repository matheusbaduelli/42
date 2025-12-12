#!/usr/bin/env python3

import sys

argvs = sys.argv

if len(argvs) < 3: 
    print("none")
else:    
    for arg in reversed(argvs[1:]):
        print(arg)


