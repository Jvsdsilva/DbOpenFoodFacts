import pymysql.cursors
from Classes import Menu
from Classes import DbRequests
from constants import *


class Connection():

    def __init__(self):
            # Call the parent class constructor
            super().__init__()

    # Connection to mysql database
    def Open_connection_MySQL(self):

        try:
            connection = pymysql.connect(host=HOST,
                                         user=USER,
                                         passwd=PASSWD,
                                         db=DB)

        except Exception:
            print("Error MySQL connection")
        # cursor connection
        self.Cursor_connection(connection)

        return connection

    # Cursor connection
    def Cursor_connection(self, connection):
        dbquery = DbRequests.DbRequests()
        menu = Menu.Menu()

        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                # Data base insert
                Result_category = dbquery.Presence_query(cursor, TCATEGORY)
                Result_aliment = dbquery.Presence_query(cursor, TALIMENT)

                # Results presence of categories and aliments
                # in database tables
                if Result_category == 0 or Result_category is None:
                    dbquery.Insert_category(cursor)
                if Result_aliment == 0 or Result_aliment is None:
                    dbquery.Insert_ingredients(cursor)
                connection.commit()

                try:
                    # console menu
                    menu.menu(cursor, connection)

                except Exception as e:
                    print("Error with menu: " + str(e))

                # connection is not autocommit by default.
                # So you must commit to save your changes.
                connection.commit()
        finally:
            connection.close()
            cursor.close()

        return cursor
