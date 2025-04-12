from scapy.all import *

client_ip = "10.0.0.2"
server_ip = "10.0.0.1"
client_mac = "00:11:22:33:44:55"
server_mac = "66:55:44:33:22:11"
telnet_port = 23
ssh_port = 22
telnet_seq = 1000
ssh_seq = 2000
server_seq_base = 3000

# TELNET SESSION
client_port_telnet = 40000
telnet_syn = Ether(src=client_mac, dst=server_mac) / IP(src=client_ip, dst=server_ip) /     TCP(sport=client_port_telnet, dport=telnet_port, flags='S', seq=telnet_seq)
telnet_syn_ack = Ether(src=server_mac, dst=client_mac) / IP(src=server_ip, dst=client_ip) /     TCP(sport=telnet_port, dport=client_port_telnet, flags='SA', seq=server_seq_base, ack=telnet_seq+1)
telnet_ack = Ether(src=client_mac, dst=server_mac) / IP(src=client_ip, dst=server_ip) /     TCP(sport=client_port_telnet, dport=telnet_port, flags='A', seq=telnet_seq+1, ack=server_seq_base+1)

payloads_telnet = [b"Username: admin\r\n", b"Password: cisco123\r\n", b"show ip int brief\r\n"]
telnet_packets = [telnet_syn, telnet_syn_ack, telnet_ack]
telnet_seq += 1
server_seq = server_seq_base + 1

for payload in payloads_telnet:
    pkt = Ether(src=client_mac, dst=server_mac) / IP(src=client_ip, dst=server_ip) /           TCP(sport=client_port_telnet, dport=telnet_port, flags='PA', seq=telnet_seq, ack=server_seq) / Raw(load=payload)
    telnet_packets.append(pkt)
    telnet_seq += len(payload)

wrpcap("telnet_session.pcap", telnet_packets)

# SSH SESSION
client_port_ssh = 40001
ssh_syn = Ether(src=client_mac, dst=server_mac) / IP(src=client_ip, dst=server_ip) /     TCP(sport=client_port_ssh, dport=ssh_port, flags='S', seq=ssh_seq)
ssh_syn_ack = Ether(src=server_mac, dst=client_mac) / IP(src=server_ip, dst=client_ip) /     TCP(sport=ssh_port, dport=client_port_ssh, flags='SA', seq=server_seq_base, ack=ssh_seq+1)
ssh_ack = Ether(src=client_mac, dst=server_mac) / IP(src=client_ip, dst=server_ip) /     TCP(sport=client_port_ssh, dport=ssh_port, flags='A', seq=ssh_seq+1, ack=server_seq_base+1)

encrypted_payload = b"\x17\x03\x03\x00\x2a\x9f\x3b\xae\x01\x82\xaa\xd4\x6f\x78\xcd\x23"
ssh_packets = [ssh_syn, ssh_syn_ack, ssh_ack]

for i in range(3):
    pkt = Ether(src=client_mac, dst=server_mac) / IP(src=client_ip, dst=server_ip) /           TCP(sport=client_port_ssh, dport=ssh_port, flags='PA', seq=ssh_seq+i*len(encrypted_payload), ack=server_seq_base+1) / Raw(load=encrypted_payload)
    ssh_packets.append(pkt)

wrpcap("ssh_session.pcap", ssh_packets)
print("✅ Telnet and SSH pcaps generated.")
