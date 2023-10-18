"""scanner.py
Summary:
    A script to extract specific details (such as IVs and TCP checksums) from a
    pcap file.

Extended Summary:
    This script utilizes the pyshark library to analyze packet captures and
    extract specific details such as the number of IVs, the IV for the first
    packet, and the TCP checksum for the first packet.
"""

import sys
import subprocess
import pyshark

def check_install():
    """
    TODO: This function should check whether the appropriate software is installed in the environment before attempting to decrypt the pcap data.
    """
    pass

def check_permissions():
    """
    TODO: This function should check that the user has the appropriate permissions to run the programs associated with the extraction process.
    TODO: If admin permission is needed raise to user and break process.
    """
    pass


def decrypt_pcap(file_path, key, encryption_type="wep"):
    """
    Decrypts a pcap file using the provided WEP key or WPA passphrase.

    Args:
        file_path (str): Path to the pcap file.
        key (str): WEP key or WPA passphrase.
        encryption_type (str): Either 'wep' or 'wpa'. Default is 'wep'.

    Returns:
        str: Path to the decrypted pcap file (will have "-dec" appended to the original filename).
    """
    output_file = file_path.replace(".pcap", "-dec.pcap")

    if encryption_type == "wep":
        cmd = ["airdecap-ng", "-w", key, "-l", output_file, file_path]
    elif encryption_type == "wpa":
        cmd = ["airdecap-ng", "-p", key, "-l", output_file, file_path]
    else:
        raise ValueError("Invalid encryption type. Choose either 'wep' or 'wpa'.")

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as err:
        print(f"Error during decryption: {err}")
        return None

    return output_file


def get_wlan_details(cap):
    """
    Extracts details about the WLAN packets in the provided capture.

    Args:
        cap (pyshark.file.capture.FileCapture): The packet capture to analyze.

    Returns:
        tuple: Total number of IVs (int) and the IV of the first packet (str).
    """
    total_ivs = 0
    first_iv = None

    for packet in cap:
        if "wlan" in packet and "wlan.iv" in packet:
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
        str or None: TCP checksum of the first TCP packet or None if not found.
    """
    for packet in cap:
        if "tcp" in packet and "tcp.checksum" in packet:
            return packet.tcp.checksum
    return None


def get_aircrack_info(cap):
    """
    Scans the packet capture for details pertinent to Aircrack-ng: BSSID and ESSID.

    Args:
        cap (pyshark.file.capture.FileCapture): The packet capture to analyze.

    Returns:
        dict: Dictionary containing the BSSID and ESSID. Returns None if not found.
    """
    info = {"BSSID": None, "ESSID": None}

    for packet in cap:
        if "wlan" in packet.layers:
            # Check if it's a beacon frame or probe response frame
            if hasattr(
                packet.wlan, "fc_type_subtype"
            ) and packet.wlan.fc_type_subtype in ["8", "5"]:
                # Get BSSID
                if hasattr(packet.wlan, "bssid"):
                    info["BSSID"] = packet.wlan.bssid

                # Get ESSID
                if hasattr(packet.wlan, "ssid"):
                    info["ESSID"] = packet.wlan.ssid

                # If both BSSID and ESSID are found, break
                if info["BSSID"] and info["ESSID"]:
                    break

    if not info["BSSID"] and not info["ESSID"]:
        return None

    return info


def crack_pcap():
    """
    TODO: implement with aircrack-ng support
    TODO: add calls to bash scripts to run the appropriate program

    Note: Extracting WEP key directly from a pcap is not straightforward and
    typically requires a separate cracking procedure. pcap files usually
    don't contain the WEP key in plaintext.
    """
    pass


def main():
    """
    Main function to drive the script.

    Loads a pcap file, extracts specific details from the capture, and prints
    them.
    """
    pcap_file_path = "./PCAP2.cap"
    key = "DEAD10CCD15EA5ECDCC2D67ACA"

    # Decrypt the pcap file
    decrypted_file = decrypt_pcap(
        pcap_file_path, key, encryption_type="wpa"
    )  # Change to "wpa" if using WPA

    # Check if decryption was successful
    if not decrypted_file:
        print("Failed to decrypt the pcap file.")
        sys.exit(1)

    try:
        cap = pyshark.FileCapture(pcap_file_path)

        # Get Aircrack-ng related details
        aircrack_details = get_aircrack_info(cap)

        # Get WLAN details
        total_ivs, first_iv = get_wlan_details(cap)

        # Get first TCP checksum
        first_tcp_checksum = get_first_tcp_checksum(cap)

        if aircrack_details:
            print(f"BSSID: {aircrack_details['BSSID']}")
            print(f"ESSID: {aircrack_details['ESSID']}")
        else:
            print("Failed to extract BSSID and ESSID from the pcap file.")
        print(f"Total IVs in the capture: {total_ivs}")
        print(f"IV for the first packet: {first_iv}")
        print(f"TCP checksum for the first packet: {first_tcp_checksum}")
    except FileNotFoundError:
        print(f"Error: The pcap file '{pcap_file_path}' was not found.")
        sys.exit(1)
    except Exception as err:
        print(f"An error occurred: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
