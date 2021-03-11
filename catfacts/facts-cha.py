#!/usr/bin/env python3

# imports always go at the top of your code
import requests




def methods():
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    for catfact in r.json():
        print(catfact.get("text"))
        print("Created by: ", catfact.get("user") + " \nOn", catfact.get("createdAt")+"\n")


methods()
