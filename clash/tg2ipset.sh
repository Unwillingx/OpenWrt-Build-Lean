#!/bin/bash

wget -cO /etc/openclash/telegram.txt https://core.telegram.org/resources/cidr.txt
if [ $? == 0 ]; then
  ipset destroy telegram
  ipset create telegram hash:net
  for a in $(grep -v ":" /etc/openclash/telegram.txt)
  do
    ipset add telegram $a
  done
fi
