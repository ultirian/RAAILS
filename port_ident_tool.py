#!/usr/bin/env python3

""" Port identidy and feedback Class, will be used for parsing a list 
of ports from live systems scan data stream and outputting what the 
port is useful for"""

__author__ = 'Chris Weaver'
__version__ = '0.0.1'
__license__ = 'MIT'

import json


class IANAPortList:
    """Load the IANA port list into a dictionary scan for key number
    and print the protocol and description of the port number"""
    @classmethod
    def search_numbers_in_list(cls, filename, numbers_list):
        """Load the IANA port list into a dictionary"""
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)
        for number in numbers_list:
            found = False
            for item in data['record']:
                if 'number' in item and str(item['number']) == str(number):
                    if 'description' in item:
                        description = item['description']
                    else:
                        description = "No description available"
                    print(
                        f"\nPort number {number} is a {item['protocol']} protocol. Description: {description}")
                    found = True
                    break
            if not found:
                print(f"Port: {number} has not been found in the IANA list")

    @classmethod
    def search_numbers_in_list_ret_record(cls, filename, numbers_list):
        """Loads json file and numbers and returns json record found"""
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)
        result = []
        for number in numbers_list:
            for item in data['record']:
                if 'number' in item and str(item['number']) == str(number):
                    result.append(item)
                    break
        return result


class DataParser:
    """Parse the output of nmap and return a dictionary of data"""
    @classmethod
    def parse_data_dict(cls, data):
        """Parse the data from the nmap scan and return a dictionary of data"""
        addresses = []
        port_ids = []
        protocols = []
        service_names = []
        service_products = []
        service_versions = []
        cpes = []

        for item in data:
            addresses.append(item['address'])
            for port in item['ports']:
                port_ids.append(port['port_id'])
                protocols.append(port['protocol'])
                service_names.append(port['service_name'])
                service_products.append(port['service_product'])
                service_versions.append(port['service_version'])
                cpes.append(port['cpes'])

        return addresses, port_ids, protocols, service_names, \
            service_products, service_versions, cpes
