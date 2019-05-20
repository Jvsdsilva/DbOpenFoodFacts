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
        url_category = 'https://fr.openfoodfacts.org/categories.json'
        json_data = requests.get(url_category).json()
        categories = []

        for each in json_data['tags']:
            category = {} 
            category_name = each['name']# collect item name               
            category["NameCategory"] = category_name # Add to dictionary

            categories.append(category) # Add items dictionary to list
            
        #print (categories)
        return(categories)

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

    # -------------------------------- #
#              QUERYS              #
# -------------------------------- #

    # Get methode to get id from tables
    def Get_id_table(self, cursor, id, name, tablename):
        query = "SELECT " + id.strip() + ", " + name.strip()+" FROM " + tablename
        
        try:
            cursor.execute(query)
            myresult = cursor.fetchall()
            #myresult = cursor.fetchmany(20)
            #print(myresult)     

        except Exception:
            print("Error with query: " + tablename + query)
        #print(myresult)
        return(myresult)

#--Request api openfoodfacts ingredients
    def Request_ingredients(self,cursor):  
        url_ingredients = "https://fr.openfoodfacts.org/cgi/search.pl?search_terms=products&search_simple=1&action=process&json=1"
        json_data = requests.get(url_ingredients).json()
        ingredients = []

        for each in json_data['products']:
            ingredient = {}
            Name_category = each['categories'].split(",")
            Name_Store = each['stores']
            name_ingredients = each['product_name'] # collect item name
            description_ingred = each['ingredients_text_debug']

            first_category = Name_category[0]
            ingredient["NameCategory"] = first_category # Add to dictionary
            ingredient["NameAlim"] = name_ingredients # Add to dictionary
            ingredient["NameStore"] = Name_Store # Add to dictionary
            ingredient["DescriptionAlim"] = description_ingred # Add to dictionary
		    #ingredient["NutritionGrade"] = nutrition_grade
            IdNameCategory = self.Get_id_table(cursor, ID_CATEGORY, "NameCategory", TCATEGORY)
            
            for each in IdNameCategory:
                if each["NameCategory"] in ingredient["NameCategory"]:
                    idcategory = each["IdCategory"]
                    ingredient["IdCategory"] = idcategory
                    #print(idcategory)

            ingredients.append(ingredient) # Add items dictionary to list
        print(ingredients)

        return(ingredients)

    def One_category(self,cursor):
        url_ingredients = "https://fr.openfoodfacts.org/cgi/search.pl?search_terms=products&search_simple=1&action=process&json=1"
        json_data = requests.get(url_ingredients).json()
        name = []
        
        for each in json_data['products']['categories']:
            names = {}
            Name_category = each['categories'].split()
            names["NameCategory"] = Name_category # Add to dictionary
            category1 = Name_category[0]
            category2 = category1.replace(","," ")
        #print(names["NameCategory"])
        #print(category2)
        name.append(names) # Add items dictionary to list
        #print(name[0])

        return(category2)

    # Insert into table category
    def Insert_ingredients(self,cursor):
        data = self.Request_ingredients(cursor)
        print(data)
        """IdNameCategory = self.Get_id_table(cursor, ID_CATEGORY, "NameCategory", TCATEGORY)
        #print(IdNameCategory[0]["NameCategory"])
        #print(data[0]["NameCategory"])
        for each in IdNameCategory:
            #print(each["NameCategory"])
            if each["NameCategory"] in data[0]["NameCategory"]:
                idcategory = each["IdCategory"]
                #print(idcategory)"""

        self.Insert_Db(cursor,TALIMENT,FIELDS_ALIMENT,FIELDS_INSERT_ALIMENT, data)