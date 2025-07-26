
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


home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename, "r") as file:
    netdevices = yaml.safe_load(file)

cisco4 = netdevices["cisco4"]
net_connect = ConnectHandler(**cisco4)

switch_output = net_connect.send_command('show run')
from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('switch_output', syntax='ios')

for intf_obj in parse.find_parent_objects('^interface', '^\s+ip address'):
    print("ip address: " + intf_obj.text)