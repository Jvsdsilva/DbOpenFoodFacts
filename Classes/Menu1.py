#Genere Menu
# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
#from Classes import DbRequests
from constants import *
from Classes import Connection
import os

class Menu():


    def __init__(self):
            # Call the parent class constructor
            super().__init__()

    def genere_menu(self):
        header = "\
        _________               .__    __________                   __               __\n\
        \_   ___ \  ____   ____ |  |   \______   \_______  ____    |__| ____   _____/  |_\n\
        /    \  \/ /  _ \ /  _ \|  |    |     ___/\_  __ \/  _ \   |  |/ __ \_/ ___\   __\\\n\
        \     \___(  <_> |  <_> )  |__  |    |     |  | \(  <_> )  |  \  ___/\  \___|  |\n\
        \______  /\____/ \____/|____/  |____|     |__|   \____/\__|  |\___  >\___  >__|\n\
                \/                                             \______|    \/     \/      \n"
        
        colors = {
                'blue': '\033[94m',
                'pink': '\033[95m',
                'green': '\033[92m',
                }
        
    def colorize(string, color):
        if not color in colors: return string
        return colors[color] + string + '\033[0m'
    
    def foo():
        print "You called foo()"
        raw_input("Press [Enter] to continue...")
    
    def bar():
        print "You called bar()"
        raw_input("Press [Enter] to continue...")
    
    menuItems = [
        { "Call foo": foo },
        { "Call bar": bar },
        { "Exit": exit },
    ]
        
    def main():
        while True:
            os.system('clear')
            # Print some badass ascii art header here !
            print colorize(header, 'pink')
            print colorize('version 0.1\n', 'green')
            for item in menuItems:
                print colorize("[" + str(menuItems.index(item)) + "] ", 'blue') + item.keys()[0]
            choice = raw_input(">> ")
            try:
                if int(choice) < 0 : raise ValueError
                # Call the matching function
                menuItems[int(choice)].values()[0]()
            except (ValueError, IndexError):
                pass
