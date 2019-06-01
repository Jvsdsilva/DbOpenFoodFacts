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
# --Request api openfoodfacts categories
    def Request_categories(self):
        url_category = 'https://fr.openfoodfacts.org/categories.json'
        json_data = requests.get(url_category).json()
        categories = []

        for each in json_data['tags']:
            category = {}
            category_name = each['name']  # collect item name
            print(each['name'])
            category["NameCategory"] = category_name  # Add to dictionary
            categories.append(category)  # Add items dictionary to list

        return(categories)

# --Request api openfoodfacts ingredients
    def Request_ingredients(self, cursor):
        url_ingredients = ("https://fr.openfoodfacts.org/cgi/search.pl?" +
                           "search_terms=products&search_simple=1&action" +
                           "=process&page_size=60&json=1")
        json_data = requests.get(url_ingredients).json()
        ingredients = []

        for each in json_data['products']:
            ingredient = {}
            Name_category = each['categories'].split(",")  # collect item name
            Name_Store = each['stores'].split(",")  # collect item name
            Name_ingredients = each['product_name']  # collect item name
            Url = each['url']  # collect item name
            description_ingred = each['ingredients_text_debug']

            # Presence of nutrition grade in json_data
            if "nutrition_grade_fr" in each:
                nutrition_grades = each['nutrition_grade_fr']
            else:
                nutrition_grades = " "

            # Ingredient affectation
            first_category = Name_category[0]
            first_store = Name_Store[0]
            ingredient["NameCategory"] = first_category  # Add to dictionary
            ingredient["NameAlim"] = Name_ingredients  # Add to dictionary
            ingredient["NameStore"] = first_store  # Add to dictionary
            ingredient["DescriptionAlim"] = description_ingred
            ingredient["NutritionGrade"] = nutrition_grades
            ingredient["Url"] = Url
            IdNameCategory = self.Get_id_table(cursor, ID_CATEGORY,
                                               "NameCategory", TCATEGORY)
            # Search of IdCategory in table category
            for each in IdNameCategory:
                if each["NameCategory"] in ingredient["NameCategory"]:
                    idcategory = each["IdCategory"]
                    ingredient["IdCategory"] = idcategory
                    break

            ingredients.append(ingredient)  # Add dictionary's items to list

        return(ingredients)

# -------------------------------- #
#              INSERTS             #
# -------------------------------- #
    # Insert methode for data insert
    def Insert_Db(self, cursor, tablename, fields, fiels_insert, list):
        sql = ("INSERT INTO " + tablename + fields +
               "VALUES (" + fiels_insert + ");")

        try:
            cursor.executemany(sql, list)
            print("Insert successful " + tablename + "!!")
        except Exception as e:
            print(sql)
            print("Error data insert: " + str(e))

        return (sql)

    # Insert into table category
    def Insert_category(self, cursor):
        data = self.Request_categories()
        self.Insert_Db(cursor, TCATEGORY, FIELDS_CATEGORY,
                       FIELDS_INSERT_CATEGORY, data)

    # Insert into table aliment
    def Insert_ingredients(self, cursor):
        data = self.Request_ingredients(cursor)
        self.Insert_Db(cursor, TALIMENT, FIELDS_ALIMENT,
                       FIELDS_INSERT_ALIMENT, data)

    # Insert into table foodsave
    def Foodsave(self, cursor, data_foodsave):
        print(data_foodsave)
        self.Insert_Db(cursor, TFOODSAVE, FIELDS_FOODSAVE,
                       FIELDS_INSERT_FOODSAVE, data_foodsave)

# -------------------------------- #
#              QUERYS              #
# -------------------------------- #

    # Get methode to get id from tables
    def Get_id_table(self, cursor, id, name, tablename):
        query = ("SELECT " + id.strip() + ", " + name.strip() +
                 " FROM " + tablename)

        try:
            cursor.execute(query)
            myresult = cursor.fetchall()

        except Exception:
            print("Error with query: " + tablename + query)

        return(myresult)

    # Get methode to get id from tables
    def Get_id_by_name(self, cursor, id, nameAlim, tablename, Name):
        query = ("SELECT " + id.strip() + ", " + nameAlim.strip() +
                 " FROM " + tablename +
                 "WHERE NameAlim = " + Name)

        try:
            cursor.execute(query)
            myresult = cursor.fetchone()  # fetch the first row only

        except Exception:
            print("Error with query: " + tablename + query)

        return(myresult)

    # Search of aliments by IdCategory in table Aliment
    def Aliment_query(self, cursor, NameAlim, IdCategory, NutritionGrade):

        query = ("SELECT IdAliment, NameAlim, DescriptionAlim, NameStore," +
                 " Url FROM " + TALIMENT + " WHERE IdCategory = " +
                 IdCategory + " and NutritionGrade = '" +
                 NutritionGrade + "'")

        try:
            cursor.execute(query)
            myresult = cursor.fetchone()  # fetch the first row only

        except Exception:
            print("Error with query: " + query)

        return myresult

    # Search Aliment in table Foodsave
    def Foodsave_query(self, cursor):

        query = ("SELECT a.NameAlim, a.DescriptionAlim, a.NameStore," +
                 " a.Url FROM " + TFOODSAVE + " f INNER JOIN " +
                 TALIMENT + " a on f.IdAliment = a.IdAliment")

        try:
            cursor.execute(query)
            myfoodsave = cursor.fetchall()  # fetch all rows

        except Exception:
            print("Error with query: " + query)

        return myfoodsave

    # Search results in a table
    def Presence_query(self, cursor, NameTable):

        query = ("SELECT * FROM " + NameTable)

        try:
            cursor.execute(query)
            myresult = cursor.fetchone()  # fetch the first row only

        except Exception:
            print("Error with query: " + query)

        return myresult
