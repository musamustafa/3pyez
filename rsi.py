#!/usr/local/bin/python3

from jnpr.junos import Device
from pprint import pprint as pp
from jnpr.junos.utils.start_shell import StartShell
from lxml import etree
from jnpr.junos.utils.scp import SCP

# connect to the device with IP-address, login user and passwort
dev = Device(host="10.49.236.63", user="musa", password="Musa19ie@", port=22, gather_facts=False)
dev.open()
# Increase timeout to 600 sec.
dev.timeout = 600
print("Connection successfully...")

# Open a new shell connection via StartShell (Paramiko)
ss = StartShell(dev)
ss.open()
ss.run('cli -c "request support information | save /var/tmp/pyez_rsi2.txt"')

# Transfer file via SCP
with SCP(dev, progress=True) as scp:
    scp.get("/var/tmp/pyez_rsi2.txt", "rsi2.txt")

ss.run('rm /var/tmp/pyez_rsi*')
ss.close()
# Close connection to the device

dev.close()
print("Connection closed...")
