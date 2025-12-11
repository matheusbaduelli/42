#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]

array_modificado = []

for i in array:
    if i > 5:
        array_modificado.append(i + 2)
print(f"Original array: {array}")
print(f"New array: {set(array_modificado)}")