"""
_summary_

_extended_summary_
"""

import pyshark

# Load the pcap file
cap = pyshark.FileCapture('d:/downloads/checksum.pcap')

# Variables to store required information
DNS_QUERY = None
INV_IP_CKSUM = None
INV_TCP_CKSUM = None
INV_UDP_CKSUM = None
MAC_CLIENT = None

# Iterate through each packet
for pkt in cap:
    # Extract the full domain name queried in the DNS request
    if "DNS" in pkt and hasattr(pkt.dns, 'qry_name'):
        DNS_QUERY = pkt.dns.qry_name

    # # Identify frames with invalid IP checksum
    # if hasattr(pkt.ip, 'checksum_bad') and pkt.ip.checksum_bad == '1':
    #     INV_IP_CKSUM = pkt.number

    # Identify frames with invalid TCP checksum
    if "TCP" in pkt and hasattr(pkt.tcp, 'checksum_bad') and pkt.tcp.checksum_bad == '1':
        INV_TCP_CKSUM = pkt.number

    # Identify frames with invalid UDP checksum
    if "UDP" in pkt and hasattr(pkt.udp, 'checksum_bad') and pkt.udp.checksum_bad == '1':
        INV_UDP_CKSUM = pkt.number

    # To find the manufacturer of the client device, you might look for the MAC
    # address of the client and then use a MAC address lookup tool or database
    # to determine the manufacturer. Here, we simply extract the MAC address
    # for demonstration.
    if "ETH" in pkt:
        MAC_CLIENT = pkt.eth.src

print("Full domain name queried in DNS request:", DNS_QUERY)
print("Frame number with invalid IP checksum:", INV_IP_CKSUM)
print("Frame number with invalid TCP checksum:", INV_TCP_CKSUM)
print("Frame number with invalid UDP checksum:", INV_UDP_CKSUM)
print("MAC address of the client device:", MAC_CLIENT)
