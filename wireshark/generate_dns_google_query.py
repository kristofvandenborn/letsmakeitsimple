from scapy.all import *

pc_ip = "192.168.1.100"
dns_ip = "95.56.3.21"
pc_mac = "00:11:22:33:44:55"
dns_mac = "66:55:44:33:22:11"
src_port = 33333
dns_port = 53
dns_txid = 0xAAAA

dns_query = (
    Ether(src=pc_mac, dst=dns_mac) /
    IP(src=pc_ip, dst=dns_ip) /
    UDP(sport=src_port, dport=dns_port) /
    DNS(id=dns_txid, rd=1, qd=DNSQR(qname="google.com", qtype="A"))
)

dns_response = (
    Ether(src=dns_mac, dst=pc_mac) /
    IP(src=dns_ip, dst=pc_ip) /
    UDP(sport=dns_port, dport=src_port) /
    DNS(id=dns_txid, qr=1, aa=1, ra=1, qd=DNSQR(qname="google.com", qtype="A"),
        an=DNSRR(rrname="google.com", type="A", rdata="142.250.190.78", ttl=300))
)

wrpcap("dns_google_query.pcap", [dns_query, dns_response])
print("✅ DNS pcap generated.")
