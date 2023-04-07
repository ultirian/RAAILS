import unittest
from unittest.mock import patch, Mock
from io import StringIO
from live_system_2 import HostHolder, ScanSystem, LiveSystem

class TestHostHolder(unittest.TestCase):

    def test_set_host(self):
        HostHolder.set_host("example.com")
        self.assertEqual(HostHolder.get_host(), "example.com")

    def test_set_ip(self):
        HostHolder.set_ip("192.168.1.1")
        self.assertEqual(HostHolder.get_ip(), "192.168.1.1")

class TestScanSystem(unittest.TestCase):
    

    def setUp(self):
        self.scan_system = ScanSystem()
        

    @patch("builtins.input", side_effect=["example.com"])
    @patch("set_host.SetHost.input_host_name", return_value=("example.com", "192.168.1.1"))
    def test_set_hostname(self, mock_input_host_name, mock_input):
        self.scan_system.set_hostname()
        self.assertEqual(self.scan_system.host_holder.get_host(), "example.com")
        self.assertEqual(self.scan_system.host_holder.get_ip(), "192.168.1.1")

    @patch("builtins.input", side_effect=["192.168.1.1"])
    @patch("set_host.SetHost.input_host_ip", return_value=("192.168.1.1", "example.com"))
    def test_set_ip(self, mock_input_host_ip, mock_input):
        self.scan_system.set_ip()
        self.assertEqual(self.scan_system.host_holder.get_host(), "example.com")
        self.assertEqual(self.scan_system.host_holder.get_ip(), "192.168.1.1")

class TestLiveSystem(unittest.TestCase):

    def setUp(self):
        self.live_system = LiveSystem(Mock())

    def test_switch_case_livesystem(self):
        with patch("builtins.input", side_effect=["1", "8"]):
            with patch("live_system_2.LiveSystem.set_hostname") as mock_set_hostname:
                self.live_system.display_menu()
                mock_set_hostname.assert_called_once()

if __name__ == "__main__":
    unittest.main()
