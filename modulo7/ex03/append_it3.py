#!/usr/bin/env python3


import sys


argvs = sys.argv

listagem = []
listagem1 = []
listagem3 = []
if len(argvs) == 1:
    print("none")

else:

        
    keyword = "ism"

    for texto in argvs:
        listagem.append(texto)

for palavra in listagem[1:]:
    if keyword in palavra:
        listagem1.append(palavra)

lista1 = set(listagem[1:])
lista2 = set(listagem1)

valores_nao_repetidos = lista1 ^ lista2

for palavra_sem_repeticao in valores_nao_repetidos:
    print(palavra_sem_repeticao + keyword)









