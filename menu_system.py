import os
import sys

def makeLine(text: str):
    print("="*len(text))

def clear_console():
    os.system('cls||clear')

default_msgs_menu = {
    "welcome": "Welcome to the program...",
    "choopt": "Please choose an option",
    "choopt_invalid": "Option is invalid",
    "confirmation": "Ok...",
    "do_next": "Done. What do you want to do next?",
    "thanks_for_using": "Thanks for using this program",
    "closing_program": "Closing the program...",
    "return_menu": "Return to the menu",
    "repeat_action": "Repeat the action",
    "quit_program": "Exit"
}

class Menu:
    def __init__(self, functions: list, msgs: dict = default_msgs_menu):
        self.functions = functions
        self.msgs = msgs

    def salir(self, msg=True):
        if msg == False:
            sys.exit()
        else:
            clear_console()
            print(self.msgs["thanks_for_using"])
            print(self.msgs["closing_program"])
            sys.exit()

    def menu(self):
        if not(self.salir in self.functions):
            self.functions.append(self.salir)
        
        makeLine(self.msgs["welcome"])
        print(self.msgs["welcome"])
        makeLine(self.msgs["welcome"])
        
        titles = []
        for function in self.functions:
            titles.append(function.__name__)

        for title in titles:
            print(str(titles.index(title) + 1) + ". " + str(title))

        choopt_msg =  "{}: ".format(self.msgs["choopt"])
        choopt_invalid_msg = "{} {}: ".format(self.msgs["choopt_invalid"], self.msgs["choopt"])

        makeLine(choopt_msg)
        self.choose = input(choopt_msg)

        while ((not(self.choose.isnumeric() == True)) or ((int(self.choose) <= 0) or (int(self.choose) > len(self.functions)))):
            makeLine(choopt_invalid_msg)
            self.choose = input(choopt_invalid_msg)

        self.choose = int(self.choose)
        
        makeLine(self.msgs["confirmation"])
        print(self.msgs["confirmation"])
        
        clear_console()
        self.functions[self.choose - 1]()

        self.do_next_func()

    def do_next_func(self):
        print("")
        makeLine(self.msgs["do_next"])
        print(self.msgs["do_next"])
        
        print("1. {}". format(self.msgs["return_menu"]))
        print("2. {}". format(self.msgs["repeat_action"]))
        print("3. {}". format(self.msgs["quit_program"]))

        choopt_msg =  "{}: ".format(self.msgs["choopt"])
        choopt_invalid_msg = "{} {}: ".format(self.msgs["choopt_invalid"], self.msgs["choopt"])

        makeLine(choopt_msg)
        choose_do_next = input(choopt_msg)

        while ((not(choose_do_next.isnumeric() == True)) or ((int(choose_do_next) <= 0) or (int(choose_do_next) > 3))):
            makeLine(choopt_invalid_msg)
            choose_do_next = input(choopt_invalid_msg)

        choose_do_next = int(choose_do_next)
            
        match choose_do_next:
            case 1:
                makeLine(self.msgs["confirmation"])
                print(self.msgs["confirmation"])
                
                clear_console()
                self.menu()
            case 2:
                makeLine(self.msgs["confirmation"])
                print(self.msgs["confirmation"])
                
                clear_console()
                self.functions[self.choose - 1]()
                self.do_next_func()
            case 3:
                self.salir()
            case _:
                print("Achievement: How did we get here?...")