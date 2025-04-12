from scapy.all import *
from scapy.contrib.stp import STP

# MAC addresses and Bridge IDs
mac_a = "00:aa:aa:aa:aa:aa"
mac_b = "00:bb:bb:bb:bb:bb"
mac_c = "00:cc:cc:cc:cc:cc"

bridge_id_a = b'\x80\x00' + bytes.fromhex(mac_a.replace(':', ''))
bridge_id_b = b'\x80\x00' + bytes.fromhex(mac_b.replace(':', ''))
bridge_id_c = b'\x80\x00' + bytes.fromhex(mac_c.replace(':', ''))

def config_bpdu(src_mac, root_id, bridge_id, port_id, cost=0, tc_flag=0):
    return (
        Ether(src=src_mac, dst="01:80:c2:00:00:00") /
        LLC(dsap=0x42, ssap=0x42, ctrl=3) /
        STP(bpdutype=0x00, rootid=root_id, rootpathcost=cost,
            bridgeid=bridge_id, portid=port_id, flags=tc_flag)
    )

def tcn_bpdu(src_mac, bridge_id):
    return (
        Ether(src=src_mac, dst="01:80:c2:00:00:00") /
        LLC(dsap=0x42, ssap=0x42, ctrl=3) /
        STP(bpdutype=0x80)
    )

# Step-by-step packets
packets = []

# Step 1-2: Initial config BPDUs
packets.append(config_bpdu(mac_a, bridge_id_a, bridge_id_a, port_id=0x8001))
packets.append(config_bpdu(mac_b, bridge_id_a, bridge_id_b, port_id=0x8001, cost=4))
packets.append(config_bpdu(mac_c, bridge_id_a, bridge_id_c, port_id=0x8001, cost=4))

# Step 3: Link A-C fails (no packet, just event)

# Step 4-5: TCN from C to B, ACK from B
packets.append(tcn_bpdu(mac_c, bridge_id_c))  # C sends TCN to B
packets.append(config_bpdu(mac_b, bridge_id_a, bridge_id_b, port_id=0x8002))  # B sends ACK via Config BPDU

# Step 6-7: TCN from B to A, ACK from A
packets.append(tcn_bpdu(mac_b, bridge_id_b))  # B sends TCN to A
packets.append(config_bpdu(mac_a, bridge_id_a, bridge_id_a, port_id=0x8001))  # A sends ACK via Config BPDU

# Step 8: Config BPDUs with TC flag from root
packets.append(config_bpdu(mac_a, bridge_id_a, bridge_id_a, port_id=0x8001, tc_flag=1))

# Step 9: New config BPDUs with updated role info
packets.append(config_bpdu(mac_b, bridge_id_a, bridge_id_b, port_id=0x8001, cost=4))
packets.append(config_bpdu(mac_c, bridge_id_a, bridge_id_c, port_id=0x8001, cost=8))

# Save to pcap
wrpcap("stp_convergence.pcap", packets)
print("✅ STP convergence pcap generated.")
