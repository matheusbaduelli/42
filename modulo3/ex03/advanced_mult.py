#!/usr/bin/env python3


contador1 = 0

while contador1 <=10:
    print()
    print(f"table of {contador1}:",end=' ')
    

    contador2 = 0
    while contador2 <=10:
        print(contador1 * contador2,end=' ')
        contador2 += 1
    contador1 += 1