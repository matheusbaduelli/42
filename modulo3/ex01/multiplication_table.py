#!/usr/bin/env python3


number_user =  input("Enter a number: ")

i = 0

while i < 10:
    result = int(number_user) * int(i)
    print(f"{i} * {number_user} = {result}") 
    i+=1