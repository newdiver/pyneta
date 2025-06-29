
'''cCreate a script using Netmiko that executes 'show version' 
and 'show lldp neighbors' against the Cisco4 device with use_textfsm=True.

'''

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

cisco4 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

net_connect = ConnectHandler(**cisco4)
print(net_connect.find_prompt())
try:
    output = net_connect.send_command('show version',use_textfsm=True)
    output += net_connect.send_command('show lldp neighbors',use_textfsm=True)
    neighbor_port = output[1]['neighbor_interface']

    pprint(output)
    print(f"The neighbor switchport is {neighbor_port}")
    
except Exception as e:
    print(f"An error occurred: {e}")

net_connect.disconnect()