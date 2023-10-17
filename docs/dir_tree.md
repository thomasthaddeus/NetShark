.
├── LICENSE
├── requirements.txt
├── assets
│   ├── geoip_db
│   └── signatures
├── data
│   ├── logs
│   ├── out
│   └── pcaps
├── docs
│   ├── API.md
│   ├── class.md
│   ├── Libraries.md
│   ├── outline.md
│   └── PacketAnalyzer.md
├── scripts
│   ├── create_dir_structure.py
│   ├── create_utils.sh
│   ├── pyshark_scanner.py
│   └── scanner.py
├── src
│   ├── main.py
│   ├── analyzer
│   │   ├── application_analyzer.py
│   │   ├── behavior_analyzer.py
│   │   ├── content_analyzer.py
│   │   ├── crypto_analyzer.py
│   │   ├── network_topology_analyzer.py
│   │   ├── packet_analyzer.py
│   │   ├── performance_analyzer.py
│   │   ├── security_analyzer.py
│   │   ├── statistical_analyzer.py
│   │   └── traffic_analyzer.py
│   ├── config
│   │   ├── constants.py
│   │   └── settings.py
│   ├── detection
│   │   ├── anomaly_detector.py
│   │   ├── exfiltration_detector.py
│   │   └── privacy_network_detector.py
│   ├── forensics
│   │   ├── session_reconstructor.py
│   │   ├── signature_matcher.py
│   │   └── time_forensics.py
│   ├── scanner
│   │   ├── device_profiler.py
│   │   ├── geoip_resolver.py
│   │   ├── honeypot_connector.py
│   │   ├── __init__.py
│   │   └── malware_scanner.py
│   └── utils
│       ├── __init__.py
│       ├── ip_protocol_utils.py
│       ├── log_utils.py
│       ├── output_utils.py
│       └── pcap_utils.py
└── tests
    ├── test_packet_analyzer.py
    └── test_utils.py