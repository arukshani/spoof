from scapy.all import *

print("SNIFFING PACKETS")


def print_pkt(pkt):
    print("Source IP:", pkt[IP].src)
    print("Destination IP:", pkt[IP].dst)
    print("Protocol:", pkt[IP].proto)
    print("\n")

    a = IP(src="10.10.1.3", dst="10.10.1.1") 
    b = UDP() 
    data = pkt[UDP].payload 
    newpkt = a/b/data

    print("Spoofed Packet………") 
    print("Source IP : ", newpkt[IP].src) 
    print("Destination IP :", newpkt[IP].dst) 
    send(newpkt)


pkt = sniff(filter='ip src host 10.10.1.5', prn=print_pkt)