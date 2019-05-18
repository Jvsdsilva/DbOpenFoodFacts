#import MySQLdb
#import pyodbc
import urllib
import requests
import json
from constants import *
import openfoodfacts.facets

class DbRequests():

    def __init__(self):
            # Call the parent class constructor
            super().__init__()

# -------------------------------- #
#             REQUESTS             #
# -------------------------------- #
#--Request api openfoodfacts categories
    def Request_categories(self):    
        #url_category = 'https://fr.openfoodfacts.org/categories.json'
        #json_data = requests.get(url_category).json()
        json_data = openfoodfacts.facets.get_categories()
        categories = []
        #content = json.dumps(json_data, indent = 4, sort_keys=True)
        #print(content)
        #for each in json_data['tags']:
        for each in json_data:
            category = {} 
            #category_type = each['name'].replace('fr:', '')# collect item name 
            category_name = each['name']# collect item name                  
            category["NameCategory"] = category_name # Add to dictionary

            categories.append(category) # Add items dictionary to list

        #print (categories)
        return(categories)
#--Request api openfoodfacts ingredients
    def Request_ingredients(self,cursor):
        categories = []
        IdNameCategory = self.Get_id_table(cursor, ID_CATEGORY, "NameCategory", TCATEGORY)
        #print(IdNameCategory)
        #products = openfoodfacts.products.get_by_store(store)
        for value in IdNameCategory:
            categories.append(value['NameCategory'])
            print(categories)
            products = openfoodfacts.products.get_by_category( "/".join(categories))
            """search_result = openfoodfacts.products.advanced_search({
            "categories":categories,
            })"""

        print(products)
        #return(ingredients)

#--Request api openfoodfacts stores
    """def Request_stores(self,cursor):
        url_stores = "https://fr.openfoodfacts.org/stores.json"
        # Get json data from openfoodfacts 
        json_data = requests.get(url_stores).json()
        #create list
        stores = []
        # Get items from json_data
        json_stores = json_data['tags']
        #content = json.dumps(json_stores, indent = 4, sort_keys=True)
        #print(content)

        #read list of tags item's
        for each in json_stores:
            #create dictionary
            store = {}
            name_store = each['name']# collect item name
            url_store = each['url'] # collect item url

            store["StoreName"] = name_store # Add to dictionary
            store["Url"] = url_store # Add to dictionary
            stores.append(store) # Add items dictionary to list
            
        #print(stores)
        return(stores)
"""
# -------------------------------- #
#              INSERTS             #
# -------------------------------- #
    # Insert methode for data insert 
    def Insert_Db(self,cursor,tablename,fields,fiels_insert, list):
        sql = "INSERT INTO " + tablename + fields +  "VALUES ("+ fiels_insert+");"

        try:
            cursor.executemany(sql, list)
            print("Insert successful "+ tablename+ "!!")
        except Exception as e:
            print(sql)
            print("Error data insert: " + str(e))

        return (sql)

    # Insert into table category
    def Insert_category(self,cursor):
        data = self.Request_categories()
        self.Insert_Db(cursor,TCATEGORY,FIELDS_CATEGORY,FIELDS_INSERT_CATEGORY, data)
    
    # Insert into table aliment    
    def Insert_ingredients(self,cursor):
        data = self.Request_ingredients(cursor)
        self.Insert_Db(cursor,TALIMENT,FIELDS_ALIMENT,FIELDS_INSERT_ALIMENT, data)

    # Insert into table store
    def Insert_stores(self,cursor):
        data = self.Request_stores(cursor)
        self.Insert_Db(cursor,TSTORE,FIELDS_STORE,FIELDS_INSERT_STORE,data)  

    # Insert into table foodsave
    def Insert_foodsave(self, cursor):
        IdAliment = self.Get_id_table(cursor, ID_ALIMENT, TALIMENT)

        #print(data)

        #self.Insert_Db(cursor,TFOODSAVE,FIELDS_FOODSAVE,FIELDS_INSERT_FOODSAVE, data_id)

# -------------------------------- #
#              DELETES             #
# -------------------------------- #
    
    # Drop methode for delete data table
    def drop_tables(self,cursor,tablename):
        sql = " DROP TABLE " + tablename + ";"
        
        try:
            cursor.execute(sql)
            print("Delete successful "+ tablename + "!!")
        except Exception as e:
            print(sql)
            print("Error delete: " + str(e))

        return (sql)

    def Drop_store(self,cursor):
        self.drop_tables(cursor,TSTORE)

    def Drop_category(self,cursor):
        self.drop_tables(cursor,TCATEGORY)

    def Drop_aliment(self,cursor):
        self.drop_tables(cursor,TALIMENT)

    def Drop_foodsave(self,cursor):
        self.drop_tables(cursor,TFOODSAVE)

# -------------------------------- #
#              QUERYS              #
# -------------------------------- #

    # Get methode to get id from tables
    def Get_id_table(self, cursor, id, name, tablename):
        table_result = []
        query = "SELECT " + id.strip() + ", " + name.strip()+ " FROM " + tablename
        
        try:
            cursor.execute(query)

            myresult = cursor.fetchall()
            #myresult = cursor.fetchmany(20)
            #print(myresult)

            """for each in myresult:
                #table_result.append(each[id.strip()])
                table_result.append(each)"""

        except Exception:
            print("Error with query: " + tablename + query)

        #print(each[id.strip()])
        #print(table_result)
        return myresult

    def Category_query(self, cursor):
        mycategory = []
        query = "SELECT NameCategory FROM " + TCATEGORY

        try:
            cursor.execute(query)
            
            myresult = cursor.fetchmany(20)
            #print(myresult)

            for each in myresult:
                mycategory.append(each)
            #print(mycategory)

        except Exception:
            print("Error with query: " + query)

        #print(mycategory)
        return mycategory

    def Aliment_query(self, cursor, NomAlim):
        mycategory = []
        query = "SELECT NomAlim, NutritionGrade FROM " + TALIMENT + "WHERE NomAlim = '" + NomAlim + "'"

        try:
            cursor.execute(query)

            myresult = cursor.fetchall()
            #print(myresult)

            for each in myresult:
                mycategory.append(each)
            #print(mycategory)

        except Exception:
            print("Error with query: " + query)

        #print(mycategory)
        return mycategory