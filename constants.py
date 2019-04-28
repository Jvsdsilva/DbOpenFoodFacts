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
FIELDS_ALIMENT = " (NameAlim,DescriptionAlim,Nutriment_score) "
FIELDS_ARRANGE = " (IdCategory,IdAliment) "
FIELDS_CATEGORY = " (CategoryType) "
FIELDS_FOODSAVE = " (NameFood, IdCategory, IdAliment, IdStore)"
FIELDS_STOW = " (IdStore,IdAliment) "