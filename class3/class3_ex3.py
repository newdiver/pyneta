#!/usr/bin/env python
'''
3. NAPALM using nxos_ssh has the following data structure in one of its unit tests (the below data is in JSON format). 

Read this JSON data in from a file.

From this data structure extract all of the IPv4 and IPv6 addresses that are used on this NXOS device. From this data create two lists: 'ipv4_list' and 'ipv6_list'. The 'ipv4_list' should be a list of all of the IPv4 addresses including prefixes; the 'ipv6_list' should be a list of all of the IPv6 addresses including prefixes.

'''

import json


filename = "class3/nxos.json"

ipv4_list = []
ipv6_list = []

with open(filename) as f:
    nxos_data = json.load(f)
    for intf, ip_addr_dict in nxos_data.items():
        for ipv4_or_ipv6, address_info in ip_addr_dict.items():
            for ip_addr, prefix_dict in address_info.items():
                prefix_length = prefix_dict["prefix_length"]
                if ipv4_or_ipv6 == "ipv4":
                    ipv4_list.append("{}/{}".format(ip_addr, prefix_length))
                elif ipv4_or_ipv6 == "ipv6":
                    ipv6_list.append("{}/{}".format(ip_addr, prefix_length))


print("\nIPv4 Addresses: {}\n".format(ipv4_list))
print("\nIPv6 Addresses: {}\n".format(ipv6_list))