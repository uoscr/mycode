#!/usr/bin/env python3
#new list 
my_list = [ "192.168.0.5", 5060, "UP" ]
#printing the IP
print("The first item in the list (IP): " + my_list[0] )
#printing the port number
print("The second item in the list (port): " + str(my_list[1]) )
#printing interface status
print("The last item in the list (state): " + my_list[2] )

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#new line for printing with the new values 
print("When I " + new_list[-1] , "into Iaddress" + new_list[3] , "or" + new_list[4])
print("I am unable to ping ports " + new_list[1] ,"&"+ str(new_list[2]))


#print(f"When I {new_list[5]} into IP addresses {new_list[3]} or {new_list[4]} I am unable to ping ports {new_list[0]}, {new_list[1]}, {new_list[2]}")
