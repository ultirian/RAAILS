#!/usr/bin/env python3

"""Class SetHost is used to set the hostname and IP address 
of the host. It has 4 attributes: host, port, hostname, hostip. 
It has 3 methods: ip_to_hostname, hostname_to_ip, switch_case. 
It has 2 static methods: validate_ip, is_valid_hostname.
Also uses the tldextract module to extract the domain name from 
a URL and ipaddress module to validate IP addresses."""

__author__ = 'Chris Weaver'
__version__ = '0.1.0'
__license__ = 'MIT'
# https://docs.python.org/3/library/ipaddress.html
import ipaddress

# https://docs.python.org/3/library/socket.html
import socket

# https://github.com/john-kurkowski/tldextract
import tldextract

class SetHost:
    """
    Set the hostname and IP address of the host.
    https://docs.python.org/3/library/functions.html#staticmethod

    In Python, a @staticmethod is a decorator that defines a method that is bound to the class, 
    but not the instance of the class. This means that @staticmethod methods can be called on 
    the class itself, rather than on an instance of the class.
    The main difference between a @staticmethod and a @classmethod is that a @classmethod 
    receives the class itself as the first parameter, while a @staticmethod does not. Instead,
    a @staticmethod has no access to the class or instance, and operates on the arguments passed
    to it.
    """

    # Static methods don't have access to the instance or class attributes,
    # so they are usually used for utility functions that don't need to modify
    # #or access the state of the class or instance.
    # Static methods are also used to create factory functions that return
    # objects of different types depending on the input data."""
    @staticmethod
    def ip_to_hostname(ip_address):
        """Converts an IP address to a hostname."""
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            hostname = None
        return hostname

    @staticmethod
    def hostname_to_ip(hostname):
        """Converts a hostname to its corresponding IP address."""
        try:
            ip_address = socket.gethostbyname(hostname)
        except socket.gaierror:
            ip_address = None
        return ip_address

    def switch_case(self, choice):
        """switch case for set host menu"""
        options = {
            "1": self.input_host_ip,
            "2": self.input_host_name
        }

        # Call the function based on the user's input
        func = options.get(choice, lambda: print("Invalid choice"))
        return func()

    def validate_ip(self, ipinput):
        """validate IP address with ipaddress module"""
        try:
            ipaddress.ip_address(ipinput)
            return True
        except ValueError:
            return False

    def is_valid_hostname(self, hostname):
        """Returns True if `hostname` is a valid hostname."""
        extractor = tldextract.TLDExtract()
        tld, domain, _ = extractor(hostname)
        if not tld or not domain:
            return False
        if '.' in tld:
            return False
        if '-' in domain.split('.')[0] or '-' in domain.split('.')[-1]:
            return False
        return True

    def set_port(self, port):
        """Set the port number func is not used but built in for future use"""
        try:
            if port > 65535:
                return 'Invalid port number'
            else:
                return port
        except ValueError:
            return 'Invalid port number'

    def input_host_ip(self):
        """inpit IP address and validate it"""
        while True:
            try:
                # User inputs IP address
                initial_ip = input("Enter the IP address of the host: ")
                # validate inputted IP address
                if self.validate_ip(initial_ip):
                    print("Valid IP address")
                    # set the IP address of Class
                    hostip = initial_ip
                    # set the hostname of Class
                    hostname = self.ip_to_hostname(initial_ip)
                    # print the hostname and IP address
                    print(f"Hostname: {hostip} IP: {hostname}")
                    return hostip, hostname
                else:
                    print("Invalid IP address")
            except ValueError:
                print("Invalid IP address")

    def input_host_name(self):
        """Input hostname and validate it"""
        while True:
            try:
                # User inputs hostname
                initial_hostname = input("Enter the hostname of the host: ")
                # validate inputted hostname
                if self.is_valid_hostname(initial_hostname):
                    print("Valid hostname")
                    # set the hostname of Class
                    hostname = initial_hostname
                    # set the IP address of Class
                    hostip = self.hostname_to_ip(initial_hostname)
                    print(f"Hostname: {hostip} IP: {hostname}")
                    return hostip, hostname
                else:
                    print("Invalid hostname")
            except ValueError:
                print("Invalid hostname")
