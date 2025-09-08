#! /usr/bin/env python
'''
7. Using your TextFSM template and the 'show interface status' 
data from exercise2, create a Python program that uses TextFSM to 
parse this data. In this Python program, read the show interface 
status data from a file and process it using the TextFSM template. 
From this parsed-output, create a list of dictionaries. The program 
output should look as follows:
[{'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/0',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/1',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/2',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/3',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'}]
'''
from pprint import pprint as pp
import textfsm

TextFSM_Template = "class4/ex2_show_int_status.tpl"
template = open(TextFSM_Template)

with open("class4/ex2_show_int_status.txt") as f:
    raw_text_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

table_keys = re_table.header
final_list = []
for fsm_list in data:
    fsm_dict = dict(zip(table_keys, fsm_list))
    final_list.append(fsm_dict)

print()
pp(final_list)
print()