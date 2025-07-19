#!/usr/bin/env python

'''
2b. Write the data structure you created in part 2a out to a YAML file.
Use expanded YAML format. How could you re-use this YAML file 
later when creating Netmiko connections to devices?

'''

import yaml 
from pprint import pprint

cisco3 = {"device_name" : "cisco3", "host": "cisco3.lasthop.io"}
cisco4 = {"device_name" : "cisco4", "host": "cisco4.lasthop.io"} 
arista1 = {"device_name" : "arista1", "host" : "arista1.lasthop.io"}
arista2 = {"device_name" : "arista2", "host": "arista2.lasthop.io"}

my_devices= [cisco3,cisco4,arista1,arista2]

for device in my_devices:
   
    device["username"] = "myadmin"
    device["password"] = "sneakyword"
    
    print(my_devices)
    with open("output.yaml", "w") as file:
        yaml.dump(my_devices, file, default_flow_style=False, sort_keys=False)
   

    
    
    
    