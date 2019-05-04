import pymysql.cursors
import pyodbc
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
        connection.close()
        
        return connection 

    def Cursor_connexion(self,connection):     
        dbquery = DbRequests.DbRequests()
    
        # Data base insert
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                # Create a new record
                #dbquery.Category_query(cursor)
                
                """dbquery.Drop_foodsave(cursor)
                dbquery.Drop_arrange(cursor)
                dbquery.Drop_stow(cursor)
                dbquery.Drop_store(cursor)
                dbquery.Drop_category(cursor)
                dbquery.Drop_aliment(cursor)"""

                dbquery.Insert_stores(cursor)
                dbquery.Insert_ingredients(cursor)
                dbquery.Insert_category(cursor)
                
                dbquery.Insert_stow(cursor)
                dbquery.Insert_arrange(cursor)
                
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
        finally:
            cursor.close()
            connection.close()
        return cursor

