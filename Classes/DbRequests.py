#import MySQLdb
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
            Name_Store = each['stores'].split(",")
            Name_ingredients = each['product_name'] # collect item name
            Url = each['url'] # collect item name
            description_ingred = each['ingredients_text_debug']
            if "nutrition_grade_fr" in each:
                nutrition_grades = each['nutrition_grade_fr']
            else:
                nutrition_grades = " " 
            
            first_category = Name_category[0]
            first_store = Name_Store[0]
            ingredient["NameCategory"] = first_category # Add to dictionary
            ingredient["NameAlim"] = Name_ingredients # Add to dictionary
            ingredient["NameStore"] = first_store # Add to dictionary
            ingredient["DescriptionAlim"] = description_ingred # Add to dictionary
            ingredient["NutritionGrade"] = nutrition_grades
            ingredient["Url"] = Url
            
            IdNameCategory = self.Get_id_table(cursor, ID_CATEGORY, "NameCategory", TCATEGORY)
            
            for each in IdNameCategory:
                if each["NameCategory"] in ingredient["NameCategory"]:
                    idcategory = each["IdCategory"]
                    ingredient["IdCategory"] = idcategory
                    #print(idcategory)

            ingredients.append(ingredient) # Add items dictionary to list
        #print(ingredients)

        return(ingredients)

    # Insert into table aliment
    def Insert_ingredients(self,cursor):
        data = self.Request_ingredients(cursor)

        self.Insert_Db(cursor,TALIMENT,FIELDS_ALIMENT,FIELDS_INSERT_ALIMENT, data)

    def Aliment_query(self, cursor, NameAlim, IdCategory):
        myaliment = []
        query = "SELECT NameAlim, DescriptionAlim, NameStore, Url FROM " + TALIMENT + " WHERE IdCategory = '" + IdCategory + "' and NutritionGrade = 'a' "

        try:
            cursor.execute(query)

            myresult = cursor.fetchone()  # fetch the first row only
            

            for each in myresult:
                myaliment.append(each)
            

        except Exception:
            print("Error with query: " + query)

        #print(myresult)
        return myresult

    def Foodsave_query(self, cursor, NameFood):
        
        IdAliment = self.Get_id_table(cursor, ID_ALIMENT, "IdAliment", TFOODSAVE)
        print(IdAliment)
        #?????????????#
        query = " SELECT f. " + NameFood + ", a.NameAlim, a.DescriptionAlim, a.NameStore, a.Url FROM " + TFOODSAVE + " INNER JOIN " + TALIMENT + " a on f.IdAliment = a.IdAliment WHERE a.IdAliment = '" + IdAliment + "'"

        try:
            cursor.execute(query)

            myfoodsave = cursor.fetchone()  # fetch the first row only

        except Exception:
            print("Error with query: " + query)

        #print(myfoodsave)
        return myfoodsave