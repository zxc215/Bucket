from scapy.all import *

p1 = Ether(dst="aa:bb:cc:dd:ee:ff") / IP(src="0.0.0.0",dst="192.168.10.100") / TCP(sport=15,dport=51) / "aaaaaaaaaaaaaaaaaaaaa"
p2 = Ether(dst="aa:bb:cc:dd:ee:ff") / IP(src="0.0.0.0",dst="192.168.10.100") / TCP(sport=15,dport=52) / "aaaaaaaaaaaaaaaaaaaaa"
p3 = Ether(dst="aa:bb:cc:dd:ee:ff") / IP(src="0.0.0.0",dst="192.168.10.100") / TCP(sport=15,dport=53) / "aaaaaaaaaaaaaaaaaaaaa"
p4 = Ether(dst="aa:bb:cc:dd:ee:ff") / IP(src="0.0.0.0",dst="192.168.10.100") / TCP(sport=15,dport=54) / "aaaaaaaaaaaaaaaaaaaaa"
p5 = Ether(dst="aa:bb:cc:dd:ee:ff") / IP(src="0.0.0.0",dst="192.168.10.100") / TCP(sport=15,dport=55) / "aaaaaaaaaaaaaaaaaaaaa"
p = Ether(dst="aa:bb:cc:dd:ee:ff") / IP(src="10.0.0.100",dst="10.0.0.2") / TCP(sport=100,dport=200) / "aaaaaaaaaaaaaaaaaaaaa"
# p.show()
#hexdump(p)
for i in range (1):
    sendp(p,iface = "enp4s8")
#    sendp(p1,iface = "vf0_0")
#    sendp(p2,iface = "vf0_0")
#    sendp(p3,iface = "vf0_0")
#    sendp(p4,iface = "vf0_0")
#    sendp(p5,iface = "vf0_0")
