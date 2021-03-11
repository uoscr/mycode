#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

print("Resources in "+ farms[0]["name"], ":")
for animals in farms[0]["agriculture"]:
    print(animals)


print("Resources in "+ farms[1]["name"], ":")
for animals in farms[1]["agriculture"]:
    print(animals)


print("Resources in "+ farms[2]["name"], ":")
for animals in farms[2]["agriculture"]:
    print(animals)
