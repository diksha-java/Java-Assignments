from scapy.all import sniff,IP
from collections import defaultdict
import time
packet_counter=defaultdict(int)
start_time=time.time()
def packet_analysis(packet):
    if packet.haslayer(IP):
        source_ip=packet[IP].src
        packet_counter[source_ip]+=1
        if time.time()-start_time>10:
            for ip,count in packet_counter.items():
                print("IP:",
                      ip,
                      "Packets:",
                      count)
                if count>100:
                    print("ALERT:Possible DoS Attack")
                    print("Source:",ip)
                    packet_counter.clear()
                    print("DoS Detection Started")
                    sniff(prn=packet_analysis,
                          store=False)
