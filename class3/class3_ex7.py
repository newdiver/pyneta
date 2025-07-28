# class3_ex7.py
#1 /usr/bin/ python
'''
From this BGP configuration, retrieve all of BGP peer IP addresses and their corresponding remote-as. 
Return a list of tuples. The tuples should be (neighbor_ip, remote_as). Print your data-structure to 
standard output.

Your output should look similar to the following. Use ciscoconfparse to accomplish this.
​BGP Peers: 
[('10.220.88.20', '42'), ('10.220.88.32', '43')]

'''
from ciscoconfparse import CiscoConfParse


bgp_data = """ router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""


bgp_obj = CiscoConfParse(bgp_data.splitlines())

neighbor = bgp_obj.find_objects(r"^bgp")
print(neighbor)
print(type(neighbor))
print(dir(neighbor))



#print("​BGP Peers:") 
#print([('10.220.88.20', '42'), ('10.220.88.32', '43')])