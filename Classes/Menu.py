#Genere Menu
# Import the necessary packages
from Classes import DbRequests
from constants import *

class Menu():


    def __init__(self):
            # Call the parent class constructor
            super().__init__()

    def menu(self,cursor,connection):
        request = DbRequests.DbRequests()

        print(TITLE)
        print(SUBTITLE)
        print("1 Quel aliment souhaitez-vous remplacer?")
        print("2 Retrouver mes aliments substitués")
        print("3 Exit")
        
        choice = input()    
        
        if choice == "1":

            print("Sélectionnez la catégorie \n ")
            print("1 category1")
            print("2 category2")
            print("3 category3")
            print("4 category4")

            choice_category = input()
            
            if choice_category == "1":          
                print("Selectionnez l'aliment \n ")

                print("1 Corn Flakes")
                print("2 Muesli Bio Jordans")
                print("3 mails rouge")
                print("4 Kellog's All-Bran")
                choice_alim1 = input()
                if choice_alim1 == "1":
                    NameAlim = "Corn Flakes"
                    IdCategorie = "12090"
                    Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
                    print("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n Store: {p[NameStore]}  \n Url: {p[Url]} \n".format(p=Aliment))
                    
                    print("Voulez-vous enregistrer? \n ")
                    print("1 Oui")
                    print("2 Non")
                    enregistrer = input()
                    if enregistrer == "1":
                        data_foodsave =[]
                        Foodsave = {}
                        print("Donnez un nom a votre recherche \n ")
                        NameFoodsave = input()
                        IdAliment = "5"

                        Foodsave["NameFood"] = NameFoodsave
                        Foodsave["IdAliment"] = IdAliment
                       
                        #print(NameFoodsave)
                        #insertion in foodsave table
                        data_foodsave.append(Foodsave)
                        request.Insert_Db(cursor,TFOODSAVE,FIELDS_FOODSAVE,FIELDS_INSERT_FOODSAVE, data_foodsave) #?????????#
                        connection.commit()
                        #print(data_foodsave)
                    if enregistrer == "2":
                        print(TITLE)
                        print(SUBTITLE)
                        print("1 Quel aliment souhaitez-vous remplacer?")
                        print("2 Retrouver mes aliments substitués")
                        print("3 Exit")
                
        if choice == "2":
            print("Donnez le nom de la recherche \n ")
            NameFood = input()
            Foodsave = request.Foodsave_query(cursor, NameFood)
            print("Recherche liste ")

