# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:25:19 2019

@author: id1262

Fichier principal du programme
"""

from compte import Compte
from baseUtilisateur import BaseUtilisateur
from catalogue import Catalogue
from enum import Enum

class Choix:#Une simple classe qui contient la description associée à un choix, ainsi que la fonction appellée
    def __init__(self, desc, fonc):
        self.description = desc
        self.fonction = fonc

class Main:
    def main(self):
        
        print("Bienvenue dans la base OFF.")
        while (self.continuer):
            
            if self.compteUtilisateur:
                print("Vous êtes connecté sous le pseudo " + str(self.compteUtilisateur.pseudo) + (" (admin)." if self.compteUtilisateur.admin else "."))
            else:
                print("Vous n'êtes pas connecté")
            
            #On actualise le type de l'utilisateur
            if self.compteUtilisateur == None:
                typeUtilisateur = "utilisateur"
            elif self.compteUtilisateur.admin:
                typeUtilisateur = "admin"
            else:
                typeUtilisateur = "contributeur"
    
            print("\nTâches disponibles :")
            self.menuChoix(typeUtilisateur)
            nombreRecu = self.obtenirChoix(typeUtilisateur)
            self.appliquerChoix(typeUtilisateur, nombreRecu)
            print(" ")
           
    def menuChoix(self, indexDicChoix : str):#Fonction affichant les choix disponibles à l'utilisateur
        for i in range(len(self.choixDispo[indexDicChoix])):
            print(" " + str(i) + "/" + self.choixDispo[indexDicChoix][i].description)
    
    def appliquerChoix(self, typeUtilisateur : str, choix : int):
        self.choixDispo[typeUtilisateur][choix].fonction()#On appelle la fonction liée au choix
            
    def obtenirChoix(self, typeUtilisateur : str) -> int:
        nombreChoix = len(self.choixDispo[typeUtilisateur]) - 1
        nombreRecu = ""
        while nombreRecu == "":
            nombreRecu = input("Entrez votre choix : ")
            try:
                nombreRecu = int(nombreRecu)
                if nombreRecu < 0 or nombreRecu > nombreChoix:
                    print("Erreur : choix inconnu")
                    nombreRecu = ""
            except ValueError:
                print("Erreur : type de variable incompatible (entrez un entier)")
                nombreRecu = ""
        return nombreRecu
    	
    def __init__(self):
        
        self.continuer = True
        self.choixDispo = {"utilisateur" : [], "contributeur" : [], "admin" : []} #Dictionnaires contenant les choix associés à chaque type d'utilisateur
        self.compteUtilisateur = Compte("Boris","1234", False) #Pseudo de l'utilisateur actuel
        self.typeUtilisateur = "" #Un des 3 mentionnés au-dessus, utilisateur, contributeur ou admin
        self.catalogueOFF = Catalogue() #OFF = Open Food Facts
        self.baseUsers = BaseUtilisateur() #La base utilisateur
        
        #On initialise d'abord la base de données OFF
        self.catalogueOFF.chargerBase("../data/open_food_facts.csv")
        #Puis la base utilisateur
        self.baseUsers.ajouterCompte(Compte("FredPoul","jesuisvieux",False))
        #Puis enfin les choix disponibles, qu'on lie à leurs fonctions respectives
        self.choixDispo["utilisateur"] = []
        self.choixDispo["contributeur"] = []
        self.choixDispo["admin"] = []
        #Les choix si l'utilisateur est non connecté
        self.choixDispo["utilisateur"].append(Choix("Afficher un produit", self.dummy))
        self.choixDispo["utilisateur"].append(Choix("Afficher les ingrédients d'un produit", self.dummy))
        self.choixDispo["utilisateur"].append(Choix("Création de compte", self.dummy))
        self.choixDispo["utilisateur"].append(Choix("Connexion", self.dummy))
        self.choixDispo["utilisateur"].append(Choix("Quitter", self.quitter))
        #Si il est contributeur
        self.choixDispo["contributeur"].append(Choix("Afficher un produit", self.dummy))
        self.choixDispo["contributeur"].append(Choix("Afficher les ingrédients d'un produit", self.dummy))
        self.choixDispo["contributeur"].append(Choix("Afficher n premiers produits ajoutés", self.dummy))
        self.choixDispo["contributeur"].append(Choix("Créer ou modifier un produit", self.dummy))
        self.choixDispo["contributeur"].append(Choix("Déconnexion", self.deconnecter))
        self.choixDispo["contributeur"].append(Choix("Quitter", self.quitter))
        #Si il est admin
        self.choixDispo["admin"].append(Choix("Afficher un produit", self.dummy))
        self.choixDispo["admin"].append(Choix("Afficher les ingrédients d'un produit", self.dummy))
        self.choixDispo["admin"].append(Choix("Afficher n premiers produits ajoutés", self.dummy))
        self.choixDispo["admin"].append(Choix("Créer ou modifier un produit", self.dummy))
        self.choixDispo["admin"].append(Choix("Supprimer un produit", self.dummy))
        self.choixDispo["admin"].append(Choix("Valider ou supprimer un compte contributeur", self.dummy))
        self.choixDispo["admin"].append(Choix("Deux statistiques au choix parmi trois", self.dummy))
        self.choixDispo["admin"].append(Choix("Un graphique au choix parmi deux", self.dummy))
        self.choixDispo["admin"].append(Choix("Déconnexion", self.deconnecter))
        self.choixDispo["admin"].append(Choix("Quitter", self.quitter))
    	
    def dummy(self):
        print("FONCTION NON-TERMINEE")
        
    def deconnecter(self):
        print("Déconnexion")
        self.compteUtilisateur = None
        
    def quitter(self):
        self.continuer = False
    
main = Main()
main.main()