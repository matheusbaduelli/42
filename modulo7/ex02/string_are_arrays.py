#!/usr/bin/env python3

import sys
import re

argvs = sys.argv


if len(argvs) == 1:
    print("none")

else:

        
    keyword = "z"
    text = sys.argv[1]


    matches = re.findall(re.escape(keyword),text)

    if not matches:
        print("none")
    else:
        print(keyword * len(matches))
