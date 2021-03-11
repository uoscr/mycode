#!/usr/bin/python3

#defining pizza options and toppings
predef = ["Pepperoni","Ham & cheesse", "Veggetarian"]
topping = ["olives","anchovies","pineapple","ham","peppers"]
option = ["light on cheesse", "double cheesse", "light on sauce"]

#welcome screen for clien
name = input("Hi, What is your name? ")
print("Hello,", name +" Welcome to our online pizza menu!")

#Question for choosing Predefined pizza or custom build
print('Pick on of the following options: 1)Predefined options 2)Build your own')
pick = input("Enter your option: ")

if pick == "1": 
	print(f"Aavailble options are: 1) {predef[0]} 2) {predef[1]} 3) {predef[2]}")
	order = input("Enter your option")
        if order == "1": 
		print(f"Thank you for your order, you have ordered {predef[0].upper()} Pizza")
        if order == "2" :
		print(f"Thank you for your order, you have ordered {predef[1].upper()} Pizza")
        if order == "3": 
		print(f"Thank you for your order, you have ordered {predef[2].upper()} Pizza")

if pick == "2": 
	print(f"Aavailble options are: 1) {topping[0]} 2) {topping[1]} 3) {topping[2]} 4) {topping[3]}")
	toppa = input("Enter your first topping: ") 
	toppb = input("Enter your 2nd topping: ")
	print(f"pink your style: 1) {option[0]} 2) {option[1]} 3) {option[2]}")

