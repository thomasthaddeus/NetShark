"""constants.py

Summary:
This module contains constant values used across the PacketAnalyzer tool.

Extended Summary:
For maintainability and clarity, constants are centralized in this module.
This ensures that they are not scattered throughout the code and can be
easily updated in one place. Constants might include fixed values related
to protocols, ports, specific strings, or any other value that remains
unchanged throughout the tool's execution.
"""

# Network Protocols
PROTOCOL_TCP = 6
PROTOCOL_UDP = 17
PROTOCOL_ICMP = 1

# Common Ports
PORT_HTTP = 80
PORT_HTTPS = 443
PORT_FTP = 21
PORT_DNS = 53

# Analysis Settings
MAX_PACKETS_TO_PROCESS = 10000  # Maximum number of packets to process in a single run.

# Error Messages
ERR_INVALID_PCAP = "The provided file is not a valid pcap or pcapng file."
ERR_UNSUPPORTED_PROTOCOL = "The protocol is not supported by this tool."

# Other Constants
DEFAULT_BUFFER_SIZE = 4096  # Buffer size for reading files, streams, etc.
