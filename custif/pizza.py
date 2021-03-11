#!/usr/bin/python3

#defining pizza options and toppings
predef = ["Pepperoni","Ham & cheesse", "Veggetarian"]
topping = ["olives","anchovies","pineapple","ham","peppers"]
option = ["light on cheesse", "double cheesse", "light on sauce"]

#welcome screen for clien
name = input("Hi, What is your name? ")
print("Hello,", name +" Welcome to our online pizza menu!")

#Question for choosing Predefined pizza or custom build
print('Pick on of the following options: a)Predefined options b)Build your own')
pick = input("Enter your option: ")

if pick == "a": 
    print(f"Aavailble options are: a) {predef[0]} b) {predef[1]} c) {predef[2]}")
    order= input("Enter your option: ")
    if order == "a" :
        print(f"Thank you for your order, you have ordered {predef[0].upper()} Pizza")
    if order == "b" :
        print(f"Thank you for your order, you have ordered {predef[1].upper()} Pizza")
    if order == "c" :
        print(f"Thank you for your order, you have ordered {predef[2].upper()} Pizza")
    #if order == "a" or order == "b" or order == "c" :
    #   print(f"Thank you for your order, you have ordered {order.upper()} Pizza")


else:
    print("Thank you for your, we did not get your order")

