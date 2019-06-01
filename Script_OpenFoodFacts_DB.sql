#------------------------------------------------------------
# Table: CATEGORY
#------------------------------------------------------------

CREATE TABLE CATEGORY(
        IdCategory   Int  Auto_increment  NOT NULL ,
        NameCategory Varchar (550) NOT NULL
	,CONSTRAINT CATEGORY_PK PRIMARY KEY (IdCategory)
);

#------------------------------------------------------------
# Table: ALIMENT
#------------------------------------------------------------

CREATE TABLE ALIMENT(
        IdAliment       Int  Auto_increment  NOT NULL ,
        NameAlim        Varchar (250) NOT NULL ,
        NameStore       Varchar (250) NOT NULL ,
        Url             Varchar (500) NOT NULL ,
        DescriptionAlim Varchar (1500) NOT NULL ,
        NutritionGrade  Varchar (250) NOT NULL ,
        IdCategory      Int
	,CONSTRAINT ALIMENT_PK PRIMARY KEY (IdAliment)
	,CONSTRAINT ALIMENT_CATEGORY_FK FOREIGN KEY (IdCategory) REFERENCES CATEGORY(IdCategory)
);

#------------------------------------------------------------
# Table: FOODSAVE
#------------------------------------------------------------

CREATE TABLE FOODSAVE(
        IdFood    Int  Auto_increment  NOT NULL,
        IdAliment Int
	,CONSTRAINT FOODSAVE_PK PRIMARY KEY (IdFood)
	,CONSTRAINT FOODSAVE_ALIMENT_FK FOREIGN KEY (IdAliment) REFERENCES ALIMENT(IdAliment)
);