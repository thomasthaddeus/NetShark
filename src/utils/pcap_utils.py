"""pcap_utils.py

2. **`filter_packets(capture, filter_string)`**:
    - Purpose: Apply a filter to the packet capture based on a given filter string.
    - Parameters:
        - `capture`: The loaded packet capture.
        - `filter_string`: The filtering criteria (e.g., "ip.src == 192.168.1.1").

6. **`packet_to_dict(packet)`**:
    - Purpose: Convert a packet object into a dictionary format for easier manipulation.
    - Parameters:
        - `packet`: The packet object to convert.

7. **`calculate_bandwidth_usage(capture, interval)`**:
    - Purpose: Calculate bandwidth usage for specific intervals.
    - Parameters:
        - `capture`: The loaded packet capture.
        - `interval`: The time interval for which to calculate bandwidth (e.g., "1s", "1m").

10. **`validate_pcap(file_path)`**:
    - Purpose: Ensure the given file is a valid pcap or pcapng file.
    - Parameters:
        - `file_path`: The path to the pcap file.

11. **`get_duration(capture)`**:
    - Purpose: Calculate the duration of the packet capture.
    - Parameters:
        - `capture`: The loaded packet capture.

12. **`get_unique_ips(capture, ip_type="src")`**:
    - Purpose: Extract unique source or destination IPs from the packet capture.
    - Parameters:
        - `capture`: The loaded packet capture.
        - `ip_type`: The type of IP to extract ("src" or "dst").
"""

import pyshark
from typing import List, Dict, Union

def filter_packets(capture: pyshark.FileCapture, filter_string: str) -> List[pyshark.packet.packet.Packet]:
    """
    Apply a filter to the packet capture based on a given filter string.
    """
    try:
        field, _, value = filter_string.split()
        return [pkt for pkt in capture if pkt.layers[0].get_field_value(field) == value]
    except Exception as e:
        print(f"Error filtering packets: {e}")
        return []

def packet_to_dict(packet: pyshark.packet.packet.Packet) -> Dict:
    """
    Convert a packet object into a dictionary format for easier manipulation.
    """
    try:
        return {field.name: field.get_default_value() for layer in packet.layers for field in layer.field_names}
    except Exception as e:
        print(f"Error converting packet to dictionary: {e}")
        return {}

def calculate_bandwidth_usage(capture: pyshark.FileCapture, interval: str) -> Dict[str, int]:
    """
    Calculate bandwidth usage for specific intervals.
    """
    try:
        byte_count = 0
        bandwidth = {}
        start_time = float(capture[0].sniff_timestamp)

        for packet in capture:
            byte_count += int(packet.length)
            elapsed_time = float(packet.sniff_timestamp) - start_time

            if interval == "1s" and elapsed_time >= 1:
                bandwidth[packet.sniff_timestamp] = byte_count
                byte_count = 0
                start_time = float(packet.sniff_timestamp)
            elif interval == "1m" and elapsed_time >= 60:
                bandwidth[packet.sniff_timestamp] = byte_count
                byte_count = 0
                start_time = float(packet.sniff_timestamp)

        return bandwidth
    except Exception as e:
        print(f"Error calculating bandwidth usage: {e}")
        return {}

def validate_pcap(file_path: str) -> bool:
    """
    Ensure the given file is a valid pcap or pcapng file.
    """
    try:
        _ = pyshark.FileCapture(file_path)
        return True
    except Exception as e:
        print(f"Error validating pcap file: {e}")
        return False

def get_duration(capture: pyshark.FileCapture) -> Union[float, None]:
    """
    Calculate the duration of the packet capture.
    """
    try:
        return float(capture[-1].sniff_timestamp) - float(capture[0].sniff_timestamp)
    except Exception as e:
        print(f"Error calculating capture duration: {e}")
        return None

def get_unique_ips(capture: pyshark.FileCapture, ip_type: str = "src") -> List[str]:
    """
    Extract unique source or destination IPs from the packet capture.
    """
    ips = set()

    try:
        for packet in capture:
            if ip_type == "src":
                ips.add(packet.ip.src)
            else:
                ips.add(packet.ip.dst)
        return list(ips)
    except AttributeError:
        # This handles cases where the packet does not have an IP layer
        return list(ips)
    except Exception as e:
        print(f"Error extracting unique IPs: {e}")
        return []

# Note: These utility functions are built upon the pyshark library. Ensure pyshark is installed and compatible.
