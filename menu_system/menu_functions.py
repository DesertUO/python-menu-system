import os
import sys
from typing import Union, List

def makeLine(text: str):
    print("="*len(text))

def clear_console():
    os.system('cls||clear')

# Some first docstrings :)
class MenuMessages:
    """This class manages the user interaction and program flow."""

    def __init__(self):
        self.welcome = "Welcome to the program..."
        """Welcome message for the user."""
        self.choopt = "Please choose an option"
        """Prompt for choosing an option."""
        self.choopt_invalid = "Option is invalid"
        """Message displayed when an invalid option is selected."""
        self.confirmation = "Ok..."
        """Confirmation message."""
        self.do_next = "Done. What do you want to do next?"
        """Prompt for the next action."""
        self.thanks_for_using = "Thanks for using this program"
        """Thank you message for using the program."""
        self.closing_program = "Closing the program..."
        """Message shown when closing the program."""
        self.return_menu = "Return to the menu"
        """Prompt for returning to the main menu."""
        self.repeat_action = "Repeat the action"
        """Prompt to repeat the last action."""
        self.quit_program = "Exit"
        """Option to exit the program."""
        self.confirm_quit = "Do you really want to exit?"
        """Confirmation message for quitting the program."""

defaultMsgs = MenuMessages()

def validateInput(msg: str, type: str = "str", inputRange: Union[str, List, range] = None):
    if type == "str":
        if inputRange is None:
            inputRange = set()
        
        while True:
            try:
                toValidate = input(msg + ": ")
                
                if not toValidate.isascii():
                    raise ValueError("Input must be ASCII.")
                if inputRange and toValidate not in inputRange:
                    raise ValueError(f"Input out of range ({inputRange})")
                return toValidate
            
            except ValueError as e:
                print(f"Input is invalid: {e}. Try again...")
                
    elif type == "int":
        if inputRange is None:
            inputRange = range(-float('inf'), float('inf'))
            
        while True:
            try:
                toValidate = int(input(msg + ": "))
                
                if toValidate in inputRange:
                    return toValidate
                else:
                    raise ValueError(f"Input out of range ({inputRange})")
                
            except ValueError as e:
                print(f"Input is invalid {e}. Try again...")
                
    elif type == "float":
        if inputRange is None:
            inputRange = (-float('inf'), float('inf'))
            
        while True:
            try:
                toValidate = float(input(msg + ": "))
                
                if not (inputRange[0] <= toValidate <= inputRange[1]):
                    raise ValueError(f"Input out of range ({inputRange})")
                return toValidate
            
            except ValueError as e:
                print(f"Input is invalid {e}. Try again...")
                
    else:
        raise TypeError("Type must be 'str', 'int' or 'float'.")

class Menu:
    def __init__(self, functions: list, msgs: MenuMessages = defaultMsgs):
        self.functions = functions
        self.msgs = msgs

    def quit(self, msg: bool = True):
        if msg == False:
            sys.exit()
        elif msg == True:
            clear_console()
            print(self.msgs.thanks_for_using)
            print(self.msgs.closing_program)
            sys.exit()
            
    def askExit(self, current_menu):
        choose_exit = validateInput("{} (y/n): ". format(self.msgs.confirm_quit), "str", ["y", "Y", "n", "N"])
            
        if ((choose_exit == "y") or (choose_exit == "Y")):
            print(self.msgs.confirmation)
            self.quit(True)
        elif ((choose_exit == "n") or (choose_exit == "N")):
            print(self.msgs.confirmation)
            clear_console()

            if current_menu == "root":
                self.menu()
            elif current_menu == "do_next_func":
                self.do_next_func()

    def menu(self):
        def namedExit():
            return self.askExit("root")
        namedExit.__name__ = "Exit"

        if not any(func.__name__ == namedExit.__name__ for func in self.functions):
            self.functions.append(namedExit)
        
        makeLine(self.msgs.welcome)
        print(self.msgs.welcome)
        makeLine(self.msgs.welcome)
        
        titles = []
        for function in self.functions:
            titles.append(function.__name__)

        for title in titles:
            print(str(titles.index(title) + 1) + ". " + str(title))

        choopt_msg =  "{}: ".format(self.msgs.choopt)

        makeLine(choopt_msg)
        self.choose = validateInput(choopt_msg, "int", range(1, len(self.functions) + 1))
        
        makeLine(self.msgs.confirmation)
        print(self.msgs.confirmation)
        
        clear_console()
        self.functions[self.choose - 1]()

        self.do_next_func()

    def do_next_func(self):
        print("")
        makeLine(self.msgs.do_next)
        print(self.msgs.do_next)
        
        print("1. {}". format(self.msgs.return_menu))
        print("2. {}". format(self.msgs.repeat_action))
        print("3. {}". format(self.msgs.quit_program))

        choopt_msg =  "{}: ".format(self.msgs.choopt)

        makeLine(choopt_msg)
        choose_do_next = validateInput(choopt_msg, "int", range(1, 4))
            
        match choose_do_next:
            case 1:
                makeLine(self.msgs.confirmation)
                print(self.msgs.confirmation)
                
                clear_console()
                self.menu()
            case 2:
                makeLine(self.msgs.confirmation)
                print(self.msgs.confirmation)
                
                clear_console()
                self.functions[self.choose - 1]()
                self.do_next_func()
            case 3:
                self.askExit("root")
            case _:
                print("Achievement Unlocked: How did we get here?...")