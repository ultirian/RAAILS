#!/usr/bin/env python3

"""RAAILS Learning System proof of concept. Two test functions with outputs added, 
However adding a database to call verbose print statements may help order information using a lib
such as SQL Alchemy and a database such as MySQL or SQLite. This will be a future feature."""

__author__ = 'Chris Weaver'
__version__ = '0.0.7'
__license__ = 'MIT'

import time
import nist_search as ns
import table_generator as tg
import nmap_scan_groups as nsg
import os

from nmap_command_engine import NMapRunner as run
from port_ident_tool import DataParser, IANAPortList
from halo import Halo
from rich.console import Console


class SystemScanner:
    """This class will be used to scan the system for ports and services."""
    def scan_test_server(self):
        """Scan the test server, this will be a remote VM host that rotates 5 random ports every
        5 minutes the server is up for testing initally only, the text below is prototype text."""

        console = Console()
        console.print(
            "[bold green]************************************************************[/]")
        console.print(
            "[bold green]This scan will look for a preset test server on the internet[/]")
        console.print(
            "[bold green]\N{battery}INTERNET NOT INCLUDED\N{battery}                 [/]")
        console.print(
            "[bold green]************************************************************[/]")
        console.print(
            "[bold green]The scan used will is a TCP SYN Scan! TOP 1000 Ports        [/]")
        console.print(
            "[bold green]Your computer requests a connection to the server:SYN       [/]")
        console.print(
            "[bold blue]\N{thinking face} --------------------->[/]\N{vibration mode}")
        console.print(
            "[bold green]Then the serer states the port is open and go ahead:SYN/ACK [/]")
        console.print(
            "[bold blue]\N{face with monocle} <---------------------[/]\N{vibration mode}")
        console.print(
            "[bold green]But then you close the port and the connection is dropped:RST[/]")
        console.print(
            "[bold red]\N{nerd face} NO THX!<--------------[/]\N{vibration mode}")
        console.print(
            "[bold green] But because of this we know the port is open! Result!      [/]")
        console.print(
            "[bold green] If it is closed the scan will end with a RST Flag.         [/]")
        console.print(
            "[bold green]Check out the following links for more details:\n[/]")
        console.print("https://nmap.org/book/synscan.html")
        console.print("https://www.rfc-editor.org/rfc/rfc9293")

        time.sleep(5)

        console.print(
            "[bold green]It is important to note that this software uses NMAP,       [/]")
        console.print(
            "[bold green]NMAP Is a powerful scanning tool with many scanning tools,  [/]")
        console.print(
            "[bold green]Its worth googling this tool and becoming familiar with the [/]")
        console.print(
            "[bold green]many options it has.                                        [/]")

        time.sleep(5)

        console.print(
            "[bold green]This scan will take a few minutes, please be patient.       [/]")
        LearningSystem.nmap_external_single_ip_1000_azure(self)

        console.print("\n")
        console.print(
            "[bold green]************************************************************[/]")
        console.print(
            "[bold green]The scan has completed, please review the results above.    [/]")
        console.print(
            "[bold green]************************************************************[/]")
        console.print(
            "What are CPEs?           https://nvd.nist.gov/products/cpe")
        console.print(
            "What are CVEs?           https://www.cve.org/About/Overview")
        console.print(
            "What are CVSS Scores?    https://www.first.org/cvss/specification-document")
        console.print("What is NIST?            https://www.nist.gov/")
        console.print("SOLID START!\N{nerd face}")
        console.print("\n")

    def scan_nmap_server(self):
        """Scan a remote machine, this will be scanme.nmap.org due to the explit permission
        given by the owner of the machine in the nmap documentation. The text below is 
        prototype text, this will be replaced with a more professional message and potentially
        added to a sql database for expansion and more features."""

        console = Console()
        console.print(
            "[bold green]************************************************************[/]")
        console.print(
            "[bold green]This scan will scan nmaps scanme.nmap.org                   [/]")
        console.print(
            "[bold green]\N{battery}INTERNET NOT INCLUDED\N{battery}                 [/]")
        console.print(
            "[bold green]\N{battery}Be aware, this is a public server                [/]")
        console.print(
            "[bold green]\N{battery}https://nmap.org/book/man-examples.html          [/]")
        console.print(
            "[bold green]\N{battery}Check link for terms of use.                     [/]")
        console.print(
            "[bold green]************************************************************[/]")
        console.print(
            "[bold green]\N{battery}\N{battery}\N{battery}\N{battery}\N{battery}     [/]")
        console.print(
            "[bold green]************************************************************[/]")
        console.print(
            "[bold green]The scan used will is a TCP SYN Scan! TOP 1000 Ports        [/]")
        console.print(
            "[bold green]Your computer requests a connection to the server:SYN       [/]")
        console.print(
            "[bold blue]\N{thinking face} --------------------->[/]\N{vibration mode}")
        console.print(
            "[bold green]Then the serer states the port is open and go ahead:SYN/ACK [/]")
        console.print(
            "[bold blue]\N{face with monocle} <---------------------[/]\N{vibration mode}")
        console.print(
            "[bold green]But then you close the port and the connection is dropped:RST[/]")
        console.print(
            "[bold red]\N{nerd face} NO THX!<--------------[/]\N{vibration mode}")
        console.print(
            "[bold green] But because of this we know the port is open! Result!      [/]")
        console.print(
            "[bold green] If it is closed the scan will end with a RST Flag.         [/]")
        console.print(
            "[bold green]Check out the following links for more details:\n[/]")
        console.print("https://nmap.org/book/synscan.html")
        console.print("https://www.rfc-editor.org/rfc/rfc9293")

        time.sleep(5)

        console.print(
            "[bold green]It is important to note that this software uses NMAP,       [/]")
        console.print(
            "[bold green]NMAP Is a powerful scanning tool with many scanning tools,  [/]")
        console.print(
            "[bold green]Its worth googling this tool and becoming familiar with the [/]")
        console.print(
            "[bold green]many options it has.                                        [/]")

        time.sleep(5)

        console.print(
            "[bold green]This scan will take a few minutes, please be patient.       [/]")
        LearningSystem.nmap_external_single_ip_1000_scanme(self)

        console.print("\n")
        console.print(
            "[bold green]************************************************************[/]")
        console.print(
            "[bold green]The scan has completed, please review the results above.    [/]")
        console.print(
            "[bold green]************************************************************[/]")
        console.print(
            "What are CPEs?           https://nvd.nist.gov/products/cpe")
        console.print(
            "What are CVEs?           https://www.cve.org/About/Overview")
        console.print(
            "What are CVSS Scores?    https://www.first.org/cvss/specification-document")
        console.print("What is NIST?            https://www.nist.gov/")
        console.print("SOLID START!\N{nerd face}")
        console.print("\n")


class LearningSystem(SystemScanner):
    """Learning test system class inherits from SystemScanner Class"""

    def __init__(self, main_menu_callback):
        self.console = Console()
        self.main_menu_callback = main_menu_callback

    def display_menu(self):
        """Display the learning test system menu"""
        while True:
            self.console.print("[green] 1: Scan Test Server")
            self.console.print("[green] 2: Scan scanme.nmap.org")
            self.console.print("[blue] 3: Return to main menu")
            choice = self.console.input("~>: ")
            self.switch_case_learning_system(choice)
            if choice == "3":
                break

    def switch_case_learning_system(self, choice_in):
        """Switch case to call the correct function"""
        options = {
            "1": self.scan_test_server,
            "2": self.scan_nmap_server,
            "3": self.main_menu
        }
        func = options.get(
            choice_in, lambda: self.console.print("Invalid choice"))
        func()

    def main_menu(self):
        """Return to main menu"""
        # loops console menu
        while True:
            self.console.print("\n[bold white]Main Menu[/]")
            self.console.print("[bold green]1: Learning Test System[/]")
            self.console.print("[bold red]2: Live System[/]")
            self.console.print("[bold blue]3: Exit[/]")
            # get user input
            choice = self.console.input("~>: ")
            # Call the switch_case method based on the user's input
            return self.main_menu_callback.switch_case_toplevel(choice)

    def init_scan_azure_vm(self, hostname: str, hostip: str, scan_group_in: dict) -> None:
        """Scan function to facilitate the scan, this passes in returns from defined methods
        from the switch case functions above."""

        def ping_server(ip: str, timeout: int) -> bool:
            response = os.system(f"ping -n 1 -w {timeout} {ip} >nul 2>&1" if os.name == "nt" else f"ping -c 1 -W {timeout} {ip} > /dev/null 2>&1")
            return response == 0

        # Ping the server and end the scan if there is no response
        if not ping_server(hostip, 1000):
            print(f"\n \u26A0\ufe0f   No response from {hostip}. Ending scan. \u26A0\ufe0f")
            return

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

        print(f'scan completed in {finish - start:0.4f} seconds')

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
        with Halo(text='\n\n\n Running Scan...against NIST Database: \n\n\n', spinner='dots', color='red'):
            print('\n')

        # File path to the modified IANA port list json file.
        file_path = 'learning_system_port_desc.json'


        # This then compares the service_names list to the IANA port list and returns the results.
        # as a json object and stores the return in a varible.
        record = IANAPortList.search_numbers_in_list_ret_record(
            file_path,
            port_ids)

        print(f'this is the OBJ: {record}')

        tg.print_port_results_learning(record)

    def nmap_external_single_ip_1000_azure(self):
        """TCP SYN SCAN TOP 1000 PORTS"""
        hostname = "Remote Azure VM Test Server"
        hostip = "20.28.241.117"
        scan_group = nsg.NMAP_EXTERNAL_SS_SC_SV_OS_1000
        self.init_scan_azure_vm(hostname, hostip, scan_group)

    def nmap_external_single_ip_1000_scanme(self):
        """TCP SYN SCAN TOP 1000 PORTS"""
        hostname = "scanme.nmap.org"
        hostip = "45.33.32.156"
        scan_group = nsg.NMAP_EXTERNAL_SS_SC_SV_OS_1000
        self.init_scan_azure_vm(hostname, hostip, scan_group)
