# Constants

# Data base settings
HOST = "localhost"
USER = "root"
PASSWD = "1234"
DB = "openfoodfacts"

TSTORE = "STORE"
TALIMENT = "ALIMENT"
TCATEGORY = "CATEGORY"
TFOODSAVE = "FOODSAVE"
        
FIELDS_STORE = " (StoreName, Url) "
FIELDS_ALIMENT = " (NameAlim, NameStore, DescriptionAlim, IdCategory) "
FIELDS_CATEGORY = " (NameCategory) "
FIELDS_FOODSAVE = " (NameFood)"

FIELDS_INSERT_STORE = " StoreName, Url "
FIELDS_INSERT_ALIMENT = " NameAlim, NameStore, DescriptionAlim, IdCategory"
FIELDS_INSERT_CATEGORY = " NameCategory"
FIELDS_INSERT_FOODSAVE = " IdAliment, NameFood"

ID_ALIMENT = " IdAliment "
ID_STORE = " IdStore "
ID_CATEGORY = " IdCategory "

#Menu
TITLE = "Pur Beurre"
SUBTITLE = "Données OpenFoodFacts"