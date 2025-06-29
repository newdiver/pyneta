'''
2. Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2 and 
fast_cli=False (you must explicitly set fast_cli=False as the Netmiko default has changed). 
Execute 'show lldp neighbors detail' and print the returned output to standard output. 
Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8.
Print the output of this command to standard output. Use the Python datetime library to record 
the execution time of both of these commands. Print these execution times to standard output.
'''

#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device1 ={ #(NX-OSv Switch)
    "host" : 'nxos2.lasthop.io',
   # "ssh_port" : 22,
   # nxapi_port : 8443,
    "username" : 'pyclass',
    "password" : getpass(),
    "device_type" : 'cisco_nxos',
    "global_delay_factor" : 2,
    "fast_cli" : False,
}
global_delay_factor_val = device1["global_delay_factor"]
delay_factor_val = 8
net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

startTime = datetime.now()
output = net_connect.send_command("show lldp neighbors detail")
print(output)

global_delay_time = datetime.now() - startTime

startTime = datetime.now()

output = net_connect.send_command("show lldp neighbors detail", delay_factor==delay_factor_val)
print(output)

function_delay_time = datetime.now() - startTime

print(f"The Global delay factor of {global_delay_factor_val} took {global_delay_time} seconds")
print(f"The delay factor of {delay_factor_val} took {function_delay_time} seconds")
