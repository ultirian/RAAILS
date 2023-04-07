import unittest
from unittest import mock
import json
from port_ident_tool import IANAPortList, DataParser


class TestIANAPortList(unittest.TestCase):
    def setUp(self):
        self.filename = "IANA_convertjson.json"  # A sample IANA port list for testing
        self.iana_port_list = IANAPortList()

def test_search_numbers_in_list(self):
    # Test searching for port numbers in the IANA port list
    numbers_list = [80, 443]
    with unittest.mock.patch('builtins.print') as mock_print:
        self.iana_port_list.search_numbers_in_list(self.filename, numbers_list)
        # Check if the print function has been called with the expected strings
        mock_print.assert_any_call("\nPort number 80 is a tcp protocol. Description: World Wide Web HTTP")
        mock_print.assert_any_call("\nPort number 443 is a tcp protocol. Description: http protocol over TLS/SSL")

def test_search_numbers_in_list_ret_record(self):
    # Test searching for port numbers in the IANA port list and returning records
    numbers_list = [80, 443]
    expected_result = [
        {
            "number": "80",
            "name": "http",
            "protocol": "tcp",
            "description": "World Wide Web HTTP",
            "assigned_date": "1992-12-01"
        },
        {
            "number": "443",
            "name": "https",
            "protocol": "tcp",
            "description": "http protocol over TLS/SSL",
            "assigned_date": "1995-11-01"
        }
    ]
    result = self.iana_port_list.search_numbers_in_list_ret_record(self.filename, numbers_list)
    self.assertEqual(result, expected_result)


class TestDataParser(unittest.TestCase):
    def setUp(self):
        self.data_parser = DataParser()
        self.data = [
            {
                "address": "192.168.1.1",
                "ports": [
                    {
                        "port_id": 80,
                        "protocol": "tcp",
                        "service_name": "http",
                        "service_product": "nginx",
                        "service_version": "1.14.0",
                        "cpes": ["cpe:/a:nginx:nginx:1.14.0"]
                    },
                    {
                        "port_id": 443,
                        "protocol": "tcp",
                        "service_name": "https",
                        "service_product": "nginx",
                        "service_version": "1.14.0",
                        "cpes": ["cpe:/a:nginx:nginx:1.14.0"]
                    }
                ]
            }
        ]

    def test_parse_data_dict(self):
        # Test parsing the data and returning the expected output
        expected_output = (
            ["192.168.1.1"],
            [80, 443],
            ["tcp", "tcp"],
            ["http", "https"],
            ["nginx", "nginx"],
            ["1.14.0", "1.14.0"],
            [["cpe:/a:nginx:nginx:1.14.0"], ["cpe:/a:nginx:nginx:1.14.0"]]
        )
        output = self.data_parser.parse_data_dict(self.data)
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
