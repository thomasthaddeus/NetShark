"""checksum.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

# 1st approach

import pyshark

# Load the pcap file
cap = pyshark.FileCapture('/mnt/data/checksum.pcap', use_json=True, include_raw=True)

# Extract DNS queries
dns_queries = []
for packet in cap:
    if 'DNS' in packet and hasattr(packet.dns, 'qry_name'):
        dns_queries.append(packet.dns.qry_name)

print(dns_queries)


# 2nd approach

from scapy.all import rdpcap, DNSQR

# Load the pcap file
packets = rdpcap('/mnt/data/checksum.pcap')

# Extract DNS queries
dns_queries = []
for packet in packets:
    if packet.haslayer(DNSQR):
        dns_queries.append(packet[DNSQR].qname.decode('utf-8'))

print(dns_queries)


# 3rd approach

import dpkt
import socket

# Function to extract DNS queries from the pcap file
def extract_dns_queries(pcap_file):
    with open(pcap_file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        queries = []

        for _, buf in pcap:
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                if isinstance(eth.data, dpkt.ip.IP):
                    ip = eth.data
                    if isinstance(ip.data, dpkt.udp.UDP) and ip.data.dport == 53:
                        udp = ip.data
                        dns = dpkt.dns.DNS(udp.data)
                        for qname in dns.qd:
                            queries.append(qname.name.decode())
            except Exception as e:
                continue

    return queries

dns_queries_alt = extract_dns_queries('/mnt/data/checksum.pcap')
print(dns_queries_alt)


# 4th approach

import struct

# Function to parse DNS queries from raw UDP data
def parse_dns_query(data):
    # DNS Header: Transaction ID (2 bytes), Flags (2 bytes), Questions (2 bytes)
    # Answers, Authority RRs, Additional RRs are 2 bytes each but we're only interested in Questions here
    transaction_id, flags, questions = struct.unpack('!HHH', data[:6])

    # We are only interested in standard queries
    if flags & 0x7800 != 0:  # Checking if Opcode (bits 3-6 of Flags) is non-zero
        return []

    # Parse questions
    data = data[6:]
    queries = []
    for _ in range(questions):
        query = []
        while True:
            length = data[0]
            if not length:
                break
            query.append(data[1:1+length].decode())
            data = data[1+length:]
        queries.append(".".join(query))
        data = data[5:]  # Skip Type (2 bytes) and Class (2 bytes) and null byte of the name
    return queries

# Extract DNS queries from the PCAP file
def extract_dns_queries_manual(pcap_file):
    with open(pcap_file, 'rb') as f:
        pcap_header = f.read(24)  # Read global header
        queries = []

        while True:
            pkt_header = f.read(16)  # Per-packet header
            if not pkt_header:
                break

            sec, usec, cap_len, length = struct.unpack('IIII', pkt_header)
            pkt_data = f.read(cap_len)

            # Check for IP (0x0800) and UDP (0x11)
            if pkt_data[12:14] == b'\x08\x00' and pkt_data[23] == 0x11:
                udp_data = pkt_data[42:]  # Skip Ethernet, IP, and UDP headers
                queries.extend(parse_dns_query(udp_data))

    return queries

dns_queries_manual = extract_dns_queries_manual('/mnt/data/checksum.pcap')
print(dns_queries_manual)
