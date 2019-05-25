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
        self.menu_base()
   
        choice = input()    
        #Selection menu choice
        if choice == "1":
            self.menu_category()
            # Select category
            choice_category = input()
            self.choice_category(choice_category)
            #select Aliment
            choice_aliment = input()
            self.choice_aliment(choice_category,choice_aliment,request,cursor,connection)
 
        if choice == "2":
            print("Donnez le nom de la recherche \n ")
            NameFood = input()
            Foodsave = request.Foodsave_query(cursor)
            print(Foodsave)

#-------------------------------------------------------------------#
    # Show menu 
    def menu_base(self):
        print(TITLE)
        print(SUBTITLE)
        print("1 Quel aliment souhaitez-vous remplacer?")
        print("2 Retrouver mes aliments substitués")
        print("3 Exit")

    # Show category menu
    def menu_category(self):
        print("Sélectionnez la catégorie \n ")
        print("1 Aliments et boissons à base de végétaux")
        print("2 Spreads")
        print("3 Produits laitiers")
        print("4 Surgelés")

    # Show category choice
    def choice_category(self,choice_category):
        if choice_category == "1":          
            self.list_category1()
        if choice_category == "2":          
            self.list_category2()
        if choice_category == "3":          
            self.list_category3()
        if choice_category == "4":        
            self.list_category4()
    
    # Show aliment choice
    def choice_aliment(self,choice_category,choice_aliment,request,cursor,connection):
        if choice_aliment == "1":          
            IdAliment = self.subs_Alim1(choice_category, request,cursor)
            self.save_search(IdAliment, request,cursor,connection)
        if choice_aliment == "2":          
            IdAliment = self.subs_Alim2(choice_category,request,cursor)
            self.save_search(IdAliment, request,cursor,connection)
        if choice_aliment == "3":          
            self.subs_Alim3(choice_category,request,cursor)
            self.save_search( request,cursor,connection)
        if choice_aliment == "4":        
            self.subs_Alim4(choice_category,request,cursor)
            self.save_search( request,cursor,connection)

    def list_category1(self):
        print("Selectionnez l'aliment \n ")
        print("1 Corn Flakes")
        print("2 Muesli Bio Jordans")
        print("3 Lentilles vertes Bio")
        print("4 Kellog's All-Bran")

    def list_category2(self):
        print("Selectionnez l'aliment \n ")
        print("1 Escalope Cordon Bleu")
        print("2 Miel de fleurs liquide")
        print("3 Nesquik")
        print("4 Pâte brisée Tarte en Or")
    
    def list_category3(self):
        print("Selectionnez l'aliment \n ")
        print("1 Parmigiano Reggiano râpé frais")
        print("2 Chaussée aux Moines")
        print("3 Camembert")
        print("4 Mozzarella (18 % MG)")
    
    def list_category4(self):
        print("Selectionnez l'aliment \n ")
        print("1 Lasagnes Bolognaise Pur Bœuf")
        print("2 8 portions panées de Colin d'Alaska")
        print("3 Lasagnes à la bolognaise, Surgelées")

    def subs_Alim1(self,choice_category,request,cursor):
        if choice_category == 1:
            NameAlim = "Corn Flakes"
            IdCategorie = "1"
            
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            IdAliment = Aliment["IdAliment"]

            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                    "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))
            

        if choice_category == 2:
            NameAlim = "Escalope Cordon Bleu"
            IdCategorie = "74"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            IdAliment = Aliment["IdAliment"]
            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                    "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))

        if choice_category == 3:
            NameAlim = "Parmigiano Reggiano râpé frais"
            IdCategorie = "6"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            IdAliment = Aliment["IdAliment"]
            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                    "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))

        if choice_category == 4:
            NameAlim = "Lasagnes Bolognaise Pur Bœuf"
            IdCategorie = "26"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            IdAliment = Aliment["IdAliment"]
            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                   "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))
        return(IdAliment)

    def subs_Alim2(self,choice_category,request,cursor):
        if choice_category == 1:
            NameAlim = "Muesli Bio Jordans"
            IdCategorie = "1"
            
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            IdAliment = Aliment["IdAliment"]
            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                    "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))
        
        if choice_category == 2:
            NameAlim = "Miel de fleurs liquide"
            IdCategorie = "74"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            IdAliment = Aliment["IdAliment"]
            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                    "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))

        if choice_category == 3:
            NameAlim = "Chaussée aux Moines"
            IdCategorie = "6"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            IdAliment = Aliment["IdAliment"]
            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                    "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))

        if choice_category == 4:
            NameAlim = "8 portions panées de Colin d'Alaska"
            IdCategorie = "26"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            IdAliment = Aliment["IdAliment"]
            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                   "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))
        return(IdAliment)
    
    def subs_Alim3(self,choice_category,request,cursor):
        if choice_category == 1:
            NameAlim = "Lentilles vertes Bio"
            IdCategorie = "1"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                    "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))
        
        if choice_category == 2:
            NameAlim = "Nesquik"
            IdCategorie = "74"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                    "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))

        if choice_category == 3:
            NameAlim = "Camembert"
            IdCategorie = "6"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                    "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))

        if choice_category == 4:
            NameAlim = "Lasagnes à la bolognaise, Surgelées"
            IdCategorie = "26"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                   "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))
    
    def subs_Alim4(self,choice_category,request,cursor):
        if choice_category == 1:
            NameAlim = "Kellog's All-Bran"
            IdCategorie = "1"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                    "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))
        
        if choice_category == 2:
            NameAlim = "Pâte brisée Tarte en Or"
            IdCategorie = "74"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                    "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))

        if choice_category == 3:
            NameAlim = "Mozzarella (18 % MG)"
            IdCategorie = "6"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie)
            print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n Description :{p[DescriptionAlim]} \n" +
                    "Store: {p[NameStore]}  \n Url: {p[Url]} \n").format(p=Aliment))


    def save_search(self, IdAliment, request,cursor,connection):
        print("Voulez-vous enregistrer? \n ")
        print("1 Oui")
        print("2 Non")
        save = input()
        if save == "1":
            data_foodsave =[]
            Foodsave = {}
            print("Donnez un nom a votre recherche \n ")
            NameFoodsave = input()

            Foodsave["NameFood"] = NameFoodsave
            Foodsave["IdAliment"] = IdAliment
            #insertion in foodsave table
            data_foodsave.append(Foodsave)
            request.Foodsave(cursor,data_foodsave)
            print("Recherche bien enregistrée!! \n ")
            #print(data_foodsave)
        if save == "2":
            self.menu(cursor,connection)