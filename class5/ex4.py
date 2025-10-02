#! /usr/bin/env python 
'''
4. Expand on exercise3 except use a for-loop to configure five VRFs. Each VRF should have a 
unique name and a unique route distinguisher. Each VRF should once again have the IPv4 and 
the IPv6 address families controlled by a conditional-variable passed into the template.

Note, you will want to pass in a list or dictionary of VRFs that you loop over in your Jinja2 template.

'''

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

if __name__ =="__main__":
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader("./templates/exercise4")

    vrf_list = [
        {"vrf_name": "blue", "rd_number": "100:1", "ipv4_enabled": True, "ipv6_enabled": True},
        {"vrf_name": "green", "rd_number": "100:2", "ipv4_enabled": True, "ipv6_enabled": True},
        {"vrf_name": "red", "rd_number": "100:3", "ipv4_enabled": True, "ipv6_enabled": True},
        {"vrf_name": "yellow", "rd_number": "100:4", "ipv4_enabled": True, "ipv6_enabled": True},
        {"vrf_name": "purple", "rd_number": "100:5", "ipv4_enabled": True, "ipv6_enabled": True},
        {"vrf_name": "khaki", "rd_number": "100:6", "ipv4_enabled": True, "ipv6_enabled": True},
]
j2_vars = {"vrf_list": vrf_list}    
print(env.loader)
template_filename = "ios_vrf.j2"
template = env.get_template(template_filename)
cfg = template.render(**j2_vars)
print(cfg)
print()
    
