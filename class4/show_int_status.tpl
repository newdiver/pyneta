Value PORT_NAME (\S+)

Start
  ^Port.*Type\s*$$ -> ShowPortName

ShowPortName
  ^${PORT_NAME} -> Record

EOF


