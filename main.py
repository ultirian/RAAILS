#!/usr/bin/env python3

""" RAAILS Main program calls in other functions from within program """
__author__ = 'Chris Weaver'
__version__ = '0.0.5'
__license__ = 'MIT'

import sys

from live_system_2 import LiveSystem
from learning_system import LearningSystem
# https://github.com/sepandhaghighi/art
from art import text2art
# https://rich.readthedocs.io/
from rich.console import Console

# Create an instance of the Console class from rich libary.
console = Console()


class RAAILS():
    """This class is used to print the title of the program"""

    def __init__(self) -> None:
        pass

    def title(self):
        """Print the title of the program"""
        # Print the title
        title = "RAAILS"
        print("\n")
        # Set font to ghost
        header = text2art(title, font='ghost')
        # print the title using text2art for flair
        console.print(header)
        console.print(
            "\t\t------------------------------------------------------------")
        console.print(
            "\t\t[bold yellow]\U0001F686 Really Awesome, Auditing and Interactive Learning System \U0001F686[/]")
        console.print(
            "\t\t------------------------------------------------------------")

    def disclaimer(self):
        """Print the disclaimer"""

        console.print('[bold red]Enumerating a host system involves identifying and gathering'
                      'information about the system\'s configuration, services, and applications.'
                      'This tool can be valuable for system administrators and security professionals'
                      'to identify vulnerabilities and potential security risks. However it is'
                      'important to note that this process can also have risks and possible'
                      'consequences.\n\nThe act of enumeration itself can disrupt the system being'
                      'scanned or even cause the system to crash. Additionally, during the'
                      'enumeration process, sensitive information about the system may be disclosed,'
                      'which can lead to unauthorized access or other security breaches. It is'
                      'essential to obtain proper authorization and consent before attempting to'
                      'enumerate a system. Unauthorized or malicious enumeration can lead to legal'
                      'and ethical consequences. \n\nIt is also crucial to use reliable and reputable'
                      'tools and to follow established best practices for system enumeration to'
                      'minimize the risks involved. By choosing to enumerate a host system, you'
                      'accept responsibility for any potential risks and consequences that may arise.'
                      'Therefore, we strongly recommend you consult with a qualified IT professional'
                      'and obtain proper authorization and consent before attempting any system enumeration.[/]')

    def introduction_text(self):
        """Print the introduction text"""


class ToplevelSwitch:
    """This class is used to switch between the different functions and allows for
    live_system to return the hostip_top variable to the main program."""

    def __init__(self):
        pass

    def learning_test_system(self):
        """Run the learning test system"""
        print("RAAILS Learning Test System")
        print("This is a learning test system to help you learn how to use RAAILS")
        print("This will test a VM on your local machine")
        # Implement callback to main menu
        learning_system = LearningSystem(main_menu_callback=my_switch)
        learning_system.display_menu()

    def live_system(self):
        """Run the live system"""
        print("RAAILS Live System")
        live_system = LiveSystem(main_menu_callback=my_switch)
        # Call the switch_case method based on the user's input
        live_system.display_menu()

    # end program escape function
    def end_program(self):
        """End the program with exit()"""
        console.print("[blue]Thank you for using RAAILS. Goodbye.[/]")
        sys.exit()

    def default_action(self):
        """Default action if user enters invalid choice"""
        print("Invalid choice\n")

    def switch_case_toplevel(self, choice_input):
        """Switch case to call the correct function"""
        options = {
            "1": self.learning_test_system,
            "2": self.live_system,
            "3": self.end_program
        }
        # Call the function based on the user's input
        func = options.get(choice_input, self.default_action)
        func()


if __name__ == "__main__":
    # Create an instance of the RAAILS class
    R = RAAILS()
    # Call the title method from RAAILS class
    R.title()
    # Create an instance of the Switch class
    R.disclaimer()
    my_switch = ToplevelSwitch()
    # loops console menu
    while True:
        console.print("\n[bold white]Main Menu[/]")
        console.print("[bold green]1: Learning Test System[/]")
        console.print("[bold red]2: Live System[/]")
        console.print("[bold blue]3: Exit[/]")
        # get user input
        
        choice = console.input("~>: ")
        # Call the switch_case method based on the user's input
        my_switch.switch_case_toplevel(choice)
