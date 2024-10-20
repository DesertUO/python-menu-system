# REALLY SIMPLE example on the usage of the menu_system module
import menu_system as mc

# Some functions
def option_one():
    print("You selected option 1.")

def option_two():
    print("You selected option 2.")

def option_three():
    print("You selected option 3.")

# List of functions to be used as options in the menu
functions = [option_one, option_two, option_three]

# Defining the menu class and starting the menu interface
def main():
    menu_1 = mc.Menu(functions)
    menu_1.menu()

# I think you can nest menus, but I haven't tried it yet. It's something I plan to implement later.

if __name__ == "__main__":
    main()