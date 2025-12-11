#!/usr/bin/env python3


pessoas = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}


lista = []

def array_de_nomes(pessoas):




    for chave, valor in pessoas.items():

        chave = chave.capitalize()
        valor = valor.capitalize()

        
        concatenado = f"{chave} {valor}"

        lista.append(concatenado)

    return lista



print(array_de_nomes(pessoas))
