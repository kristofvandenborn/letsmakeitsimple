from scapy.all import *
from scapy.layers.dhcp import DHCP, BOOTP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether

xid = 0x12345678
client_mac = "00:11:22:33:44:55"
server_mac = "66:55:44:33:22:11"
client_mac_bytes = bytes.fromhex(client_mac.replace(':', ''))

discover = Ether(src=client_mac, dst="ff:ff:ff:ff:ff:ff") / IP(src="0.0.0.0", dst="255.255.255.255") /            UDP(sport=68, dport=67) / BOOTP(chaddr=client_mac_bytes, xid=xid, flags=0x8000) /            DHCP(options=[("message-type", "discover"), "end"])

offer = Ether(src=server_mac, dst=client_mac) / IP(src="192.168.1.1", dst="255.255.255.255") /         UDP(sport=67, dport=68) / BOOTP(op=2, yiaddr="192.168.1.100", siaddr="192.168.1.1",
        chaddr=client_mac_bytes, xid=xid) / DHCP(options=[("message-type", "offer"), ("server_id", "192.168.1.1"),
        ("lease_time", 3600), "end"])

request = Ether(src=client_mac, dst="ff:ff:ff:ff:ff:ff") / IP(src="0.0.0.0", dst="255.255.255.255") /           UDP(sport=68, dport=67) / BOOTP(chaddr=client_mac_bytes, xid=xid, flags=0x8000) /           DHCP(options=[("message-type", "request"), ("server_id", "192.168.1.1"),
          ("requested_addr", "192.168.1.100"), "end"])

ack = Ether(src=server_mac, dst=client_mac) / IP(src="192.168.1.1", dst="255.255.255.255") /       UDP(sport=67, dport=68) / BOOTP(op=2, yiaddr="192.168.1.100", siaddr="192.168.1.1",
      chaddr=client_mac_bytes, xid=xid) / DHCP(options=[("message-type", "ack"), ("server_id", "192.168.1.1"),
      ("lease_time", 3600), "end"])

wrpcap("dhcp_handshake.pcap", [discover, offer, request, ack])
print("✅ DHCP pcap generated.")
