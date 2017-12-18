from scapy.all import *

sniff(iface = "enp4s8f2", prn = lambda x: hexdump(x))
