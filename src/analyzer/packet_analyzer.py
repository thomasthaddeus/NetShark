"""
2. **Main Class: `PacketAnalyzer`**
    - Purpose: Handle packet capture loading and orchestrate different types of analysis.

    **Attributes**:
    - file_path: path to the packet capture file.
    - cap: Loaded packet capture using pyshark.

    **Methods**:
    - `__init__(self, file_path)`: Constructor
    - `load_capture(self)`: Load packet capture using pyshark.
    - `summary(self)`: Print basic summary of the capture.
    - `analyze(self, analysis_type)`: Depending on the type of analysis, delegate to specific analysis classes.
"""

import pyshark

class PacketAnalyzer:

    def __init__(self, file_path: str):
        """
        Constructor for PacketAnalyzer.

        Parameters:
        - file_path (str): Path to the packet capture file.
        """
        self.file_path = file_path
        self.cap = None

    def load_capture(self):
        """
        Load packet capture using pyshark.
        """
        try:
            self.cap = pyshark.FileCapture(self.file_path)
        except Exception as e:
            print(f"Error loading packet capture from {self.file_path}: {e}")
            self.cap = None

    def summary(self):
        """
        Print basic summary of the capture.
        """
        if self.cap is None:
            print("Capture not loaded.")
            return

        total_packets = len(self.cap)
        print(f"Total Packets: {total_packets}")
        # You can expand on this method to show more summary details.

    def analyze(self, analysis_type: str):
        """
        Depending on the type of analysis, delegate to specific analysis classes.

        Parameters:
        - analysis_type (str): The type of analysis to be performed.
        """
        if self.cap is None:
            print("Capture not loaded.")
            return

        if analysis_type == "network":
            # Delegate to NetworkAnalyzer class (to be defined)
            pass
        elif analysis_type == "security":
            # Delegate to SecurityAnalyzer class (to be defined)
            pass
        # ... Add other analysis types as needed

        else:
            print(f"Unknown analysis type: {analysis_type}")

# Sample Usage:
# analyzer = PacketAnalyzer("/path/to/pcap/file.pcap")
# analyzer.load_capture()
# analyzer.summary()
# analyzer.analyze("network")
