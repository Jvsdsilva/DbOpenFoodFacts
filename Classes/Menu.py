#Genere Menu
# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
from Classes import DbRequests
from constants import *
from Classes import Connection

class Menu():


    def __init__(self):
            # Call the parent class constructor
            super().__init__()

            self._category = " "
            self._aliment = " "
       
    # function to get value of _age 
    def get_category(self): 
         print("getter method called") 
         return self._category 
       
    # function to set value of _age 
    def set_category(self, category): 
        print("setter method called") 
        self._category = category


    def genere_menu(self):
        # Create the menu
        menu = ConsoleMenu(TITLE, SUBTITLE)

        # Create some items

        # MenuItem is the base class for all items, it doesn't do anything when selected
        menu_item = MenuItem("Menu Item")

        # A FunctionItem runs a Python function when selected
        function_item = FunctionItem("Call a Python function", input, ["Enter an input"])

        # A CommandItem runs a console command
        command_item = CommandItem("Run a console command",  "touch hello.txt")

        # A SelectionMenu constructs a menu from a list of strings
        selection_menu = SelectionMenu(["Choisir une catégorie", "Retrouver mes aliments substitués"])

        # A SubmenuItem lets you add a menu (the selection_menu above, for example)
        # as a submenu of another menu
        submenu_item = SubmenuItem("Quel aliment souhaitez-vous remplacer?", selection_menu, menu)

        # Once we're done creating them, we just add the items to the menu
        menu.append_item(menu_item)
        menu.append_item(function_item)
        menu.append_item(command_item)
        menu.append_item(submenu_item)

        # Finally, we call show to show the menu and allow the user to interact
        menu.show()

