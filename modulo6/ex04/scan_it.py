#!/usr/bin/env python3

import sys
import re

argvs = sys.argv

if len(argvs) < 3:
    print("none")

else:
    
    keyword = sys.argv[1]
    text = sys.argv[2]


    matches = re.findall(re.escape(keyword),text)


    if not matches:
        print("none")

    print(len(matches))


        
