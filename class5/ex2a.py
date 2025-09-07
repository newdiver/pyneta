#! /usr/bin/env python
'''
 Use Python and Jinja2 to generate the below NX-OS interface 
 configuration. You should use an external template file and 
 a Jinja2 environment to accomplish this. The interface, ip_address, 
 and netmask should all be variables in the Jinja2 template.
 
nxos1
interface Ethernet1/1
  ip address 10.1.100.1/24

nxos2
interface Ethernet1/1
  ip address 10.1.100.2/24
  '''
from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined, Template
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/")

filename = "./templates/ex2_nxos.j2"
with open(filename) as f:
    my_template = f.read()
nxos1 = {
  "interface": "ethernet1/1",
  "ipv4_address":"10.1.100.1",
  "ipv4_mask": "24",
}
nxos2 = {
  "interface": "ethernet1/1",
  "ipv4_address": "10.1.100.2",
  "ipv4_mask":"24"
}   
for j2_vars in (nxos1, nxos2):
    j2_template = Template(my_template)
    output = j2_template.render(**j2_vars)
    print(output) 
  