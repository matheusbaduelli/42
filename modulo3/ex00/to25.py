#!/usr/bin/env python3

user_numeric = int(input())

limit = 25

if user_numeric > limit:
    print("erro")
else:
   while user_numeric <= 25:
        print(f"Inside the loop my variable is {user_numeric}")
        user_numeric += 1




