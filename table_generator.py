#!/usr/bin/env python3

""" Functions for printing tables to the console"""
__author__ = 'Chris Weaver'
__version__ = '0.0.6'
__license__ = 'MIT'
# https://rich.readthedocs.io/
from rich.console import Console
from rich.table import Table


console = Console()

def print_host_ip_table(hostname, hostip):
    """Prints Host IP to confirm scan is running on correct host"""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Host")
    table.add_column("IP")

    table.add_row(hostname, hostip)
    console.print("\n")
    console.print(table)

# Prints table from dictionary in nmap_scan_groups.py

def print_dictonary_table(dict_to_print):
    """print_dictonary_table"""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Switch", style="dim", width=22)
    table.add_column("Description")
    for switch, description in dict_to_print.items():
        table.add_row(switch, description)
    console.print("\n")
    console.print(table)

# Prints table from Nmap parsed data from xml_parser.py
def print_nmap_parsed(parsed_to_print):
    """print_nmap_parsed to table data in is a list of dictionaries
    this function adds columns and rows to the table and popuuates/prints"""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Address")
    table.add_column("Port ID")
    table.add_column("Protocol")
    table.add_column("Service Name")
    table.add_column("Service Product")
    table.add_column("Service Version")
    table.add_column("CPES")

    for item in parsed_to_print:
        address = item['address']
        for port in item['ports']:
            port_id = port['port_id']
            protocol = port['protocol']
            service_name = port['service_name']
            service_product = port['service_product']
            service_version = port['service_version']
            cpes = ", ".join(port['cpes'])
            table.add_row(
                address,
                port_id,
                protocol,
                service_name,
                service_product,
                service_version,
                cpes
            )

    console.print("\n")
    console.print(table)

def print_nist_tables(id_list, score_list, description_list):
    """Prints NIST result tables"""

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("CVE ID")
    table.add_column("CVSS Score")
    table.add_column("CVE Description")
    for id, score, description in zip(id_list, score_list, description_list):
        # score is seen as a "float" so needs to be converted to a string
        table.add_row(id, str(score), description)

    console.print("\n")
    console.print(table)

def print_iana_results(result):
    """Print the port search results as a table for IANA_convert.json"""
    table = Table(title="Port Search Results")
    table.add_column("Number")
    table.add_column("Protocol")
    table.add_column("Description")
    table.add_column("XRefs")
    for record in result:
        xrefs = ",".join([f"{xref['_type']}: {xref['_data']}" for xref in record['xref']])
        table.add_row(record['number'], record['protocol'], record['description'], xrefs)
    console = Console()

    console.print("\n")
    console.print(table)

def print_port_results_learning(result):
    """Print search results in a table from learning_system_port_desc.json"""
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Protocol", style="dim", width=6, min_width=6, max_width=10)
    table.add_column("Description", style="dim", width=30, min_width=30, max_width=30)
    table.add_column("Port", style="dim", width=6, min_width=2, max_width=6)
    table.add_column("Service", style="dim", width=10, min_width=10, max_width=10)
    table.add_column("RFC", style="dim", width=10, min_width=10, max_width=15)
    table.add_column("Link", style="dim")
    
    for record in result:
        table.add_row(
            record["protocol"],
            record["description"],
            record["number"],
            record["name"],
            record["RFC"],
            record["link"]
        )
    console.print("\n")
    console.print(table)
