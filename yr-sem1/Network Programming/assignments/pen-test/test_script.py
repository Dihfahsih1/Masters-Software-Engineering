#MAC address spoofing using Python:

import subprocess as sub

interface = "wlp2s0"

#fe80::2fd3:bfe6:6d8f:3efb
new_mac = "08:00:27:02:3a:52"

sub.call(['sudo', 'ifconfig', interface, 'down'])

sub.call(['sudo', 'ifconfig', interface, 'hw', 'wlp2s0', new_mac])

sub.call(['sudo', 'ifconfig', interface, 'up'])