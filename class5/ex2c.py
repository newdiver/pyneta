#! /usr/bin/env python 
'''
2c. Use Netmiko to push the configurations generated in exercise 2b 
to the nxos1 device and to the nxos2 device, respectively. Verify you 
are able to ping between the devices and also verify that the BGP 
session reaches the established state. Note, you might need to use 
an alternate interface besides Ethernet 1/1 (you can use either 
Ethernet 1/1, 1/2, 1/3, or 1/4). Additionally, you might need to 
use a different IP network (to avoid conflicts with other students). 
Your autonomous system should remain 22, however.

For this exercise you should store your Netmiko connection 
dictionaries in an external file named my_devices.py and should 
import nxos1, and nxos2 from that external file. Make sure that 
you use getpass() to enter the password in for these devices 
(as opposed to storing the definitions in the file).
'''
import time
import re

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

from netmiko import ConnectHandler
from my_devices import nxos1, nxos2

if __name__ =="__main__":
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader("./templates/exercise2")

filename = "ex2b_nxos.j2"

