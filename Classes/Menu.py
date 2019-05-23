#Genere Menu
# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
#from Classes import DbRequests
from constants import *
from Classes import Connection
import sys, os

class Menu():


    def __init__(self):
            # Call the parent class constructor
            super().__init__()

    def genere_menu(self,list_category):
        """connexion = Connection.Connection()
        conexion_bdd = connexion.Open_connection_MySQL()
        cursor = connexion.Cursor_connexion(conexion_bdd)
        request = DbRequests.DbRequests()
        mycategory = request.Category_query(cursor)"""
        
        # Create the menu
        menu = ConsoleMenu(TITLE, SUBTITLE)
        menu2 = ConsoleMenu("Choisir categorie")
        # Create some items

        # MenuItem is the base class for all items, it doesn't do anything when selected
        menu_item = MenuItem("Menu Item")

        # A FunctionItem runs a Python function when selected
        function_item = FunctionItem("Call a Python function", input, ["Enter an input"])

        # A CommandItem runs a console command
        command_item = CommandItem("Run a console command",  "touch hello.txt")

        # A SelectionMenu constructs a menu from a list of strings
        selection_menu = SelectionMenu(list_category)
        print(list_category)
        # A SubmenuItem lets you add a menu (the selection_menu above, for example)
        # as a submenu of another menu
        selection_menu2 = SelectionMenu([list_category],None)
        submenu_item2 = SubmenuItem("Choisir une catégorie", selection_menu2, menu)
        submenu_item = SubmenuItem("Quel aliment souhaitez-vous remplacer?", selection_menu, menu)
        
        
        selection_menu3 = SelectionMenu([list_category])
        submenu_item3 = SubmenuItem("Retrouver mes aliments substitués", selection_menu3, menu)
       
        
        # Once we're done creating them, we just add the items to the menu
        menu.append_item(menu_item)
        menu.append_item(function_item)
        menu.append_item(command_item)
        menu.append_item(submenu_item)
        menu.append_item(submenu_item3)
        # Finally, we call show to show the menu and allow the user to interact
        menu.show()

    def genere_menu2(self):
        """connexion = Connection.Connection()
        conexion_bdd = connexion.Open_connection_MySQL()
        cursor = connexion.Cursor_connexion(conexion_bdd)
        request = DbRequests.DbRequests()
        mycategory = request.Category_query(cursor)"""
        list_category = ["category1", "category2", "category3"]
        list_aliments = ["Alim1", "Alim2", "Alim3"]
        # Create the menu
        menu = ConsoleMenu(TITLE, SUBTITLE)
        # Create some items

        # MenuItem is the base class for all items, it doesn't do anything when selected
        menu_item = MenuItem("Menu Item")

        # A FunctionItem runs a Python function when selected
        function_item = FunctionItem("Choisir une catégorie", input, ["Enter an input"])

        # A CommandItem runs a console command
        command_item = CommandItem("Run a console command",  "touch hello.txt")

        # A SelectionMenu constructs a menu from a list of strings
        selection_menu = SelectionMenu(list_category)
        print(list_category)
        # A SubmenuItem lets you add a menu (the selection_menu above, for example)
        # as a submenu of another menu

        submenu_item = SubmenuItem("Quel aliment souhaitez-vous remplacer?", selection_menu, menu)
        
        selection_menu2 = SelectionMenu(list_aliments)
        #selection = SelectionMenu.get_selection(list_category)
        submenu_item2 = SubmenuItem("Choisir une catégorie", selection_menu, menu)
        submenu_item4 = SubmenuItem("Choisir un aliment", selection_menu2, menu)
        """choice_category = input(submenu_item2)

        if choice_category == "1":
            print("alim1")
        if choice_category == "2":
            print("alim2")
        if choice_category == "3":
            print("alim3")"""
        
        selection_menu3 = SelectionMenu([list_category])
        submenu_item3 = SubmenuItem("Retrouver mes aliments substitués", selection_menu3, menu)
        
        # Once we're done creating them, we just add the items to the menu
        #menu.append_item(menu_item)
        menu.append_item(function_item)
        #menu.append_item(selection)
        menu.append_item(submenu_item)
        menu.append_item(submenu_item3)
        # Finally, we call show to show the menu and allow the user to interact
        menu.show()

    def menu(self):
        
        print("Pur Beurre Bonjour")

        print("1 Quel aliment souhaitez-vous remplacer?")
        print("2 Retrouver mes aliments substitués")
        print("3 Exit")
        print("4 Exit")
        
        choice = input()    
        
        if choice == "1":
            #list_category = ["category1", "category2", "category3"]
            list_alim1 = ["alimcat1", "alimcat1", "alimcat1"]
            list_alim2 = ["alimcat2", "alimcat2", "alimcat2"]
            list_alim3 = ["alimcat3", "alimcat3", "alimcat3"]
            print("Sélectionnez la catégorie \n ")
            print("1 category1")
            print("2 category2")
            print("3 category3")
            print("4 category4")
            #print(list_category)
            choice_category = input()
            
            if choice_category == "1":          
                print("Selectionnez l'aliment \n ")
                print("1 alimcat1")
                print("2 alimcat1")
                print("3 alimcat1")
                print("4 alimcat1")
                choice_alim1 = input()
                if choice_alim1 == "1":
                    Id_categorie = "1"
                    NomAlim = "alim1"
                    print(NomAlim)
                if choice_alim1 == "2":
                    Id_categorie = "1"
                    NomAlim = "alim1"
                    print(NomAlim)
                if choice_alim1 == "3":
                    Id_categorie = "1"
                    NomAlim = "alim1"
                    print(NomAlim)
                if choice_alim1 == "4":
                    Id_categorie = "1"
                    NomAlim = "alim1"
                    print(NomAlim)
            if choice_category == "2":
                print("Selectionnez l'aliment \n ")
                print("1 alimcat1")
                print("2 alimcat1")
                print("3 alimcat1")
                print("4 alimcat1")
                choice_alim2 = input()
                if choice_alim2 == "2":
                    Id_categorie = "2"
                    NomAlim = "alim2"
                    print(NomAlim)
            if choice_category == "3":
                print("Selectionnez l'aliment \n ")
                print("1 alimcat1")
                print("2 alimcat1")
                print("3 alimcat1")
                print("4 alimcat1")
                choice_alim3 = input()
                if choice_alim3 == "3":
                    Id_categorie = "3"
                    NomAlim = "alim3"
                    print(NomAlim)
        if choice == "2":
            print("Recherche liste ")
