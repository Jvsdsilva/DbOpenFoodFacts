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
        #connection.close()
        
        return connection 

    def Cursor_connexion(self,connection):     
        dbquery = DbRequests.DbRequests()
    
        # Data base insert
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                # Create a new record
                """dbquery.Drop_store(cursor)
                dbquery.Drop_foodsave(cursor)
                dbquery.Drop_aliment(cursor)
                dbquery.Drop_category(cursor)"""
                #dbquery.Insert_category(cursor)
                #dbquery.Insert_stores(cursor)
                dbquery.Insert_ingredients(cursor)
                
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
                
                try:
                    dbquery.Category_query(cursor)
                except Exception as e:
                    print("Error with query: "  + str(e))
        finally:
            connection.close()
            cursor.close()
            
        return cursor

