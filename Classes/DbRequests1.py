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
        url_category = 'https://fr.openfoodfacts.org/cgi/search.pl?search_terms=products&search_simple=1&action=process&json=1'
        json_data = requests.get(url_category).json()
        categories = []
        #content = json.dumps(json_data, indent = 4, sort_keys=True)
        #print(content)

        for each in json_data['products']:
            category = {} 
            #category_type = each['name'].replace('fr:', '')# collect item name 
            category_name = each['categories']# collect item name               
            category["NameCategory"] = category_name # Add to dictionary

            categories.append(category) # Add items dictionary to list
            
        #print (categories)
        return(categories)

#--Request api openfoodfacts ingredients
    def Request_ingredients(self,cursor):  
        url_ingredients = "https://fr.openfoodfacts.org/cgi/search.pl?search_terms=products&search_simple=1&action=process&json=1"
        json_data = requests.get(url_ingredients).json()
        ingredients = []
        i = 0

        for each in json_data['products']:
            i += 1
            ingredient = {}
            Name_category = each['categories']
            Name_Store = each['stores']
            name_ingredients = each['product_name'] # collect item name
            description_ingred = each['ingredients_text_debug']
            #nutrition_grade = each['nutrition_grades'] # collect item 
            #print(Name_category)
            IdNameCategory = self.Get_id_table(cursor, ID_CATEGORY, "NameCategory", TCATEGORY)
            #print(IdNameCategory)
			
            # Presece category in data to get id
            for row in IdNameCategory:
                for elem in row:
                    print(elem)
                print()

            """if Name_category in IdNameCategory.values:
                print("request category")
                ingredient = {}
                IdNameCategory = self.Get_id_table(cursor, ID_CATEGORY, "NameCategory", TCATEGORY)
                for value in IdNameCategory:
                    ingredient["IdCategory"] = value["IdCategory"]
                    #print(IdNameCategory)"""
				
            # Presece store in data to get id
            """if Name_Store in json_data['products']:
                ingredient = {}
                IdName_Store = self.Get_id_table(cursor, ID_STORE, "Name_Store", TSTORE)
                for value in IdName_Store:
                    ingredient["IdStore"] = IdName_Store # Add to dictionary"""
		   
        ingredient["NameAlim"] = name_ingredients # Add to dictionary
        ingredient["DescriptionAlim"] = description_ingred # Add to dictionary
		#ingredient["NutritionGrade"] = nutrition_grade
        
        ingredients.append(ingredient) # Add items dictionary to list
        #print(ingredients)
        return(ingredients)

#--Request api openfoodfacts stores
    def Request_stores(self,cursor):
        url_stores = "https://fr.openfoodfacts.org/cgi/search.pl?search_terms=products&search_simple=1&action=process&json=1"
        # Get json data from openfoodfacts 
        json_data = requests.get(url_stores).json()
        #create list
        stores = []
        # Get items from json_data
        #content = json.dumps(json_stores, indent = 4, sort_keys=True)
        #print(content)
        #read list of tags item's
        for each in json_data['products']:
            #create dictionary
            store = {}
            name_store = each['stores']# collect item name
            url_store = each['url'] # collect item url

            store["StoreName"] = name_store # Add to dictionary
            store["Url"] = url_store # Add to dictionary
            stores.append(store) # Add items dictionary to list
            
        #print(stores)    
        return(stores)

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

            """ for each in myresult:
                #table_result.append(each[id.strip()])
                #table_result.append(each)
                table_result.update(each)"""

        except Exception:
            print("Error with query: " + tablename + query)
        
        #print(each[id.strip()])
        #print(table_result)
        #print("results")
        #print(myresult)
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