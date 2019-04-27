import pymysql.cursors
import pyodbc
from Classes import DbRequests

from constants import *

class Connection():


    def __init__(self):
            # Call the parent class constructor
            super().__init__()

    def Open_connection_MySQL(self):       
        dbquery = DbRequests.DbRequests()
        
        try:
            connection = pymysql.connect (host = HOST,
                                          user = USER,
                                          passwd = PASSWD,
                                          db = DB)
          
        except Exception:         
            print("Error MySQL connection")

        cursor = connection.cursor()
        
        # Data base insert
        try:
            with connection.cursor() as cursor:
            # Create a new record
               dbquery.Insert_stores(cursor)
               dbquery.Insert_category(cursor)
               dbquery.Insert_ingredients(cursor)
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            cursor.close()
            connection.close()
        
        
        #row = cursor.fetchone()
        #connection.commit()
        #cursor.close()
        #connection.close()
        
        return connection 

