#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message


print("\n\n****Extra request for Interface details*****")
name= input("Enter the Interface name: ")

interf = (netifaces.interfaces())

if name in interf:
    print((netifaces.ifaddresses(name)[netifaces.AF_LINK])[0]['addr'])
    print((netifaces.ifaddresses(name)[netifaces.AF_INET])[0]['addr'])

else: 
    print("Try again later")


