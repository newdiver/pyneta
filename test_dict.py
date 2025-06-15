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
device1 = {
    'host': 'nxos1.lasthop.io', 
    'username': 'pyclass', 
    'password': getpass(), 
    'device_type': 'cisco_nxos',
   # 'session_log':'my_session.txt',
    }
net_connection = ConnectHandler(**device1)
print(net_connection.find_prompt())

    
