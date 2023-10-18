"""signature_matcher.py

Summary:
Module provides functionality to match packets against a database of known signatures of malicious activity.

Extended Summary:
The SignatureMatcher class is designed to detect potential malicious activities in packet captures by comparing packet data
against a database of known malicious signatures. This method of detection, while not exhaustive, can quickly identify known threats.
"""

import json

class SignatureMatcher:
    def __init__(self, packet_data, signature_db_path="signatures.json"):
        """
        Initializes the SignatureMatcher with the packet data to analyze and the path to the signature database.

        Args:
            packet_data (List[Dict]): List of packets (typically as dictionaries).
            signature_db_path (str): Path to the signature database file.
        """
        self.packet_data = packet_data
        self.signature_db_path = signature_db_path
        self.signatures = self.load_signatures()

    def load_signatures(self):
        """
        Load signatures from the signature database.

        Returns:
            Dict: Loaded signatures.
        """
        with open(self.signature_db_path, 'r') as file:
            return json.load(file)

    def match_signatures(self):
        """
        Match packet data against the loaded signatures.

        Returns:
            List[Dict]: List of matched signatures with corresponding packet data.
        """
        matches = []

        for packet in self.packet_data:
            for sig_name, signature in self.signatures.items():
                # This is a basic string matching example. In reality, the matching logic may be more complex.
                if signature in packet.values():
                    matches.append({
                        'signature_name': sig_name,
                        'matched_packet': packet
                    })

        return matches

    def update_signature(self, sig_name, new_signature):
        """
        Update a specific signature in the signature database.

        Args:
            sig_name (str): Name of the signature to update.
            new_signature (Dict): New signature data.
        """
        self.signatures[sig_name] = new_signature
        with open(self.signature_db_path, 'w') as file:
            json.dump(self.signatures, file, indent=4)

    def add_signature(self, sig_name, signature):
        """
        Add a new signature to the signature database.

        Args:
            sig_name (str): Name of the new signature.
            signature (Dict): Signature data.
        """
        self.signatures[sig_name] = signature
        with open(self.signature_db_path, 'w') as file:
            json.dump(self.signatures, file, indent=4)

    def remove_signature(self, sig_name):
        """
        Remove a signature from the signature database.

        Args:
            sig_name (str): Name of the signature to remove.
        """
        if sig_name in self.signatures:
            del self.signatures[sig_name]
            with open(self.signature_db_path, 'w') as file:
                json.dump(self.signatures, file, indent=4)
