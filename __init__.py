# !/usr/bin/python3
# -*- coding: Utf-8 -*
from Classes import Connection
from Classes import Menu

# Main program
def main():
    #menu = Menu.Menu()
    #menu.genere_menu()
    con = Connection.Connection()
    con.Open_connection_MySQL()
    
           

if __name__ == "__main__":
    main()
