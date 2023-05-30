#!/bin/bash

wget -cO /etc/openclash/telegram.txt https://core.telegram.org/resources/cidr.txt

if [ $? == 0 ]; then

    ipset destroy telegram

    ipset create telegram hash:net

    for a in $(cat /etc/openclash/telegram.txt)

    do

        if [ ! grep -q ":" <<< "$a"]; then

            ipset add telegram $a

        else

            break

        if
    done

if
