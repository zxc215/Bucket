from scapy.all import *

sniff(iface = "enp4s8f1", prn = lambda x: hexdump(x))
