import unittest
from unittest.mock import MagicMock
from io import StringIO
from contextlib import redirect_stdout
from main import RAAILS, ToplevelSwitch


class TestRAAILS(unittest.TestCase):

    def test_title(self):
        raails = RAAILS()
        # Redirect stdout to capture printed output
        with redirect_stdout(StringIO()) as f:
            raails.title()
        output = f.getvalue().strip()
        # Check if the expected output is equal to the printed output
        expected_output = "RAAILS"
        self.assertEqual(expected_output, output.split("\n")[0])

    def test_disclaimer(self):
        raails = RAAILS()
        # Redirect stdout to capture printed output
        with redirect_stdout(StringIO()) as f:
            raails.disclaimer()
        output = f.getvalue().strip()
        # Check if the expected output is equal to the printed output
        expected_output = "Enumerating a host system involves identifying"
        self.assertEqual(expected_output, output.split("\n")[0])

    def test_switch_case_toplevel(self):
        switch = ToplevelSwitch()
        # Test learning test system option
        switch.learning_test_system = MagicMock()
        switch.switch_case_toplevel("1")
        switch.learning_test_system.assert_called_once()
        # Test live system option
        switch.live_system = MagicMock()
        switch.switch_case_toplevel("2")
        switch.live_system.assert_called_once()
        # Test exit option
        switch.end_program = MagicMock()
        switch.switch_case_toplevel("3")
        switch.end_program.assert_called_once()
        # Test default action for invalid input
        with redirect_stdout(StringIO()) as f:
            switch.switch_case_toplevel("4")
        output = f.getvalue().strip()
        expected_output = "Invalid choice"
        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
