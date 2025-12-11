#!/usr/bin/env python3

import sys


argvs = sys.argv

tamanho = len(argvs)


if tamanho > 1:
    print(sys.argv[1])
else:
    print("none")

