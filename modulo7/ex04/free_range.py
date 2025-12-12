#!/usr/bin/env python3

import sys


argvs = sys.argv

lista = []



if len(argvs) != 3:
    print("none")

else:
    primeiro_index = argvs[1]
    segundo_index = argvs[-1]
    if primeiro_index > segundo_index:
        print("none")
    else:

        for i in range(int(primeiro_index),int(segundo_index)+1):
            lista.append(i)
        print(lista)