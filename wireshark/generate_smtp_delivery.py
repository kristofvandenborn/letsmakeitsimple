from scapy.all import *

sender_ip = "192.0.2.1"
receiver_ip = "198.51.100.1"
sender_mac = "00:11:22:33:44:55"
receiver_mac = "66:55:44:33:22:11"
src_port = 12345
dst_port = 25
client_seq = 1000
server_seq = 5000

syn = Ether(src=sender_mac, dst=receiver_mac) / IP(src=sender_ip, dst=receiver_ip) /       TCP(sport=src_port, dport=dst_port, flags='S', seq=client_seq)
syn_ack = Ether(src=receiver_mac, dst=sender_mac) / IP(src=receiver_ip, dst=sender_ip) /           TCP(sport=dst_port, dport=src_port, flags='SA', seq=server_seq, ack=client_seq+1)
ack = Ether(src=sender_mac, dst=receiver_mac) / IP(src=sender_ip, dst=receiver_ip) /       TCP(sport=src_port, dport=dst_port, flags='A', seq=client_seq+1, ack=server_seq+1)

smtp_msgs = [
    b"220 mail.receiver.com ESMTP Postfix\r\n",
    b"HELO mail.sender.com\r\n",
    b"250 mail.receiver.com\r\n",
    b"MAIL FROM:<sender@example.com>\r\n",
    b"250 2.1.0 Ok\r\n",
    b"RCPT TO:<recipient@example.org>\r\n",
    b"250 2.1.5 Ok\r\n",
    b"DATA\r\n",
    b"354 End data with <CR><LF>.<CR><LF>\r\n",
    b"Subject: Test Email\r\n\r\nHello from sender!\r\n.\r\n",
    b"250 2.0.0 Ok: queued\r\n",
    b"QUIT\r\n",
    b"221 2.0.0 Bye\r\n"
]

def make_packet(src, dst, sport, dport, flags, seq, ack, payload, smac, dmac):
    return Ether(src=smac, dst=dmac) / IP(src=src, dst=dst) / TCP(sport=sport, dport=dport, flags=flags, seq=seq, ack=ack) / Raw(load=payload)

packets = [syn, syn_ack, ack]
client_seq += 1
server_seq += 1

for i, msg in enumerate(smtp_msgs):
    if i % 2 == 0:
        pkt = make_packet(receiver_ip, sender_ip, dst_port, src_port, 'PA', server_seq, client_seq, msg, receiver_mac, sender_mac)
        server_seq += len(msg)
    else:
        pkt = make_packet(sender_ip, receiver_ip, src_port, dst_port, 'PA', client_seq, server_seq, msg, sender_mac, receiver_mac)
        client_seq += len(msg)
    packets.append(pkt)

final_ack = Ether(src=sender_mac, dst=receiver_mac) / IP(src=sender_ip, dst=receiver_ip) /             TCP(sport=src_port, dport=dst_port, flags='A', seq=client_seq, ack=server_seq)
packets.append(final_ack)

wrpcap("smtp_delivery.pcap", packets)
print("✅ SMTP pcap generated.")
