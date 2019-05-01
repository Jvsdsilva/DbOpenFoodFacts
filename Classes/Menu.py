#Genere Menu

class Menu():


    def __init__(self):
            # Call the parent class constructor
            super().__init__()

            self._category = " "
            self._aliment = " "
       
    # function to get value of _age 
    def get_category(self): 
         print("getter method called") 
         return self._category 
       
    # function to set value of _age 
    def set_category(self, category): 
        print("setter method called") 
        self._category = category


    def genere_menu(self):
        print("Pur Beurre Bonjour, \n 1. Print Quel aliment souhaitez-vous remplacer ? \n 2. Print Retrouver mes aliments substitués.")
        choice = input()    
        
        if choice == "1":
            print("Sélectionnez la catégorie,\n 1. Print Categorie1 \n 2. Print Categorie2 \n 3. Print Categorie3 ")
            choice_category = input()

            if choice_category == "1":
                print("categorie1")
            if choice_category == "2":
                print("categorie2")
            if choice_category == "3":
                print("categorie3")
        
        if choice == "2":
            print("Recherche liste ")

            self.set_category(choice_category)
