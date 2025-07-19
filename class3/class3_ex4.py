#!/usr/bin/env python
'''
From a file, read this JSON data into your Python program. Process this ARP data 
and return a dictionary where the dictionary keys are the IP addresses and the 
dictionary values are the MAC addresses. Print this dictionary to standard output.
'''

import json
from pprint import pprint

filename = "class3/arista.json"
with open(filename) as f:
    arp_data = json.load(f)

arp_dict = {}
arp_entries = arp_data["ipV4Neighbors"]
for entry in arp_entries:
    ip_addr = entry["address"]
    mac_addr = entry["hwAddress"]
    arp_dict[ip_addr] = mac_addr

print()
pprint(arp_dict)
print()