#!/usr/bin/env python
'''
6. Use Netmiko to retrieve 'show run' from the Cisco4 device. Feed this configuration into CiscoConfParse.

Use CiscoConfParse to find all of the interfaces on Cisco4 that have an IP address. Print out the interface name and IP address for each interface. 
Your solution should work if there is more than one IP address configured on Cisco4. For example, if you configure a loopback interface on Cisco4 with an IP address, then your solution should continue to work. The output from this program should look similar to the following:
$ python confparse_ex6.py 

Interface Line: interface GigabitEthernet0/0/0
IP Address Line:  ip address 10.220.88.23 255.255.255.0

Note: CiscoConfParse now emits a logging message unless you set "ignore_blank_lines=False". Consequently, you should add this argument to your CiscoConfParse call:
CiscoConfParse(config.splitlines(), ignore_blank_lines=False)



'''
import yaml 
from os import path
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

if __name__ == "__main__":
    home_dir = path.expanduser("~")
    filename = path.join(home_dir, ".netmiko.yml")

    with open(filename, "r") as file:
        netdevices = yaml.safe_load(file)

    cisco4 = netdevices["cisco4"]
    net_connect = ConnectHandler(**cisco4)
    with net_connect:
        try:
            print(net_connect.find_prompt()) # Troubleshooting see if i can get the command prompt
            switch_output = net_connect.send_command("show run")
            dir(switch_output)
            parse = CiscoConfParse(switch_output.splitlines(), ignore_blank_lines=False)
            interfaces = parse.find_objects_w_child(
            parentspec=r"^interface", childspec=r"^\s+ip address"
            )
            print(interfaces)
            #for intf in interfaces:
        except Exception as e:
            print(f"An error occurred: {e}")
