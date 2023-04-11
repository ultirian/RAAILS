#!/usr/bin/env python3

""" Scan groups for easy calling of nmap scans and descriptors """

__version__ = '0.0.3'
__license__ = 'MIT'
# TCP SYN scan all ports, tries to guess the operating system. 
# does not do dns resolution for local network
# as assumed no dns server is assumed on local network.
# https://nmap.org/book/synscan.html
NMAP_HOME_NETWORK_DEFAULT_FLAGS = {
    """
    Scan to scan a home network, Using a TCP SYN scan, all ports, 
    tries to guess the operating system.
    """
    '-n': 'Never do DNS resolution',
    '-sS': 'TCP SYN scan, SYN “Half-open” Scan',
    '-p-': 'All ports',
    '-sV': 'Probe open ports to determine service/version info',
    '-O': 'OS Probe. Requires sudo/ root',
    '-T5': 'Aggressive timing template',
    '-PE': 'Enable this echo request behavior. Good for internal networks',
    '--version-intensity 5': 'Set version scan intensity. Default is 7',
    '--disable-arp-ping': 'No ARP or ND Ping, In the case a router is using proxy ARP this will cause false positives',
    '--max-hostgroup 20': 'Hostgroup (batch of hosts scanned concurrently) size',
    '--min-parallelism 10': 'Number of probes that may be outstanding for a host group',
    '--osscan-limit': 'Limit OS detection to promising targets this is more usefull if a open and closed port is found',
    '--max-os-tries 1': 'Maximum number of OS detection tries against a target',
    # https://nmap.org/book/output-formats-xml-output.html
    '-oX -': 'Send XML output to STDOUT, avoid creating a temp file'
}
# TCP SYN scan top 1000 ports
NMAP_EXTERNAL_SS_SC_SV_OS_1000 = {
    '-sS': 'TCP SYN scan, SYN “Half-open” Scan',
    '--top-ports 1000': 'Scan top 1000 ports',
    '-sV': 'Probe open ports to determine service/version info',
    '-O': 'OS Probe. Requires sudo/ root',
    '-T5': 'Aggressive timing template',
    '--min-parallelism 10': 'Number of probes that may be outstanding for a host group',
    '-oX -': 'Send XML output to STDOUT, avoid creating a temp file'
}
# TCP Connect Scan (-sT)    https://nmap.org/book/scan-methods-connect-scan.html
NMAP_EXTERNAL_ST = {
    '-sT': 'TCP Connect Scan',
    '-T5': 'Aggressive timing template',
    '-p-': 'All ports',
    '-oX -': 'Send XML output to STDOUT, avoid creating a temp file',
}

# TCP ACK Scan (-sA)        https://nmap.org/book/scan-methods-ack-scan.html
NMAP_EXTERNAL_SA = {
    '-sA': 'TCP ACK Scan',
    '-T5': 'Aggressive timing template',
    '-p-': 'All ports',
    '-oX -': 'Send XML output to STDOUT, avoid creating a temp file',
}
# UDP Scan (-sU)            https://nmap.org/book/scan-methods-udp-scan.html
NMAP_EXTERNAL_SU_V_F = {
    '-sUV': 'UDP Scan with version detection',
    '-F': 'Fast scan, scan top 100 ports',
    '-T5': 'Aggressive timing template',
    '--min-hostgroup 50': 'Hostgroup (batch of hosts scanned concurrently) size',
    '-oX -': 'Send XML output to STDOUT, avoid creating a temp file'
}
# Can be very slow
NMAP_EXTERNAL_SU_V = {
    '-sUV': 'UDP Scan with version detection',
    '-F': 'Fast scan, scan top 100 ports',
    '-T5': 'Aggressive timing template',
    '--min-hostgroup 50': 'Hostgroup (batch of hosts scanned concurrently) size',
    '-oX -': 'Send XML output to STDOUT, avoid creating a temp file'
}
# IP Protocol Scan (-sO)    https://nmap.org/book/synscan.html
# TCP FTP Bounce Scan (-b)  https://nmap.org/book/scan-methods-ftp-bounce-scan.html

# TCP Null Scan             nmap -sN <target>

# TCP Ping Scan             nmap -sn -PS <target>
NMAP_HOME_NETWORK_PING_SWEEP = {
    '-n': 'Never do DNS resolution',
    '-sn': 'Ping sweep the network',
    '-oX -': 'Send XML output to STDOUT, avoid creating a temp file'
}

NMAP_EXTERNAL_SCAN_SC_SV_OS = {
    '-T4': 'Aggressive timing template, this is the default for nmap',
    '--top-ports 1000': 'Scan top 1000 ports',
    '-sC': 'equivalent to --script=default this runs the default scripts for nmap https://nmap.org/nsedoc/categories/default.html',
    '-sV': 'Probe open ports to determine service/version info this can be helpfull for finding old service vlunrabilities',
    '-O': 'Enable OS detection singular scan for OS can be ommited with -A if grouping scans together',
    '-oX -': 'Send XML output to STDOUT, avoid creating a temp file'
}

NMAP_EXTERNAL_SCAN_SC_SV_OS_ALLPORTS = {
    '-T4': 'Aggressive timing template, this is the default for nmap',
    '-p-': 'Scan all ports',
    '-sC': 'equivalent to --script=default this runs the default scripts for nmap https://nmap.org/nsedoc/categories/default.html',
    '-sV': 'Probe open ports to determine service/version info this can be helpfull for finding old service vlunrabilities',
    '-O': 'Enable OS detection singular scan for OS can be ommited with -A if grouping scans together',
    '-oX -': 'Send XML output to STDOUT, avoid creating a temp file'
}

# scan range with last 3 nums 1-254

NMAP_EXTERNAL_SCAN_SC_SV_OS_RANGE_1_254 = {
    '-T4': 'Aggressive timing template, this is the default for nmap',
    '-oX -': 'Send XML output to STDOUT, avoid creating a temp file'
}
