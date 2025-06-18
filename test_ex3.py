#!/usr/bin/env python
'''
 For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'. 
 Save this output to a file in the current working directory.
'''
import os 
from netmiko import ConnectHandler
from getpass import getpass

'''
cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.10',
    'username': 'test',
    'password': 'password',
    'port' : 8022,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}
'''
cisco3 = {
    'device_type': 'cisco_ios',
    'hostname' : 'cisco3.lasthop.io',
    'username': 'test',
    'password': 'password',
    'port' : 8022,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}
net_connection = ConnectHandler(**cisco3)
    # print the router prompt back from this device to verify you are connecting to the device properly.
print(net_connection.find_prompt())
   # send_command() method to retrieve 'show version'  
output= net_connection.send_command('show version')    
print(output)

with open("show_version.txt", "w") as file:
       file.write(output)
file.close
    
