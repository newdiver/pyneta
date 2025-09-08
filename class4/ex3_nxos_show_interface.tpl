Value INT_NAME (\S+)
Value LINE_STATUS ((up|down))
Value ADMIN_STATUS ((up|down))
Value MAC_ADDR ([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})
Value MTU (\d+)
Value DUPLEX ((full|half)-duplex)
Value SPEED (\d+)

Start
  ^${INT_NAME} is ${LINE_STATUS}$$
  ^admin state is ${ADMIN_STATUS},
  ^  Hardware:.*address: ${MAC_ADDR}\s
  ^  MTU ${MTU} bytes
  ^  ${DUPLEX}, ${SPEED} Mb/s -> Record
  
  
    
#  Ethernet2/1 is up
#  admin state is up, Dedicated Interface
#    Hardware:  Ethernet, address: 000c.29d1.d56b (bia 2cc2.605e.5dba)
#    MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec
#    reliability 255/255, txload 1/255, rxload 1/255
#    Encapsulation ARPA, medium is broadcast
#    Port mode is routed
#    full-duplex, 1000 Mb/s
#    Beacon is turned off
#    Auto-Negotiation is turned off
#    Input flow-control is off, output flow-control is off
#    Auto-mdix is turned off
#    Switchport monitor is off 
#    EtherType is 0x8100 
#    EEE (efficient-ethernet) : n/a
#    Last link flapped 2week(s) 0day(s)
#    Last clearing of "show interface" counters never