#!/usr/bin/env python3

import sys

argvs = sys.argv



def downcase_it(argumentos):
    if len(argumentos) == 1:
        print("none")

    else:
        lista_minuscula = [lista.lower() for lista in argumentos[1:]]

        for listagem in lista_minuscula:


            print(listagem)

downcase_it(argvs)