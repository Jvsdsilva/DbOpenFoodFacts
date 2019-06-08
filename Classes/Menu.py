# Genere Menu
# Import the necessary packages
from Classes import DbRequests
from constants import *


class Menu():

    def __init__(self):
        # Call the parent class constructor
        super().__init__()

    def menu(self, cursor, connection):
        request = DbRequests.DbRequests()
        self.menu_base()
        choice = input()
        if choice == "1" or choice == "2" or choice == "3":
            # Selection menu choice
            if choice == "1":
                self.menu_category()
                self.choice_1(request, cursor, connection)

            if choice == "2":
                self.choice_2(request, cursor)
        else:
            self.menu(cursor, connection)

# ------------------------------------------------------------------- #
    # Menu choice one
    def choice_1(self, request, cursor, connection):
        # Select category
        choice_category = input()
        self.choice_category(choice_category, request, cursor, connection)
        if choice_category == "1" or choice_category == "2" \
           or choice_category == "3":
            # Select Aliment
            choice_aliment = input()
            if choice_aliment == "1" or choice_aliment == "2" \
               or choice_aliment == "3" or choice_aliment == "4":
                self.choice_aliment(choice_category, choice_aliment, request,
                                    cursor, connection)
            else:
                self.choice_category(choice_category, request, cursor,
                                     connection)
                choice_aliment = input()
                self.choice_aliment(choice_category, choice_aliment, request,
                                    cursor, connection)
        else:
            self.menu_category()
            choice_category = input()
            self.choice_category(choice_category, request, cursor, connection)

    # Menu choice two
    def choice_2(self, request, cursor):
        # Save search
        Foodsave = request.Foodsave_query(cursor)
        for food in Foodsave:
            print(("Vous recherches \n\n Aliment :{p[NameAlim]} \n" +
                   "Description :{p[DescriptionAlim]} \n " +
                   "Store: {p[NameStore]} \n" +
                   "Url: {p[Url]} \n").format(p=food))

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

    # Show category choice
    def choice_category(self, choice_category, request, cursor, connection):
        if choice_category == "1":
            self.list_category1()
        if choice_category == "2":
            self.list_category2()
        if choice_category == "3":
            self.list_category3()

    # Show aliment choice
    def choice_aliment(self, choice_category, choice_aliment, request, cursor,
                       connection):
        if choice_aliment == "1":
            self.subs_Alim1(choice_category, request, cursor)

        elif choice_aliment == "2":
            self.subs_Alim2(choice_category, request, cursor)

        elif choice_aliment == "3":
            self.subs_Alim3(choice_category, request, cursor)

        elif choice_aliment == "4":
            self.subs_Alim4(choice_category, request, cursor)
        else:
            self.choice_aliment(choice_category, choice_aliment, request,
                                cursor, connection)
        # return Id Aliment
        if choice_category == "1":
            NameAlim = "Ravioles du Dauphiné"
            idalim = request.Get_id_alim(cursor, NameAlim, TALIMENT)
            IdAliment = idalim["IdAliment"]

        if choice_category == "2":
            NameAlim = "Kiri à la crème de lait (8 Portions)"
            idalim = request.Get_id_alim(cursor, NameAlim, TALIMENT)
            IdAliment = idalim["IdAliment"]

        if choice_category == "3":
            NameAlim = "Parmigiano Reggiano râpé frais"
            idalim = request.Get_id_alim(cursor, NameAlim, TALIMENT)
            IdAliment = idalim["IdAliment"]
        # Save search
        self.save_search(IdAliment, request, cursor, connection)

    # Category list 1
    def list_category1(self):
        print("Selectionnez l'aliment \n ")
        print("1 Corn Flakes")
        print("2 Muesli Bio Jordans")
        print("3 Lentilles vertes Bio")
        print("4 Kellog's All-Bran")

    # Category list 2
    def list_category2(self):
        print("Selectionnez l'aliment \n ")
        print("1 Escalope Cordon Bleu")
        print("2 Miel de fleurs liquide")
        print("3 Nesquik")
        print("4 Pâte brisée Tarte en Or")

    # Category list 3
    def list_category3(self):
        print("Selectionnez l'aliment \n ")
        print("1 Cancoillotte fabriquée en Franche-Comté")
        print("2 Chaussée aux Moines")
        print("3 Camembert")
        print("4 Mozzarella (18 % MG)")

    # Aliments choice 1 by category
    def subs_Alim1(self, choice_category, request, cursor):
        self.choice_categ1_alim1(choice_category, request, cursor)
        self.choice_categ2_alim1(choice_category, request, cursor)
        self.choice_categ3_alim1(choice_category, request, cursor)

    # Aliments choice 2 by category
    def subs_Alim2(self, choice_category, request, cursor):
        self.choice_categ1_alim2(choice_category, request, cursor)
        self.choice_categ2_alim2(choice_category, request, cursor)
        self.choice_categ3_alim2(choice_category, request, cursor)

    # Aliments choice 3 by category
    def subs_Alim3(self, choice_category, request, cursor):
        self.choice_categ1_alim3(choice_category, request, cursor)
        self.choice_categ2_alim3(choice_category, request, cursor)
        self.choice_categ3_alim3(choice_category, request, cursor)

    # Aliments choice 4 by category
    def subs_Alim4(self, choice_category, request, cursor):
        self.choice_categ1_alim4(choice_category, request, cursor)
        self.choice_categ2_alim4(choice_category, request, cursor)
        self.choice_categ3_alim4(choice_category, request, cursor)

    # Save search
    def save_search(self, idaliment, request, cursor, connection):
        print("Voulez-vous enregistrer? \n ")
        print("1 Oui")
        print("2 Non")
        save = input()
        # choice
        if save == "1":
            data_foodsave = []
            Foodsave = {}
            Foodsave["IdAliment"] = idaliment

            # insertion in foodsave table
            data_foodsave.append(Foodsave)
            request.Foodsave(cursor, data_foodsave)
            print("Recherche bien enregistrée!! \n ")
            self.menu(cursor, connection)

        if save == "2":
            self.menu(cursor, connection)

    def request_aliment(self, request, cursor, NameAlim, IdCategorie,
                        NutritionGrade):
        Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie,
                                        NutritionGrade)

        # If not nutrition grade A we continue to search
        if Aliment == "0":
            NutritionGrade = "b"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie,
                                            NutritionGrade)
        elif Aliment == "0":
            NutritionGrade = "c"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie,
                                            NutritionGrade)
        else:
            NutritionGrade = "d"
            Aliment = request.Aliment_query(cursor, NameAlim, IdCategorie,
                                            NutritionGrade)
        
        print(("Nous vous proposons \n\n Name: {p[NameAlim]} \n " +
               "Description :{p[DescriptionAlim]} \n" +
               "Store: {p[NameStore]}  \n " +
               "Url: {p[Url]} \n").format(p=Aliment))

    # Choice aliment1 in category 1
    def choice_categ1_alim1(self, choice_category, request, cursor):
        if choice_category == "1":
            NameAlim = "Corn Flakes"
            IdCategorie = "1"
            NutritionGrade = "a"
            self.request_aliment(request, cursor, NameAlim, IdCategorie,
                                 NutritionGrade)

    # Choice aliment1 in category 2
    def choice_categ2_alim1(self, choice_category, request, cursor):
        if choice_category == "2":
            NameAlim = "Escalope Cordon Bleu"
            IdCategorie = "4203"
            NutritionGrade = "a"
            self.request_aliment(request, cursor, NameAlim, IdCategorie,
                                 NutritionGrade)

    # Choice aliment1 in category 3
    def choice_categ3_alim1(self, choice_category, request, cursor):
        if choice_category == "3":
            NameAlim = "Parmigiano Reggiano râpé frais"
            IdCategorie = "6"
            NutritionGrade = "a"
            self.request_aliment(request, cursor, NameAlim, IdCategorie,
                                 NutritionGrade)

    # Choice aliment2 in category 1
    def choice_categ1_alim2(self, choice_category, request, cursor):
        if choice_category == "1":
            NameAlim = "Muesli Bio Jordans"
            IdCategorie = "1"
            NutritionGrade = "a"
            self.request_aliment(request, cursor, NameAlim, IdCategorie,
                                 NutritionGrade)

    # Choice aliment2 in category 2
    def choice_categ2_alim2(self, choice_category, request, cursor):
        if choice_category == "2":
            NameAlim = "Miel de fleurs liquide"
            IdCategorie = "4203"
            NutritionGrade = "a"
            self.request_aliment(request, cursor, NameAlim, IdCategorie,
                                 NutritionGrade)

    # Choice aliment2 in category 3
    def choice_categ3_alim2(self, choice_category, request, cursor):
        if choice_category == "3":
            NameAlim = "Chaussée aux Moines"
            IdCategorie = "6"
            NutritionGrade = "a"
            self.request_aliment(request, cursor, NameAlim, IdCategorie,
                                 NutritionGrade)

    # Choice aliment3 in category 1
    def choice_categ1_alim3(self, choice_category, request, cursor):
        if choice_category == "1":
            NameAlim = "Lentilles vertes Bio"
            IdCategorie = "1"
            NutritionGrade = "a"
            self.request_aliment(request, cursor, NameAlim, IdCategorie,
                                 NutritionGrade)

    # Choice aliment3 in category 2
    def choice_categ2_alim3(self, choice_category, request, cursor):
        if choice_category == "2":
            NameAlim = "Nesquik"
            IdCategorie = "4203"
            NutritionGrade = "a"
            self.request_aliment(request, cursor, NameAlim, IdCategorie,
                                 NutritionGrade)

    # Choice aliment3 in category 3
    def choice_categ3_alim3(self, choice_category, request, cursor):
        if choice_category == "3":
            NameAlim = "Camembert"
            IdCategorie = "6"
            NutritionGrade = "a"
            self.request_aliment(request, cursor, NameAlim, IdCategorie,
                                 NutritionGrade)

    # Choice aliment4 in category 1
    def choice_categ1_alim4(self, choice_category, request, cursor):
        if choice_category == "1":
            NameAlim = "Kellog's All-Bran"
            IdCategorie = "1"
            NutritionGrade = "a"
            self.request_aliment(request, cursor, NameAlim, IdCategorie,
                                 NutritionGrade)

    # Choice aliment4 in category 2
    def choice_categ2_alim4(self, choice_category, request, cursor):
        if choice_category == "2":
            NameAlim = "Pâte brisée Tarte en Or"
            IdCategorie = "4203"
            NutritionGrade = "a"
            self.request_aliment(request, cursor, NameAlim, IdCategorie,
                                 NutritionGrade)

    # Choice aliment4 in category 3
    def choice_categ3_alim4(self, choice_category, request, cursor):
        if choice_category == "3":
            NameAlim = "Mozzarella (18 % MG)"
            IdCategorie = "6"
            NutritionGrade = "a"
            self.request_aliment(request, cursor, NameAlim, IdCategorie,
                                 NutritionGrade)
