# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:25:19 2019

@author: id1262

Fichier principal du programme
"""

from compte import Compte
from baseUtilisateur import BaseUtilisateur
from catalogue import Catalogue
import getpass

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
            nombreRecu = self.obtenirChoix(len(self.choixDispo[typeUtilisateur]))-1
            self.appliquerChoix(typeUtilisateur, nombreRecu)
            print(" ")
           
    def menuChoix(self, indexDicChoix : str):#Fonction affichant les choix disponibles à l'utilisateur
        for i in range(len(self.choixDispo[indexDicChoix])):
            print(" " + str(i+1) + "/" + self.choixDispo[indexDicChoix][i].description)
    
    def appliquerChoix(self, typeUtilisateur : str, choix : int):
        self.choixDispo[typeUtilisateur][choix].fonction()#On appelle la fonction liée au choix
            
    def obtenirChoix(self, choixMax : float, choixMin : float = 1.0, messageDemande : str = "Entrez votre choix : ") -> int:
        nombreRecu = ""
        while nombreRecu == "":
            nombreRecu = input(messageDemande)
            try:
                nombreRecu = int(nombreRecu)
                if nombreRecu < choixMin or nombreRecu > choixMax:
                    print("Erreur : choix inconnu")
                    nombreRecu = ""
            except ValueError:
                print("Erreur : type de variable incompatible (entrez un entier)")
                nombreRecu = ""
        return nombreRecu
    	
    def __init__(self):
        
        self.continuer = True
        self.choixDispo = {"utilisateur" : [], "contributeur" : [], "admin" : []} #Dictionnaires contenant les choix associés à chaque type d'utilisateur
        self.compteUtilisateur = None #Compte de l'utilisateur actuel (initialisé en rien)
        self.typeUtilisateur = "" #Un des 3 mentionnés au-dessus, utilisateur, contributeur ou admin
        self.catalogueOFF = Catalogue() #OFF = Open Food Facts
        self.baseUsers = BaseUtilisateur() #La base utilisateur
        
        #On initialise d'abord la base de données OFF
        self.catalogueOFF.chargerBase("../data/open_food_facts.csv")
        #Puis la base utilisateur
        self.baseUsers.ajouterCompte(Compte("FredPoul","jesuisvieux",False))
        self.baseUsers.ajouterCompte(Compte("Chad","Thunder",True))
        #Puis enfin les choix disponibles, qu'on lie à leurs fonctions respectives
        self.choixDispo["utilisateur"] = []
        self.choixDispo["contributeur"] = []
        self.choixDispo["admin"] = []
        #Les choix si l'utilisateur est non connecté
        self.choixDispo["utilisateur"].append(Choix("Afficher un produit", self.afficherProduit))
        self.choixDispo["utilisateur"].append(Choix("Afficher les ingrédients d'un produit", self.afficherIngredientsProduit))
        self.choixDispo["utilisateur"].append(Choix("Création de compte", self.creationCompte))
        self.choixDispo["utilisateur"].append(Choix("Connexion", self.connexion))
        self.choixDispo["utilisateur"].append(Choix("Quitter", self.quitter))
        #Si il est contributeur
        self.choixDispo["contributeur"].append(Choix("Afficher un produit", self.afficherProduit))
        self.choixDispo["contributeur"].append(Choix("Afficher les ingrédients d'un produit", self.afficherIngredientsProduit))
        self.choixDispo["contributeur"].append(Choix("Afficher n premiers produits ajoutés", self.affichierNPremiersProduits))
        self.choixDispo["contributeur"].append(Choix("Créer ou modifier un produit", self.dummy))
        self.choixDispo["contributeur"].append(Choix("Déconnexion", self.deconnecter))
        self.choixDispo["contributeur"].append(Choix("Quitter", self.quitter))
        #Si il est admin
        self.choixDispo["admin"].append(Choix("Afficher un produit", self.afficherProduit))
        self.choixDispo["admin"].append(Choix("Afficher les ingrédients d'un produit", self.afficherIngredientsProduit))
        self.choixDispo["admin"].append(Choix("Afficher n premiers produits ajoutés", self.affichierNPremiersProduits))
        self.choixDispo["admin"].append(Choix("Créer ou modifier un produit", self.dummy))
        self.choixDispo["admin"].append(Choix("Supprimer un produit", self.supprimerProduit))
        self.choixDispo["admin"].append(Choix("Valider ou supprimer un compte contributeur", self.validerSupprimerCompte))
        self.choixDispo["admin"].append(Choix("Deux statistiques au choix parmi trois", self.dummy))
        self.choixDispo["admin"].append(Choix("Un graphique au choix parmi deux", self.dummy))
        self.choixDispo["admin"].append(Choix("Déconnexion", self.deconnecter))
        self.choixDispo["admin"].append(Choix("Quitter", self.quitter))
    	
    def dummy(self):
        print("LE CODE DE CETTE OPTION N'A PAS ETE ECRIT")
    
    def validerSupprimerCompte(self):
        print("Choix disponibles :")
        print(" 1/Valider un compte")
        print(" 2/Supprimer un compte")
        choix = self.obtenirChoix(2,1)
        if choix == 1:
            pseudo = input("Pseudo à valider : ")
            self.baseUsers.validerCompte(pseudo)
        elif choix == 2:
            pseudo = input("Pseudo à supprimer : ")
            self.baseUsers.supprimerCompte(pseudo)
            
    def connexion(self):
        pseudo = input("Pseudo : ")
        mdp = getpass.getpass("Mot de passe : ")
        if self.baseUsers.identifiantsCorrects(pseudo,mdp):
            self.compteUtilisateur = self.baseUsers.obtenirCompte(pseudo)
            if self.compteUtilisateur != None:
                print("Connexion réussie")
        else:
            print("Erreur : identifiant non trouvé ou mot de passe incorrect.")
        
    def afficherProduit(self):
        codeDemande = self.obtenirChoix(float("inf"), 0.0, "Code du produit à visualiser : ")
        
        produitAAfficher = self.catalogueOFF.obtenirProduit(codeDemande)
        if produitAAfficher:
            print("\n" + produitAAfficher.__str__())
            
    def supprimerProduit(self):
        codeDemande = self.obtenirChoix(float("inf"), 0.0, "Code du produit à supprimer : ")
        if self.catalogueOFF.aLeProduitCode(codeDemande):
            self.catalogueOFF.supprimerProduitCode(codeDemande)
            print("Produit supprimé avec succès.")
        else:
            print("Code produit " + str(codeDemande) + " non trouvé dans la base. Aucune action supplémentaire.")
    
    def affichierNPremiersProduits(self):
        print("Vous pouvez afficher un nombre de produits allant de 0 à " + str(self.catalogueOFF.taille()))
        nombreDemande = self.obtenirChoix(self.catalogueOFF.taille())
        for i in range(nombreDemande):
            print(self.catalogueOFF.produits[i])
            
    def afficherIngredientsProduit(self):
        codeDemande = self.obtenirChoix(float("inf"), 0.0, "Code du produit à visualiser : ")
        
        produitAAfficher = self.catalogueOFF.obtenirProduit(codeDemande)
        if produitAAfficher:
            toPrint = ""
            for i in produitAAfficher.ingredients:
                toPrint += i
            print(toPrint)
            
    def creationCompte(self):
        pseudo = input("Pseudo : ")
        while self.baseUsers.pseudoDansBase(pseudo):
            print("Désolé, ce pseudo est déjà dans la base")
            pseudo = input("Entrez un nouveau pseudo : ")
        mdp = getpass.getpass("Mot de passe : ")
        nvCompte = Compte(pseudo, mdp, False)
        self.baseUsers.ajouterCompte(nvCompte)
        self.compteUtilisateur = nvCompte
            
    def deconnecter(self):
        print("Déconnexion")
        self.compteUtilisateur = None
        
    def quitter(self):
        print("Merci pour votre visite !")
        self.continuer = False
    
main = Main()
main.main()