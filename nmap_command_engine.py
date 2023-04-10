#!/usr/bin/env python3

"""
Nmap Command Engine is a python script that will run 
nmap and parse the output into a dictionary of data.
"""

# https://docs.python.org/3/library/shlex.html
import shlex
# https://docs.python.org/3/library/os.html
import os
# https://docs.python.org/3/library/shutil.html
import shutil
# https://docs.python.org/3/library/subprocess.html
import subprocess
import xml_parser

class NMapRunner:
    """
    Run nmap and return the results
    """
    def __init__(self):
        self.nmap_report_file = None
        self.sudo = None
        self.nmap = None

        # check if running on Windows (For Windows nmap.exe is used)
        if os.name == 'nt':
            nmap = shutil.which('nmap.exe', mode=os.F_OK | os.X_OK)
        else:
            nmap = shutil.which('nmap', mode=os.F_OK | os.X_OK)

        if not nmap:
            raise ValueError("Nmap is not installed on this system")
        self.nmap = nmap

        # check if not running on Windows (sudo is not available on Windows) try for Linux.
        if os.name != 'nt':
            sudo = shutil.which('sudo', mode=os.F_OK | os.X_OK)
            if not sudo:
                raise ValueError("Sudo is not installed on this system")
            self.sudo = sudo

    def scan_single_ip_ports(self, *, hosts_ip: str, sudo: bool = True, scan_group: dict):
        """Run nmap and return the results as func"""
        command = []
        if sudo and self.sudo:
            command.append(self.sudo)
        command.append(self.nmap)

        # Join command from nmap_scan_groups.py
        command_in = shlex.split(" ".join(scan_group.keys()))
        command.extend(command_in)

        # Append hosts_ip to end of command
        command.append(hosts_ip)

        completed = subprocess.run(
            command, capture_output=True, shell=False, check=True)
        completed.check_returncode()
        xml_parse_in = xml_parser.DetailedOutputParser()
        args, data = xml_parse_in.parse_nmap_xml(
            completed.stdout.decode('utf-8'))

        return args, data, completed.stderr

