"""ip_protocol_utils.py

8. **`resolve_ip(ip_address)`**:
    - Purpose: Resolve an IP address to its domain name (if possible).
    - Parameters:
        - `ip_address`: The IP address to resolve.

9. **`get_protocol_name(protocol_number)`**:
    - Purpose: Get the textual name of a protocol given its number.
    - Parameters:
        - `protocol_number`: The number representing the protocol.
"""

import json
import socket

# Load protocol mappings from the JSON file
with open(file="protocols.json", mode="r", encoding='utf-8') as file:
    PROTOCOLS = json.load(file)

def resolve_ip(ip_address: str) -> str:
    """
    Resolve an IP address to its domain name (if possible).
    """
    try:
        return socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        # Unable to resolve the IP to a domain
        return ip_address
    except Exception as e:
        print(f"Error resolving IP address {ip_address}: {e}")
        return ip_address

def get_protocol_name(protocol_number: int) -> str:
    """
    Get the textual name of a protocol given its number.
    """
    return PROTOCOLS.get(str(protocol_number), f"UNKNOWN-{protocol_number}")

# Sample usage:
# print(resolve_ip("8.8.8.8"))
# print(get_protocol_name(6))
