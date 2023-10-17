import os

def create_directory(path):
    """Create directory if it doesn't exist."""
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created directory: {path}")
        else:
            print(f"Directory already exists: {path}")
    except PermissionError:
        print(f"Permission denied: Unable to create directory {path}.")
    except Exception as err:
        print(f"An error occurred while creating directory {path}: {str(err)}")

def create_file(path):
    """Create file if it doesn't exist."""
    try:
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as file:
                pass
            print(f"Created file: {path}")
        else:
            print(f"File already exists: {path}")
    except PermissionError:
        print(f"Permission denied: Unable to create file {path}.")
    except Exception as err:
        print(f"An error occurred while creating file {path}: {str(err)}")

ROOT_DIR = "../src"

# Creating directories
create_directory(ROOT_DIR)
directories = [
    "classes",
    "utils",
    "data",
    "config",
    "tests",
    "docs"
]
# Creating class files
class_files = [
    "packet_analyzer.py",
    "traffic_analyzer.py",
    "security_analyzer.py",
    "performance_analyzer.py",
    "network_topology_analyzer.py",
    "application_analyzer.py",
    "content_analyzer.py",
    "statistical_analyzer.py",
    "anomaly_detector.py",
    "signature_matcher.py",
    "behavior_analyzer.py",
    "session_reconstructor.py",
    "crypto_analyzer.py",
    "geoip_resolver.py",
    "time_forensics.py",
    "malware_scanner.py",
    "honeypot_connector.py",
    "privacy_network_detector.py",
    "exfiltration_detector.py",
    "device_profiler.py"
]
# Creating utility files
util_files = [
    "pcap_utils.py",
    "output_utils.py"
]
# Creating config files
config_files = [
    "settings.py",
    "constants.py"
]
# Creating main, requirements, gitignore, and LICENSE files
files = [
    "main.py",
    "requirements.txt",
    ".gitignore",
    "LICENSE"
]

for _ in directories:
    create_directory(os.path.join(ROOT_DIR, _))
for class_file in class_files:
    create_file(os.path.join(ROOT_DIR, "classes", class_file))
for util_file in util_files:
    create_file(os.path.join(ROOT_DIR, "utils", util_file))
for config_file in config_files:
    create_file(os.path.join(ROOT_DIR, "config", config_file))
for f in files:
    create_file(os.path.join(ROOT_DIR, f))

print("Directory structure creation attempt complete.")
