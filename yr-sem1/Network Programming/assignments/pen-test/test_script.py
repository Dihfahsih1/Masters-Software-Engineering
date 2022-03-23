import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket. htons(0x0003))

# s.bind(("mon0", 0x0003))

# ap_list = []

# while True:
#   packet = s.recvfrom(2048)
#   if packet[26] == "\x80" :
#     if packetkt[36:42] not in ap_list and ord(packetkt[63]) > 0:
#         ap_list.add(packetkt[36:42])
        
#   print("SSID:",(pkt[64:64+ord(pkt[63])],pkt[36:42].encode('hex')))

from scapy.all import *
i = 1

def deauth_frame(pkt):
  if pkt.haslayer(Dot11):
    if ((pkt.type == 0) & (pkt.subtype == 12)):
      global i
      print ("Deauth frame detected: ", i)
      i = i + 1
  sniff(iface = "mon0", prn = deauth_frame)
  print("Error")