"""settings.py

Summary:
This module centralizes configuration settings for the PacketAnalyzer tool.

Extended Summary:
This module contains various configuration options and default settings
for the PacketAnalyzer tool. These include paths to necessary files,
thresholds for analysis, connection details, and more. By centralizing
these settings, we ensure consistency across the tool and make it easier
to update configurations without delving into the main logic.
"""

# Paths
PCAP_FILE_PATH = "/path/to/default.pcap"
MALICIOUS_IP_DB_PATH = "/path/to/malicious_ips.db"

# Analysis Settings
SECURITY_ALERT_THRESHOLD = 5  # Number of suspicious activities before raising an alert.
TRAFFIC_ANALYSIS_INTERVAL = "1m"  # Default interval for traffic trend analysis (e.g., "1s", "1m", "1h").
MAX_PACKET_SIZE = 1500  # Maximum size of a packet in bytes for certain analysis.

# Database Connection Details (If you're storing analysis results)
DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "username"
DB_PASS = "password"
DB_NAME = "packet_analysis"

# External Services (e.g., for updating the malicious IP database or sending notifications)
EXTERNAL_API_KEY = "your_api_key_here"

# Logging Configuration
LOG_FILE_PATH = "/path/to/logfile.log"
LOG_LEVEL = "INFO"

# Other Settings
BASE64_DECODE = True  # Automatically decode base64 content when analyzing.
