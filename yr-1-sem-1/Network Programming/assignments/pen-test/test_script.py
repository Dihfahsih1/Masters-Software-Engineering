#MAC address spoofing using Python:

import subprocess as sub
#subprocess => module used to run new codes and applications by creating new processes

interface = "wlp2s0" #wlp2s0 => wide local area network PCI bus 2 on slot zero

new_mac = "1C:4D:70:C8:6B:B8"

#call() is used to initiate a program
#alternatively you can use Popen and run()
sub.call(['sudo', 'ifconfig', interface, 'down'])

sub.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])

sub.call(['sudo', 'ifconfig', interface, 'up'])

#run ifconfig wlp2s0 before and after running this python script

