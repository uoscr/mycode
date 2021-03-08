#!/usr/bin/env python3
icecream = ["flavors","salty"]
name = input("enter your name: ")
icecream.append(99)

print(icecream[2], icecream[0] , icecream[1]) 

print(icecream[2], icecream[0], "and "+ name, "chooses to be "+ icecream[1])

print(f"{icecream[2]} {icecream[0]}, and {name} chooses to be {icecream[1]}.")
