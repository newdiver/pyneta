'''2b. Expand your Jinja2 template such that both the following interface and 
BGP configurations are generated for nxos1 and nxos2. The interface name, 
IP address, netmask, local_as, and peer_ip should all be variables in the 
template. This is iBGP so the remote_as will be the same as the local_as.

nxos1

interface Ethernet1/1
  ip address 10.1.100.1/24

router bgp 22
  neighbor 10.1.100.2 remote-as 22
    address-family ipv4 unicast


nxos2

interface Ethernet1/1
  ip address 10.1.100.2/24

router bgp 22
  neighbor 10.1.100.1 remote-as 22
    address-family ipv4 unicast
'''

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined, Template
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/exercise2")

filename = "ex2b_nxos.j2"
#with open(filename) as f:
#    my_template = f.read()
nxos1 = {
  "device_name" : "nxos1",
  "interface": "ethernet1/1",
  "ipv4_address":"10.1.100.1",
  "local_as" : "22",
  "ipv4_netmask" : "24"
}
nxos2 = {
  "device_name": "nxos2",
  "interface": "ethernet1/1",
  "ipv4_address": "10.1.100.2",
  "local_as" : "22",
  "ipv4_netmask": "24"
}  
 
'''for j2_vars in (nxos1, nxos2):
    j2_template = Template(my_template)
    output = j2_template.render(**j2_vars)
    print(output) 
'''
nxos1["peer_ip_addr"] = nxos2["ipv4_address"]
nxos2["peer_ip_addr"] = nxos1["ipv4_address"]

print()
for device in (nxos1, nxos2):
    print(f" {device['device_name']} ".center(80, "#"))
    template = env.get_template(filename)
    output = template.render(**device)
    print(output)
    print()