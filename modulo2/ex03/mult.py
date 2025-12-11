#!/usr/bin/env python3


number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

result = int(number1) * int(number2)

if result > 0:
    print(f"{number1} x {number2} = {result}")
    print("the result is positive")
elif result < 0:
    print(f"{number1} x {number2} = {result}")
    print("the result is negative")
else:
    print(f"{number1} x {number2} = {result}")
    print("the result is positive and negative")

