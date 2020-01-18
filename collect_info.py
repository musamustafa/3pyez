#!/usr/local/bin/python3

from jnpr.junos import Device
from pprint import pprint as pp 

from lxml import etree


dev = Device(host='10.49.236.63', user='root', password='Embe1mpls', port=22)
dev.open()

dev.rpc.cli('request support information', format='text')
print(type(dev.facts))
pp(dev.facts['hostname'])

dev.close()




