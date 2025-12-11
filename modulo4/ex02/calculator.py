#!/usr/bin/env python3

primeiro_numero = input("Me dê o primeiro número: ")
segundo_numero = input("Me dê o segundo número: ")
print("Obrigado!")

primeiro_numero = int(primeiro_numero)
segundo_numero = int(segundo_numero)

divisao = primeiro_numero / segundo_numero

divisao = int(divisao)

print(f"{primeiro_numero} + {segundo_numero} = {primeiro_numero + segundo_numero}")
print(f"{primeiro_numero} - {segundo_numero} = {primeiro_numero - segundo_numero}")
print(f"{primeiro_numero} / {segundo_numero} = {divisao}")
print(f"{primeiro_numero} * {segundo_numero} = {primeiro_numero * segundo_numero}")