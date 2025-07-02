#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime


'''
Use Netmiko and the send_config_set() method to configure the following on the Cisco3 router.

ip name-server 1.1.1.1
ip name-server 1.0.0.1
ip domain-lookup

Experiment with /fast_cli=True to see how long the script takes to execute (with and without this option enabled). 
In both cases, explicitly set fast_cli (i.e. first set fast_cli=False and then set fast_cli=True, 
the Netmiko defaults for fast_cli have changed across time).

Verify DNS lookups on the router are now working by executing 'ping google.com'. Verify from this that you receive a ping response back.

'''

cisco3 = { #(Cisco IOS-XE)
    "host" : 'cisco3.lasthop.io',
    "username" : 'pyclass',
    "password" : getpass(),
    "device_type": 'cisco_ios'
    }

commands = [
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup",
    "exit",
]
net_connect = ConnectHandler(**cisco3)
with net_connect :
    print(net_connect.find_prompt())
    try:
        startTime = datetime.now()
        output = net_connect.send_config_set(commands, fast_cli = False)
        
        net_connect.disconnect()

        print(output)
    except Exception as e:
        print(f"An error occurred: {e}")

        net_connect.disconnect()