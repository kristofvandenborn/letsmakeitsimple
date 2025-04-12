from scapy.all import *

client_ip = "10.0.0.2"
server_ip = "10.0.0.1"
client_mac = "00:11:22:33:44:55"
server_mac = "66:55:44:33:22:11"
client_port = 12345
server_port = 80
seq = 1000
ack = 2000

syn = Ether(src=client_mac, dst=server_mac) / IP(src=client_ip, dst=server_ip) /       TCP(sport=client_port, dport=server_port, flags='S', seq=seq)

syn_ack = Ether(src=server_mac, dst=client_mac) / IP(src=server_ip, dst=client_ip) /           TCP(sport=server_port, dport=client_port, flags='SA', seq=ack, ack=seq+1)

ack_pkt = Ether(src=client_mac, dst=server_mac) / IP(src=client_ip, dst=server_ip) /           TCP(sport=client_port, dport=server_port, flags='A', seq=seq+1, ack=ack+1)

http_payload = b"GET / HTTP/1.1\r\nHost: example.com\r\nUser-Agent: Scapy\r\n\r\n"
http_get = Ether(src=client_mac, dst=server_mac) / IP(src=client_ip, dst=server_ip) /            TCP(sport=client_port, dport=server_port, flags='PA', seq=seq+1, ack=ack+1) / Raw(load=http_payload)

http_response = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body>Hello</body></html>"
http_200 = Ether(src=server_mac, dst=client_mac) / IP(src=server_ip, dst=client_ip) /            TCP(sport=server_port, dport=client_port, flags='PA', seq=ack+1, ack=seq+1+len(http_payload)) /            Raw(load=http_response)

final_ack = Ether(src=client_mac, dst=server_mac) / IP(src=client_ip, dst=server_ip) /             TCP(sport=client_port, dport=server_port, flags='A',
                seq=seq+1+len(http_payload), ack=ack+1+len(http_response))

wrpcap("tcp_http_handshake.pcap", [syn, syn_ack, ack_pkt, http_get, http_200, final_ack])
print("✅ TCP/HTTP pcap generated.")
