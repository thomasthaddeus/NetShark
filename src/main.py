"""main.py
**Main Class: `PacketAnalyzer`**
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
