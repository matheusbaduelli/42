#!/usr/bin/env python3

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

lista = []

def average(pessoas):
    
    return sum(pessoas.values()) / len(pessoas)
    


print(average(class_3B))
print(average(class_3C))