#!/bin/bash
./etc/mosdns/rule/ruleupdate.sh
service mosdns stop
mosdns start -c /etc/mosdns/config_custom.yaml
