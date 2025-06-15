#!/usr/bin/env python

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
# build a dictionary to hold the device connection information
device1 = {
    'host': 'nxos1.lasthop.io', 
    'username': 'pyclass', 
    'password': getpass(), 
    'device_type': 'cisco_nxos',
   # 'session_log':'my_session.txt',
    }
device2 = {  'host': 'nxos2.lasthop.io', 
    'username': 'pyclass', 
    'password': getpass(), 
    'device_type': 'cisco_nxos',
   # 'session_log':'my_session.txt',
    
}
# loop through the devices to conmmunicate with them.
for device in range(device1, device2):
    net_connection = ConnectHandler(**device)
    # print the router prompt back from this device to verify you are connecting to the device properly.
    print(net_connection.find_prompt())
    if device == device2:
  # send_command() method to retrieve 'show version'  
        output= netconnection.send_command('show version')    
        print(output)

    
