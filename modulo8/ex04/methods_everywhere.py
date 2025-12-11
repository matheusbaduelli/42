#!/usr/bin/env python3

import sys


argvs = sys.argv





def shrink(strings):
    caracteres = strings[1:]
    for letras in caracteres:
        if len(letras) > 7:
            print(letras[:8])


def enlarge(strings):
    caracteres = strings[1:]
    for letras in caracteres:
        if len(letras) < 7:
            total = 8
            texto = letras + "z" * total
            print(texto[:8])

def funcoes(argvs):
    if len(argvs) == 1:
        print("none")
    else:
        shrink(argvs)
        enlarge(argvs)

funcoes(argvs)