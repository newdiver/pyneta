
'''cisco4#ping
Protocol [ip]: 
Target IP address: 8.8.8.8
Repeat count [5]: 
Datagram size [100]: 
Timeout in seconds [2]: 
Extended commands [n]: 
Sweep range of sizes [n]: 
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/4 ms
'''

from netmiko import ConnectHandler
from getpass import getpass

cisco4 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

net_connect = ConnectHandler(**cisco4)
print(net_connect.find_prompt())
try:
    output = net_connect.send_command_timing('Ping', strip_prompt=False,strip_command=False)
    output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
    output += net_connect.send_command_timing("8.8.8.8", strip_prompt=False, strip_command=False
)
    output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
    output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
    output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
    output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
    output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
    net_connect.disconnect()

    print(output)
except Exception as e:
    print(f"An error occurred: {e}")

net_connect.disconnect()