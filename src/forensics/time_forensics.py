"""time_forensics.py

Summary:
Module provides functionality for forensic analysis of timestamps within packet captures.

Extended Summary:
The TimeForensics class is dedicated to understanding the timing and sequence of packets/events.
It looks for anomalies in packet timestamps which might indicate tampering, time manipulation, or
other inconsistencies. Such analysis is vital in incident response and digital forensics.
"""

class TimeForensics:
    def __init__(self, packet_data):
        """
        Initializes the TimeForensics class with the packet data.

        Args:
            packet_data (List[Dict]): List of packets (typically as dictionaries) containing timestamp data.
        """
        self.packet_data = packet_data

    def analyze_sequence(self):
        """
        Analyze the sequence of packets to identify any out-of-order timestamps.

        Returns:
            List[Dict]: List of out-of-order packets with details.
        """
        anomalies = []
        for i in range(1, len(self.packet_data)):
            if self.packet_data[i]['timestamp'] < self.packet_data[i - 1]['timestamp']:
                anomalies.append({
                    'previous_packet': self.packet_data[i - 1],
                    'current_packet': self.packet_data[i]
                })

        return anomalies

    def identify_time_gaps(self, threshold=60):
        """
        Identify any large gaps in packet timestamps.

        Args:
            threshold (int): Threshold time gap in seconds to be considered an anomaly.

        Returns:
            List[Dict]: List of gaps with details.
        """
        gaps = []
        for i in range(1, len(self.packet_data)):
            time_gap = self.packet_data[i]['timestamp'] - self.packet_data[i - 1]['timestamp']
            if time_gap > threshold:
                gaps.append({
                    'gap_start': self.packet_data[i - 1],
                    'gap_end': self.packet_data[i],
                    'duration': time_gap
                })

        return gaps

    def detect_time_manipulation(self):
        """
        Detect potential time manipulation by looking for inconsistent clock jumps.

        Returns:
            List[Dict]: List of suspected time manipulations.
        """
        suspected_manipulations = []
        for i in range(2, len(self.packet_data)):
            prev_time_gap = self.packet_data[i - 1]['timestamp'] - self.packet_data[i - 2]['timestamp']
            current_time_gap = self.packet_data[i]['timestamp'] - self.packet_data[i - 1]['timestamp']

            if abs(prev_time_gap - current_time_gap) > (max(prev_time_gap, current_time_gap) * 0.5):
                suspected_manipulations.append({
                    'before_jump': self.packet_data[i - 2:i],
                    'after_jump': self.packet_data[i:i + 2]
                })

        return suspected_manipulations
