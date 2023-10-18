"""app.py
11. **Main Execution Logic**:
    - Parse command-line arguments (using argparse or another method).
    - Initialize `PacketAnalyzer` with the provided pcap file.
    - Depending on user's choice, execute the specific analysis.
    - Optionally, save results to a file.
"""

from settings import PCAP_FILE_PATH, SECURITY_ALERT_THRESHOLD, ...
from constants import PROTOCOL_TCP, PORT_HTTP, ...



from packet_analyzer import PacketAnalyzer

# Example usage:
if __name__ == "__main__":
    analyzer = PacketAnalyzer("path_to_pcap_file.pcap")
    analyzer.load_capture()
    analyzer.analyze('security')
    analyzer.analyze('statistics')
    # ... and so on for other analysis types