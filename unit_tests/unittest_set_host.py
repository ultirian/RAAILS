"""unit test for set_host.py"""

import unittest
import tldextract
from set_host import SetHost


class TestSetHost(unittest.TestCase):
    def setUp(self):
        self.sethost = SetHost()

    def test_ip_to_hostname(self):
        # Test converting an IP address to a hostname
        ip_address = '8.8.8.8'  # Google DNS server
        hostname = self.sethost.ip_to_hostname(ip_address)
        self.assertIn('google', hostname.lower())

    def test_hostname_to_ip(self):
        
        # Test converting a hostname to its corresponding IP address
        hostname = 'google.com'
        ip_address = self.sethost.hostname_to_ip(hostname)
        self.assertIsNotNone(ip_address)

    def test_validate_ip(self):
        # Test validating a valid IP address
        valid_ip = '192.168.1.1'
        self.assertTrue(self.sethost.validate_ip(valid_ip))

        # Test validating an invalid IP address
        invalid_ip = '256.256.256.256'
        self.assertFalse(self.sethost.validate_ip(invalid_ip))

    def is_valid_hostname(self, hostname):
        """Returns True if `hostname` is a valid hostname."""
        extractor = tldextract.TLDExtract()
        tld, domain, _ = extractor(hostname)
        print(f"Hostname: {hostname}, TLD: {tld}, Domain: {domain}")  # Debugging line
        if not tld or not domain:
            return False
        if '.' in tld:
            return False
        if '-' in domain.split('.')[0] or '-' in domain.split('.')[-1]:
            return False
        return True

    def test_set_port(self):
        # Test setting a valid port number
        valid_port = 80
        self.assertEqual(self.sethost.set_port(valid_port), valid_port)

        # Test setting an invalid port number
        invalid_port = 70000
        self.assertEqual(self.sethost.set_port(invalid_port), 'Invalid port number')


if __name__ == '__main__':
    unittest.main()
