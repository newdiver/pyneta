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
cisco3 = {          #(Cisco IOS-XE)
    "host": 'cisco3.lasthop.io',
    "snmp_port": 161,
    "ssh_port": 22,
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
}
command = 'delete flash:/sample.txt'
    net_connection = ConnectHandler(**cisco3)
    
    # print the router prompt back from this device to verify you are connecting to the device properly.
    print(net_connection.find_prompt())
    net_connection.send_command(command, expect_string=r'confirm') 
    net_connection.send_command('y', expect_string=r'#')
    
    

    
