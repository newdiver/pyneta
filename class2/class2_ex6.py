#!/usr/bin/env python

import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime 
import time

'''6. Using SSH and netmiko connect to the Cisco4 router. 
In your device definition, specify both an 'secret' and a 
'session_log'. Your device definition should look as follows:
​password = getpass()
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}
a. Print the current prompt using find_prompt()

b. Execute the config_mode() method and print the new 
prompt using find_prompt()

c. Execute the exit_config_mode() method and 
print the new prompt using find_prompt()

d. Use the write_channel() method to send the 'disable' 
command down the SSH channel. Note, write_channel is a low 
level method so it requires that you add a newline to the end of your 'disable' command.

e. time.sleep for two seconds and then use the read_channel() 
method to read the data that is currently available on the SSH 
channel. Print this to the screen.

f. Execute the enable() method and print your now current 
prompt using find_prompt(). The enable() method will use the 
'secret' defined in your device definition. This 'secret' is the 
same as the standard lab password.

g. After you are done executing your script, look at the 
'my_output.txt' file to see what is included in the session_log.


'''
device = { 
    "host" : 'cisco4.lasthop.io',
 #   "ssh_port" : 22,
    "username" : 'pyclass',
    "password" : getpass(),
    "secret" : getpass(),
     "device_type" : 'cisco_ios',
     "session_log" : 'my_output.txt',
    }



net_connect = ConnectHandler(**device)
with net_connect :

    print(net_connect.find_prompt())
    try:
    #    startTime = datetime.now()
    #    print(startTime)
        output = net_connect.config_mode()
    # Step a.
        print(output)
    #    endTime = datetime.now() - startTime
    #    print(endTime)
    # Step B.    
        print(net_connect.find_prompt())
        output = net_connect.exit_config_mode()
    # step C.
        print(output)
    #    net_connect.save_config()
    # step D.
        net_connect.write_channel('disable\n')
        time.sleep(21) # Allow some time for the device to process
        output = net_connect.read_channel()
        print(output)
    # step 7
        net_connect.write_channel('enable\n')  # Ctrl+A
        time.sleep(1)
        output = net_connect.read_channel()
        print(output)
        output = net_connect.write_channel(secret)
        output = net_connect.write_channel('\n')
        print(output)
    except Exception as e:
        print(f"An error occurred: {e}")

net_connect.disconnect()