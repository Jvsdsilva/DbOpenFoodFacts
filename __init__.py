# !/usr/bin/python3
# -*- coding: Utf-8 -*
from Classes import Connection
from Classes import Menu

# Main program
def main():
    con = Connection.Connection()
    con.Open_connection_MySQL()
    #menu = Menu.Menu()
    #menu.genere_menu()
    
    
           

if __name__ == "__main__":
    main()
