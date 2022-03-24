#MAC address spoofing using Python:

import subprocess as sub

interface = "wlp2s0"

#fe80::2fd3:bfe6:6d8f:3efb
new_mac = "1C:4D:70:C8:6B:B8"

sub.call(['sudo', 'ifconfig', interface, 'down'])

sub.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])

sub.call(['sudo', 'ifconfig', interface, 'up'])

#run ifconfig wlp2s0 before and after running this python script

