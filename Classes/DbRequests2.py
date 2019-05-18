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
        table_result = {}
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
        
        #parcourir la data
        # a chaque tour de boucle sauvegarder la categorie
        # utiliser le nom de la categorie pour verifier si elle existe dans la table categorie
        # si elle est presente sauvegarder le id categorie
        # faire la même chose pour le store
        # inserer la ligne dans la table aliment
        
        for each in json_data['products']:
            ingredient = {}
            Name_category = each['categories'].split()
            Name_Store = each['stores']
            name_ingredients = each['product_name'] # collect item name
            description_ingred = each['ingredients_text_debug']
            #nutrition_grade = each['nutrition_grade_fr'] # collect item 
            ingredient["NameCategory"] = Name_category # Add to dictionary
            ingredient["NameAlim"] = name_ingredients # Add to dictionary
            ingredient["NameStore"] = Name_Store # Add to dictionary
            ingredient["DescriptionAlim"] = description_ingred # Add to dictionary
		    #ingredient["NutritionGrade"] = nutrition_grade
        
        ingredients.append(ingredient) # Add items dictionary to list
        print(ingredients)

        return(ingredients)

     # Insert into table category
    def Insert_ingredients(self,cursor):
        data = self.Request_ingredients(cursor)
        #print(data)
        IdNameCategory = self.Get_id_table(cursor, ID_CATEGORY, "NameCategory", TCATEGORY)
        #print(IdNameCategory[0]["NameCategory"])

        """if IdNameCategory[0]["NameCategory"] in data[0]["NameCategory"]:
            print(IdNameCategory[0]["IdCategory"])"""

        #self.Insert_Db(cursor,TCATEGORY,FIELDS_CATEGORY,FIELDS_INSERT_CATEGORY, data)
