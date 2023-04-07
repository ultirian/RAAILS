import unittest
from unittest.mock import patch, MagicMock
from learning_system import LearningSystem, SystemScanner

class TestLearningSystem(unittest.TestCase):

    # This method sets up the test environment for each test case
    def setUp(self):
        self.main_menu_callback = MagicMock()
        self.learning_system = LearningSystem(self.main_menu_callback)
        self.system_scanner = SystemScanner(self.learning_system)

    # Test the scan_test_server function
    @patch("learning_system.Console")
    def test_scan_test_server(self, mock_console):

        # Call the scan_test_server function
        self.system_scanner.scan_test_server()

        # Assert that the Console's print method was called with the expected strings
        mock_console.return_value.print.assert_any_call("[bold green]************************************************************[/]")
        mock_console.return_value.print.assert_any_call("[bold green]This scan will look for a preset test server on the internet[/]")
        # Add more assertions for other print calls as needed

    # Test the scan_nmap_server function
    @patch("learning_system.Console")
    def test_scan_nmap_server(self, mock_console):

        # Call the scan_nmap_server function
        self.system_scanner.scan_nmap_server()

        # Assert that the Console's print method was called with the expected strings
        mock_console.return_value.print.assert_any_call("[bold green]************************************************************[/]")
        mock_console.return_value.print.assert_any_call("[bold green]This scan will scan nmaps scanme.nmap.org                   [/]")
        # Add more assertions for other print calls as needed

if __name__ == "__main__":
    unittest.main()
