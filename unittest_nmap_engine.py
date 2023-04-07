import unittest
import subprocess
from unittest.mock import patch
from unittest import mock
from nmap_command_engine import NMapRunner


class TestNMapRunner(unittest.TestCase):
    def setUp(self):
        self.nmap_runner = NMapRunner()

    # Test the scan_single_ip_ports method in the NMapRunner class
    @patch('subprocess.run')
    def test_scan_single_ip_ports(self, mock_subprocess_run):
        # Set up the mock completed process with sample XML content
        sample_xml_content = b"""<?xml version="1.0" encoding="UTF-8"?>
        <nmaprun args="nmap -Pn -sT -p 1-1024 192.168.1.1">
        </nmaprun>
        """
        mock_completed_process = subprocess.CompletedProcess(
            args=None, returncode=0, stdout=sample_xml_content, stderr=b""
        )
        mock_subprocess_run.return_value = mock_completed_process

        # Call the scan_single_ip_ports method with sample input
        hosts_ip = "192.168.1.1"
        scan_group = {"-Pn": None, "-sT": None, "-p": "1-1024"}
        args, data, stderr = self.nmap_runner.scan_single_ip_ports(
            hosts_ip=hosts_ip, sudo=False, scan_group=scan_group
        )

        # Verify the output and behavior
        self.assertEqual(args, ["nmap", "-Pn", "-sT", "-p", "1-1024", "192.168.1.1"])
        self.assertEqual(data, [])
        self.assertEqual(stderr, b"")

        # Verify that subprocess.run was called with the expected command
        expected_command = [self.nmap_runner.nmap, "-Pn", "-sT", "-p", "1-1024", hosts_ip]
        mock_subprocess_run.assert_called_once_with(
            expected_command, capture_output=True, shell=False, check=True
        )


        # Assert that the parsed 'args' attribute from the XML output matches the expected value
        self.assertEqual(args, ['nmap', '-Pn', '-sT', '-p', '1-1024', '192.168.1.1'])

        # Assert that the parsed data from the XML output matches the expected value
        # The resturn is a list of dictionaries, but since we are not testing the XML parsing here, 
        # we can just assert that the list is empty
        self.assertEqual(data, [])

        # Assert that the subprocess.run function was called with the expected command, 
        # including the optional 'sudo' command.
        expected_command = [self.nmap_runner.nmap, '-Pn', '-sT', '-p', '1-1024', '192.168.1.1']
        if sudo and self.nmap_runner.sudo:
            expected_command.insert(0, self.nmap_runner.sudo)
        mock_subprocess_run.assert_called_once_with(expected_command, capture_output=True, shell=False, check=True)

        # Assert that there were no errors captured in the stderr output
        self.assertEqual(stderr, b'')


if __name__ == '__main__':
    unittest.main()
