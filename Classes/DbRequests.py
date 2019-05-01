#import MySQLdb
import pyodbc
import urllib
import requests
import json
from constants import *


class DbRequests():


    def __init__(self):
            # Call the parent class constructor
            super().__init__()
            

#--Request api openfoodfacts stores
    def Request_stores(self):
        url_stores = "https://fr.openfoodfacts.org/stores.json"
        json_data = requests.get(url_stores).json()
        stores = {}

        #content = json.dumps(json_data, indent = 4, sort_keys=True)
        #print(content)
        json_stores = json_data['tags']
        
        for each in json_stores:
            #print("ID: {0} \t NAME: {1}".format(each['id'], each['name']))
            name_store = each['name']# collect item name
            url_store = each['url'] # collect item url
            stores["StoreName"] = name_store
            stores["URL"] = url_store
            #stores.update({"StoreName":name_store, "URL":url_store}) # Add to dictionary
            #print(name_store)
            #print(url_store)       
            print(stores)
        
        return(stores)


#--Request api openfoodfacts categories
    def Request_categories(self):    
        url_category = 'https://fr.openfoodfacts.org/categories.json'
        json_data = requests.get(url_category).json()
        category = []

        for each in json_data['tags']: 
            #print(each['name'])
            name_category = each['name'] # collect item name
            category.append(name_category) # Add to dictionary
        
        return(category)

#--Request api openfoodfacts ingredients
    def Request_ingredients(self):  
        url_ingredients = "https://fr.openfoodfacts.org/ingredients.json"
        json_data = requests.get(url_ingredients).json()
        ingredients = {}
        print(json_data)
        
        for each in json_data['tags']:
            #print(each['name'])
            name_ingredients = each['name'] # collect item name
            nutrition_grade = each['nutrition_grades'] # collect item 
            ingredients.update({name_ingredients:nutrition_grade}) # Add to dictionary
        
        return(ingredients)

    def Insert_Db(self,cursor,tablename,fields,list):
        sql = "INSERT INTO " + tablename + fields +  "VALUES (" + str(list.keys()) + "," + str(list.values()) +");"

        try:
            cursor.executemany(sql)
        except Exception:
            print("Error data insert: ")

        return (sql)

    def Insert_stores(self,cursor):
        data = self.Request_stores()
        
        sql = """INSERT INTO openfoodfacts.store (StoreName, Url) VALUES (%(StoreName)s,%(Url)s)""", data
        
        try:
            cursor.executemany(sql,data)
        except Exception as e:
            print("Error data insert: " + str(e))

        return (sql)

        #self.Insert_Db(cursor,TSTORE,FIELDS_STORE,data)


    def Insert_category(self,cursor):
        data = self.Request_categories()
        
        #self.Insert_Db(cursor,TCATEGORY,FIELDS_CATEGORY,data)
        
    def Insert_ingredients(self,cursor):
        data = self.Request_ingredients()
        
        #self.Insert_Db(cursor,TALIMENT,FIELDS_ALIMENT,data)

    def Query_DB(self, cursor):
        
        query = "SELECT * FROM " + TALIMENT
        try:
            cursor.execute(query)
        except Exception:
            print("Error with query: " + query)
        
        return query