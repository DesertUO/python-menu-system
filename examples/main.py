# REALLY SIMPLE example on the usage of the menu_system module
import menu_system as ms

# Some functions
def option_one():
    print("You selected option 1.")

def option_two():
    print("You selected option 2.")

def option_three():
    print("You selected option 3.")

# List of functions to be used as options in the menu
functions = [option_one, option_two, option_three]

# Creating a custom set of messages that will be shown to the user on the menu
custom_messages_1 = ms.MenuMessages()
custom_messages_1.welcome = "Bienvenido al programa! Usando 'custom_messages_1'"
# And so on...

# Using the default set of messages (default set is in English)
custom_messages_2 = ms.defaultMsgs
custom_messages_2.welcome = "Bienvenido al programa! Usando 'custom_messages_2'"

# Defining the menu class and starting the menu interface
def main():
    menu_1 = ms.Menu(functions, custom_messages_2)
    menu_1.menu()

# I think you can nest menus, but I haven't tried it yet. It's something I plan to implement later.

if __name__ == "__main__":
    main()