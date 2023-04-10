#!/usr/bin/env python3

""" RAAILS Main program calls in other functions from within program """

__version__ = '0.0.1'
__license__ = 'MIT'

# https://docs.python.org/3/library/shlex.html
import shlex
# https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET


class OutputParser:
    """
    Parse the output of nmap and return a dictionary of data
    """
    @staticmethod
    def parse_nmap_xml(xml_string):
        """parse_nmap_xml"""
        root = ET.fromstring(xml_string)
        args = {}
        for elem in root.iter('nmaprun'):
            for child in elem:
                if child.tag == 'args':
                    args = shlex.split(child.text)
        data = {}
        for host in root.iter('host'):
            host_data = {}
            addr = host.find('address').get('addr')
            host_data['hostnames'] = []
            for hostname in host.iter('hostname'):
                host_data['hostnames'].append(hostname.get('name'))
            host_data['ports'] = []
            for port in host.iter('port'):
                port_data = {}
                port_data['number'] = int(port.get('portid'))
                port_data['protocol'] = port.get('protocol')
                port_data['service'] = port.find('service').get('name')
                host_data['ports'].append(port_data)
            data[addr] = host_data
        return args, data

class DetailedOutputParser:
    """Parse Nmap raw XML output"""

    @staticmethod
    def parse_nmap_xml(xml: str) -> tuple:
        """
        Parse XML and return details for the scanned ports
        @param xml: Nmap XML output
        @return: tuple with Nmap arguments and list of port details
        """
        parsed_data = []
        root = ET.fromstring(xml)
        nmap_args = shlex.split(root.attrib['args'])


        for host in root.findall('host'):
            address = host.find('address').attrib['addr']
            host_data = {'address': address, 'ports': []}

            for port in host.findall('ports/port'):
                state = port.find('state').attrib['state']
                if state == 'closed':
                    continue  # Skip closed ports

                port_id = port.attrib['portid']
                protocol = port.attrib['protocol']

                services = port.findall('service')
                cpe_list = [cpe.text for service in services for cpe in service.findall('cpe')]

                service = services[0]
                service_name = service.get('name', '')
                service_product = service.get('product', '')
                service_version = service.get('version', '')

                host_data['ports'].append({
                    'port_id': port_id,
                    'protocol': protocol,
                    'service_name': service_name,
                    'service_product': service_product,
                    'service_version': service_version,
                    'cpes': cpe_list
                })

            parsed_data.append(host_data)

        return nmap_args, parsed_data
