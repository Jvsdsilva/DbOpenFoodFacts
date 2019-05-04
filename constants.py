# Constants

# Data base settings
HOST = "localhost"
USER = "root"
PASSWD = "1234"
DB = "openfoodfacts"

TSTORE = DB + ".store"
TALIMENT = DB + ".aliment"
TARRANGE = DB + ".arrange"
TCATEGORY = DB + ".category"
TFOODSAVE = DB + ".foodsave"
TSTOW = DB + ".stow"
        
FIELDS_STORE = " (StoreName,Url) "
FIELDS_ALIMENT = " (NameAlim,DescriptionAlim,NutritionGrade) "
FIELDS_ARRANGE = " (IdCategory,IdAliment) "
FIELDS_CATEGORY = " (CategoryType) "
FIELDS_FOODSAVE = " (NameFood, NameAlim, DescriptionAlim, StoreName, Url, IdCategory, IdAliment, IdStore)"
FIELDS_STOW = " (IdStore,IdAliment) "

FIELDS_INSERT_STORE = " %(StoreName)s,%(Url)s"
FIELDS_INSERT_ALIMENT = " %(NameAlim)s,%(DescriptionAlim)s,%(NutritionGrade)s"
FIELDS_INSERT_ARRANGE = " %(IdCategory)s,%(IdAliment)s"
FIELDS_INSERT_CATEGORY = " %(CategoryType)s"
FIELDS_INSERT_FOODSAVE = " %(NameFood)s, %(NameAlim)s, %(DescriptionAlim)s, %(StoreName)s, %(IdCategory)s, %(Url)s, %(IdCategory)s, %(IdAliment)s,%(IdStore)s"
FIELDS_INSERT_STOW = " %(IdStore)s,%(IdAliment)s"

ID_STORE = " IdStore "
ID_ALIMENT = " IdAliment "
ID_CATEGORY = " IdCategory "

#Menu
TITLE = "Pur Beurre"
SUBTITLE = "Données OpenFoodFacts"