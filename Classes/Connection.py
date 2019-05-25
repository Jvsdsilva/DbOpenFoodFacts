import pymysql.cursors
#from Classes import DbRequests
from Classes import Menu
from Classes import DbRequests
from constants import *

class Connection():

    def __init__(self):
            # Call the parent class constructor
            super().__init__()

    def Open_connection_MySQL(self):

        try:
            connection = pymysql.connect (host = HOST,
                                          user = USER,
                                          passwd = PASSWD,
                                          db = DB)

        except Exception:         
            print("Error MySQL connection")

        self.Cursor_connexion(connection)
        
        return connection 


    def Cursor_connexion(self,connection):     
        dbquery = DbRequests.DbRequests()
        menu = Menu.Menu()
        # Data base insert
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                # Create a new record
                #dbquery.Insert_category(cursor)
                #dbquery.Insert_ingredients(cursor)
                
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
                
                try:
                    menu.menu(cursor, connection)
                    
                except Exception as e:
                    print("Error with menu: "  + str(e))
                
        finally:
            connection.close()
            cursor.close()

        return cursor
