# Constants

# Data base settings
HOST = "localhost"
USER = "root"
PASSWD = "1234"
DB = "openfoodfacts"

TSTORE = DB + ".store"
TALIMENT = DB + ".aliment"
TCATEGORY = DB + ".category"
TFOODSAVE = DB + ".foodsave"
        
FIELDS_STORE = " (StoreName, Url) "
FIELDS_ALIMENT = " (NameAlim, DescriptionAlim, IdCategory, IdStore) "
FIELDS_CATEGORY = " (NameCategory) "
FIELDS_FOODSAVE = " (NameFood)"

FIELDS_INSERT_STORE = " %(StoreName)s, %(Url)s "
FIELDS_INSERT_ALIMENT = " %(NameAlim)s, %(DescriptionAlim)s, %(IdCategory)s,%(IdStore)s"
FIELDS_INSERT_CATEGORY = " %(NameCategory)s"
FIELDS_INSERT_FOODSAVE = " %(IdAliment)s, %(NameFood)s"

ID_ALIMENT = " IdAliment "
ID_STORE = " IdStore "
ID_CATEGORY = " IdCategory "

#Menu
TITLE = "Pur Beurre"
SUBTITLE = "Données OpenFoodFacts"