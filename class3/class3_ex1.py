#!/usr/bin/env python

import re
from pprint import pprint


'''
1. Using the below ARP data, create a five element list. Each list element should be 
a dictionary with the following keys: "mac_addr", "ip_addr", "interface". At the end of this process, 
you should have five dictionaries contained inside a single list.

Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
'''

arp_data = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

arp_processed_list = []

for arp_entry in arp_data:
    if re.search(r"Protocol.*Interface", arp_entry):
        continue
        _, ip_addr, _, mac_addr, _, intf= arp_entry.split()
        arp_dict = {"mac_addr": mac_addr, "ip_addr": ip_addr, "interface": intf}
        arp_processed_list.append(arp_dict)
    
    print("*" * 80)
    pprint(arp_processed_list)
    print("*" * 80)
