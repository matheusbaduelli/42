#!/usr/bin/env python3

import sys


argvs = sys.argv

tamanho = len(argvs)


if tamanho > 1:

    argumento = sys.argv[1]
    print(argumento.upper())
else:
    print("none")
