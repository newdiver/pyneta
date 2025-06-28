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
device1 ={ #(NX-OSv Switch)
    "hostname" : 'nxos2.lasthop.io',
   # "ssh_port" : 22,
   # nxapi_port : 8443,
    "username" : 'pyclass',
    "password" : getpass(),
    "device_type" : cisco_nxos,
    "global_delay_factor" : 2,
    "fast_cli" : False,
}
net_connect = ConnectHandler(**device1)
print(net_connection.find_prompt())

output = net_connect.send_command("show lldp neighbors detail")
print(output)
