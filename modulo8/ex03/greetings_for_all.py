#!/usr/bin/env python3



def greetings(nome):
    if type(nome) == int:
        print("Error! It was not a name.")
    elif len(nome) == 0:
        print("hello, noble stranger.")
    else:
        
        print(f"hello, {nome}")
        

greetings("Alexandra")
greetings("wil")
greetings("")
greetings(42)
