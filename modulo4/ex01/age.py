#!/usr/bin/env python3

idade_usuario = input("Por favor, me diga sua idade: ")

idade_usuario = int(idade_usuario)

print(f"Você tem atualmente {idade_usuario} anos de idade.")

contador = 2
i = 0

idade_usuario = idade_usuario + 10
contador_10 = 10
while i <= contador:
    
    print(f"Em {contador_10} anos, você terá {idade_usuario} anos de idade.")
    contador_10 += 10
    idade_usuario+=10
    i+=1