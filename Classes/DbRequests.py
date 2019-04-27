#import MySQLdb
import pyodbc
import urllib
import requests
import json
from Classes import DbInsert
from constants import *
class DbRequests():


    def __init__(self):
            # Call the parent class constructor
            super().__init__()

#--Request api openfoodfacts stores
    def Request_stores(self):
        url_stores = "https://fr.openfoodfacts.org/stores.json"
        json_data = requests.get(url_stores).json()
        json_stores = json_data['tags']
        stores = {}
        
        for each in json_stores:
            #print("ID: {0} \t NAME: {1}".format(each['id'], each['name']))
            name_store = each['name'] # collect item name
            url_store = each['url'] # collect item url
            stores.update({name_store:url_store}) # Add to dictionary
        
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