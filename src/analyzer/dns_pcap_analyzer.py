"""dns_pcap_analyzer.py
_summary_

_extended_summary_

Returns:
    _type_: _description_

TODO: Add try-except blocks in methods to handle potential exceptions during packet analysis.
TODO: Add docstrings and comments to explain the purpose and functionality of each method.
TODO: Incorporate logging to capture important events, errors, or exceptions during the analysis.
TODO: Write unit tests to verify the functionality of the methods in DNSPcapAnalyzer class.
"""

import pyshark
import toml

class DNSPcapAnalyzer:
    def __init__(self, pcap_file):
        self.pcap_file = pcap_file
        # TODO: Add try-except block to handle potential exceptions when reading the pcap file.
        self.cap = pyshark.FileCapture(self.pcap_file)


    def get_dns_resolver(self):
        for pkt in self.cap:
            if hasattr(pkt, 'dns'):
                return pkt.ip.src
        return None

    def get_resolver_organization(self, ip_addr):
        # TODO: Implement logic using an external service or database to map the IP address to an organization.
        pass


    def get_ip_for_domain(self, domain):
        for pkt in self.cap:
            if hasattr(pkt, 'dns') and pkt.dns.qry_name == domain:
                return pkt.dns.a
        return None

    def get_ipv6_for_domain(self, domain):
        for pkt in self.cap:
            if hasattr(pkt, 'dns') and pkt.dns.qry_name == domain:
                return pkt.dns.aaaa
        return None

    def get_mail_provider(self, domain):
        for pkt in self.cap:
            if hasattr(pkt, 'dns') and pkt.dns.qry_name.endswith(domain) and pkt.dns.qry_type == 'MX':
                return pkt.dns.resp_name
        return None

    def get_email_handle(self):
        # TODO: Refine logic to accurately find the email handle, as the current logic may not be reliable.
        for pkt in self.cap:
            if hasattr(pkt, 'dns') and pkt.dns.qry_type in ['TXT', 'MX']:
                return pkt.dns.qry_name
        return None


    def get_reverse_lookup_ip(self):
        for pkt in self.cap:
            if hasattr(pkt, 'dns') and pkt.dns.qry_type == 'PTR':
                return pkt.dns.qry_name
        return None


    def get_reverse_lookup_organization(self, ip_addr):
        # TODO: Implement logic using an external service or database to map the IP address to an organization.
        pass


    def get_primary_sip_fqdn(self):
        # TODO: Optimize logic to handle large pcap files more efficiently.
        sip_counts = {}
        for pkt in self.cap:
            if hasattr(pkt, 'sip') and hasattr(pkt.sip, 'host'):
                sip_counts[pkt.sip.host] = sip_counts.get(pkt.sip.host, 0) + 1
        return max(sip_counts, key=sip_counts.get, default=None)

    def get_backup_sip_fqdn(self):
        # TODO: Optimize logic to handle large pcap files more efficiently.
        sip_counts = {}
        for pkt in self.cap:
            if hasattr(pkt, 'sip') and hasattr(pkt.sip, 'host'):
                sip_counts[pkt.sip.host] = sip_counts.get(pkt.sip.host, 0) + 1
        # Remove the primary SIP FQDN from the counts
        primary_sip_fqdn = self.get_primary_sip_fqdn()
        if primary_sip_fqdn in sip_counts:
            del sip_counts[primary_sip_fqdn]
        return max(sip_counts, key=sip_counts.get, default=None)

    def get_all_info(self, domain, ip_address):
        # TODO: Extend method to include other information as needed.
        info = {
            'DNS Resolver IP': self.get_dns_resolver(),
            'Organization of DNS Resolver': self.get_resolver_organization(ip_address),
            f'IPv4 Address for {domain}': self.get_ip_for_domain(domain),
            f'IPv6 Address for {domain}': self.get_ipv6_for_domain(domain),
            f'Mail Provider for {domain}': self.get_mail_provider(domain),
            'IP Address Queried for Reverse Lookup': self.get_reverse_lookup_ip(),
            'Organization of IP Address Queried for Reverse Lookup': self.get_reverse_lookup_organization(ip_address),
            'Email Handle': self.get_email_handle(),
            'Primary SIP FQDN': self.get_primary_sip_fqdn(),
            'Backup SIP FQDN': self.get_backup_sip_fqdn(),
        }
        return info

    def print_info(self, domain, ip_address):
        info = self.get_all_info(domain, ip_address)
        for key, value in info.items():
            print(f'{key}: {value}')

if __name__ == "__main__":
    # TODO: Add error handling to manage potential issues when loading the config file or analyzing the pcap file.
    # Load configuration from TOML file
    config = toml.load('config.toml')
    pcap_config = config['pcap_analysis']

    # Create PcapAnalyzer instance and call print_info method
    pcap_analyzer = DNSPcapAnalyzer(pcap_config['pcap_file'])
    pcap_analyzer.print_info(pcap_config['domain'], pcap_config['ip_address'])
