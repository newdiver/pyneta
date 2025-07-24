#!/usr/bin/env python
'''
 In your lab environment, there is a file located at ~/.netmiko.yml.
 This file contains all of the devices used in the lab. Create a Python 
 program that processes this YAML file and then uses Netmiko to connect 
 to the Cisco3 router. Print out the router prompt from this device.

Note, the device dictionaries in the .netmiko.yml file use key-value 
pairs designed to work directly with Netmiko. The .netmiko.yml also 
contains group definitions for: cisco, arista, juniper, and nxos groups.
These group definitions are lists of devices. Once again, don't check the .netmiko.yml into GitHub'''

filename = "../.netmiko.yml"

with open(filename, "w") as file:
    netdevices = yaml.safe_load(file, default_flow_style=False, sort_keys=False)
print(netdevices)

