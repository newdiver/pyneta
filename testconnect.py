#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

net_connection = ConnectHandler(
    host='cisco3.lasthop.io', 
    username='pyclass', 
    password=getpass(), 
    device_type='cisco_ios',
    session_log='my_session.txt',
)
print(net_connection.find_prompt())

    
