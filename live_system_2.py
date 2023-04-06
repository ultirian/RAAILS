
# https://github.com/manrajgrover/halo
# https://rich.readthedocs.io/en/stable/index.html
""" Class to set hostnames and run scans of hosts each function calls a scan from a scan group.
additional scans can be added to over time."""
#!/usr/bin/env python3

__author__ = 'Chris Weaver'
__version__ = '0.0.7'
__license__ = 'MIT'

import time
import nist_search as ns
import table_generator as tg
import nmap_scan_groups as nsg
import os

from set_host import SetHost
from nmap_command_engine import NMapRunner as run
from port_ident_tool import DataParser, IANAPortList
from halo import Halo
from rich.console import Console


class HostHolder:
    """
    https://docs.python.org/3/library/functions.html#classmethod

    A @classmethod is a decorator in Python that defines a method that is bound to 
    the class and not the instance of the class. When you define a method with 
    @classmethod, the first parameter of the method should be the class itself, 
    usually named cls by convention.

    In this code, all the methods are defined as class methods using the @classmethod 
    decorator, and they are accessing class-level variables host and ip using the cls 
    parameter. So, the methods defined using @classmethod will be able to access and 
    modify the class-level variables, which are shared across all instances of the class.

    Setters and getters are not the idea solution for this method, however object referencing 
    was holding back the dictonary switches and creating dependency across classes issues. 
    """
    host = None
    ip = None

    @classmethod
    def set_host(cls, host):
        """Set the host to be used for the rest of the program."""
        cls.host = host

    @classmethod
    def set_ip(cls, ip_addr):
        """Set the ip to be used for the rest of the program."""
        cls.ip = ip_addr

    @classmethod
    def get_host(cls):
        """Get the host to be used for the rest of the program."""
        return cls.host

    @classmethod
    def get_ip(cls):
        """Get the ip to be used for the rest of the program."""
        return cls.ip


class ScanSystem:
    """Class to set hostnames and run scans of hosts each function 
    calls a scan from a scan group."""
    def __init__(self):
        self.host_holder = HostHolder()

    def set_hostname(self):
        """Set the host to be used for the rest of the program. 
        You can either enter the IP address or the hostname.
        """
        set_host = SetHost()
        hostname, hosip = set_host.input_host_name()

        print(f"Host set to:{hostname} {hosip} \n")
        tg.print_host_ip_table(hostname, hosip)

        self.host_holder.set_host(hostname)
        self.host_holder.set_ip(hosip)

    def set_ip(self):
        """Set the host to be used for the rest of the program. 
        You can either enter the IP address or the hostname.
        """
        set_host = SetHost()
        hosip, hostname = set_host.input_host_ip()

        tg.print_host_ip_table(hostname, hosip)

        self.host_holder.set_host(hostname)
        self.host_holder.set_ip(hosip)

    def init_scan(self, scan_group_in):
        """Scan function to facilitate the scan, this passes in returns from defined methods
        from the switch case functions above."""
        # Calls host_holder class to get the host and ip.
        hostname = self.host_holder.get_host()
        hostip = self.host_holder.get_ip()

        # Checks if host ip is present. initally did hostname as well but local IPs have no
        # hostname. input validation automatically resolves ip and hostname so exception caught.
        if hostip is None:
            raise ValueError("\n \U0001F622 Host or IP not set \U0001F622 \n")

        with Halo(text='\n\n\n Running Scan...: \n\n\n', spinner='dots'):
            print("\n")
            tg.print_host_ip_table(hostname, hostip)

        with Halo(text='\n\n\n Running Scan...for service and port descovery...: \n\n\n',
                  spinner='dots',
                  color='green'):
            print("Using the following scan group: \n")

            tg.print_dictonary_table(scan_group_in)
            print("\n")

            start = time.perf_counter()

            args, data, stderr = run().scan_single_ip_ports(
                hosts_ip=hostip,
                scan_group=scan_group_in)

            finish = time.perf_counter()

        print(f'[bold blue]scan completed in {finish - start:0.4f} seconds [/]')

        print(f"Command Used: {args}\n")

        tg.print_nmap_parsed(data)

        # Calls the class method DataParser from port_ident_tool.py and parses through whole record
        # and returns a list of the following items the two items used are port_ids and cpes.
        addresses, port_ids, protocols, service_names, service_products, service_versions, \
            cpes = DataParser().parse_data_dict(data)

        # loops through all cpes and replaces / with 2.3 what is the current version of the CPE
        # then calls search_by_cpe_name from nist_search.py to search the NIST database.
        # the nist search then prints the output in table format.
        for sublist in cpes:
            for item in sublist:
                formated_cpe = item.replace("/", "2.3:")
                ns.search_by_cpe_name(formated_cpe)

        # This then compares the port_ids list to the IANA port list and prints the results.
        file_path = 'IANA_convertjson.json'

        # This then compares the port_ids list to the IANA port list and prints the results.
        with Halo(text='\n\n\n Running Scan...against NIST Database: \n\n\n', spinner='dots', color='red'):
            print('\n')
            record = IANAPortList.search_numbers_in_list_ret_record(
                file_path,
                port_ids)

        # Prints the results in table form.
        tg.print_iana_results(record)


class LiveSystem(ScanSystem):
    """This class will be used to run the live system scan."""

    def __init__(self, main_menu_callback):
        self.host_holder = HostHolder()
        self.console = Console()
        self.main_menu_callback = main_menu_callback

    def display_menu(self):
        """Display the menu for the live system."""
        while True:
            self.console.print("[red]1: Set Hostname[/]")
            self.console.print("[red]2: Set IP Address[/]")
            self.console.print("[red]3: Scan TCP Connect Scan[/]")
            self.console.print("[red]4: Scan TCP SYN scan top 1000 ports[/]")
            self.console.print("[red]5: Scan TCP SYN scan all ports[/]")
            self.console.print("[red]6: Scan TCP ACK Scan[/]")
            self.console.print("[red]7: Scan UDP Top 100 ports[/]")
            self.console.print("[blue]8: Return to main menu[/]")
            choice = self.console.input("~>: ")
            self.switch_case_livesystem(choice)
            if choice == "8":
                break

    def switch_case_livesystem(self, choice_in):
        """Switch case to call the correct function"""
        options = {
            "1": self.set_hostname,
            "2": self.set_ip,
            "3": self.nmap_external_tcp_connect_scan,
            "4": self.nmap_external_single_ip_1000,
            "5": self.nmap_external_tcp_sc_sv_os_allports,
            "6": self.nmap_external_tcp_ack_scan,
            "7": self.nmap_external_udp_top_100,
            "8": self.main_menu
        }
        # Call the function based on the user's input
        func = options.get(choice_in, lambda: print("\U0001F622 Invalid choice \U0001F622"))
        return func()

    def main_menu(self):
        """Display the main menu."""
        # loops self.console menu
        while True:
            self.console.print("\n[bold white]Main Menu[/]")
            self.console.print("[bold green]1: Learning Test System[/]")
            self.console.print("[bold red]2: Live System[/]")
            self.console.print("[bold blue]3: Exit[/]")
            # get user input
            choice = self.console.input("~>: ")
            # Call the switch_case method based on the user's input
            return self.main_menu_callback.switch_case_toplevel(choice)

    def nmap_external_tcp_connect_scan(self):
        """TCP CONNECT SCAN"""
        scan_group = nsg.NMAP_EXTERNAL_ST
        try:
            self.init_scan(scan_group)
        except ValueError as error:
            print(error)

    def nmap_external_single_ip_1000(self):
        """TCP SYN SCAN TOP 1000 PORTS"""
        scan_group = nsg.NMAP_EXTERNAL_SS_SC_SV_OS_1000
        try:
            self.init_scan(scan_group)
        except ValueError as error:
            print(error)

    def nmap_external_tcp_ack_scan(self):
        """TCP ACK SCAN"""
        scan_group = nsg.NMAP_EXTERNAL_SA
        try:
            self.init_scan(scan_group)
        except ValueError as error:
            print(error)

    def nmap_external_tcp_sc_sv_os_allports(self):
        """TCP SYN SCAN, SERVICE VERSION, OS DETECTION, ALL PORTS"""
        scan_group = nsg.NMAP_EXTERNAL_SCAN_SC_SV_OS_ALLPORTS
        try:
            self.init_scan(scan_group)
        except ValueError as error:
            print(error)

    def nmap_external_udp_top_100(self):
        """UDP TOP 100 PORTS"""
        scan_group = nsg.NMAP_EXTERNAL_SU_V_F
        try:
            self.init_scan(scan_group)
        except ValueError as error:
            print(error)
