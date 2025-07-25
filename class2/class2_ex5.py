#!/usr/bin/env python

import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

'''5. On both the NXOS1 and NXOS2 switches configure five 
VLANs including VLAN names (just pick 5 VLAN numbers between 100 - 999).
Use Netmiko's send_config_from_file() method to accomplish this. 
Also use Netmiko's save_config() method to save the changes to the startup-config.
'''
nxos1 = { 
    "host" : 'nxos1.lasthop.io',
 #   "ssh_port" : 22,
    "username" : 'pyclass',
    "password" : getpass(),
     "device_type" : 'cisco_nxos',
    }
nxos2 = { 
    "host" : 'nxos2.lasthop.io',
#    "ssh_port" : 22,
    "username": 'pyclass',
    "password" : getpass(),
     "device_type" : 'cisco_nxos',
    }

for device in (nxos1,nxos2):
    net_connect = ConnectHandler(**device)
    with net_connect :
        print(net_connect.find_prompt())
        try:
            startTime = datetime.now()
            print(startTime)
            output = net_connect.send_config_from_file('class2/commands.txt')
   #        print(output)
            endTime = datetime.now() - startTime
            print(endTime)
    #       net_connect.disconnect()
            print(output)
            net_connect.save_config()
        except Exception as e:
            print(f"An error occurred: {e}")

net_connect.disconnect()