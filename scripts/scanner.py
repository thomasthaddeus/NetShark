#!/usr/bin/env python3

"""scanner.py
Summary:
    A script to extract specific details (such as IVs and TCP checksums) from a pcap file.

Extended Summary:
    This script utilizes the pyshark library to analyze packet captures and extract
    specific details such as the number of IVs, the IV for the first packet, and the
    TCP checksum for the first packet.

Returns:
    None: This script prints the extracted details to the console.
"""

import pyshark

def get_wlan_details(cap):
    """
    Extracts details about the WLAN packets in the provided capture.

    Specifically, this function counts the number of IVs in the capture and retrieves
    the IV of the first packet.

    Args:
        cap (pyshark.file.capture.FileCapture): The packet capture to analyze.

    Returns:
        tuple: A tuple containing the total number of IVs (int) and the IV of the first
        packet (str).
    """
    total_ivs = 0
    first_iv = None

    for packet in cap:
        if "wlan" in packet:
            if "wlan.iv" in packet:
                total_ivs += 1
                if first_iv is None:
                    first_iv = packet.wlan.iv

    return total_ivs, first_iv

def get_first_tcp_checksum(cap):
    """
    Extracts the TCP checksum of the first TCP packet in the capture.

    Args:
        cap (pyshark.file.capture.FileCapture): The packet capture to analyze.

    Returns:
        str or None: The TCP checksum of the first TCP packet or None if no TCP packet is found.
    """
    for packet in cap:
        if "tcp" in packet and "tcp.checksum" in packet:
            return packet.tcp.checksum
    return None

def crack_pcap():
    pass  # To be implemented

def main():
    """
    Main function to drive the script.

    Loads a pcap file, extracts specific details from the capture and prints them.
    """
    # Load the pcap file
    cap = pyshark.FileCapture("./PCAP2.cap")

    # Get WLAN details
    total_ivs, first_iv = get_wlan_details(cap)

    # Get first TCP checksum
    first_tcp_checksum = get_first_tcp_checksum(cap)

    print(f"Total IVs in the capture: {total_ivs}")
    print(f"IV for the first packet: {first_iv}")
    print(f"TCP checksum for the first packet: {first_tcp_checksum}")

# Note: Extracting WEP key directly from a pcap is not straightforward and
# typically requires a separate cracking procedure. pcap files usually
# don't contain the WEP key in plaintext.

if __name__ == "__main__":
    main()
