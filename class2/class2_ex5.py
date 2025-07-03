#!/usr/bin/env python

import os
from netmiko import ConnectHandler
from getpass import getpass

'''5. On both the NXOS1 and NXOS2 switches configure five 
VLANs including VLAN names (just pick 5 VLAN numbers between 100 - 999).
Use Netmiko's send_config_from_file() method to accomplish this. 
Also use Netmiko's save_config() method to save the changes to the startup-config.
'''

net_connect = ConnectHandler(**cisco3, fast_cli = False)
with net_connect :
    print(net_connect.find_prompt())
    try:
        startTime = datetime.now()
        print(startTime)
        output = net_connect.send_config_from_file(commands.txt)
   #     print(output)
        endTime = datetime.now() - startTime
        print(endTime)
    #    net_connect.disconnect()
        print(output)
    except Exception as e:
        print(f"An error occurred: {e}")

net_connect.disconnect()