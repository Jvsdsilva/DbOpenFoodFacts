# Constants

# Data base settings
HOST = "localhost"
USER = "root"
PASSWD = "1234"
DB = "openfoodfacts"

TALIMENT = DB + ".aliment"
TCATEGORY = DB + ".category"
TFOODSAVE = DB + ".foodsave"
        
FIELDS_ALIMENT = " (NameAlim, NameStore, Url, DescriptionAlim, NutritionGrade, IdCategory) "
FIELDS_CATEGORY = " (NameCategory) "
FIELDS_FOODSAVE = " (NameFood, IdAliment) "

FIELDS_INSERT_ALIMENT = " %(NameAlim)s, %(NameStore)s, %(Url)s, %(DescriptionAlim)s, %(NutritionGrade)s, %(IdCategory)s"
FIELDS_INSERT_CATEGORY = " %(NameCategory)s"
FIELDS_INSERT_FOODSAVE = " %(NameFood)s, %(IdAliment)s "

ID_CATEGORY = " IdCategory "
ID_ALIMENT = " IdAliment "

#Menu
TITLE = "Pur Beurre"
SUBTITLE = "Données OpenFoodFacts"