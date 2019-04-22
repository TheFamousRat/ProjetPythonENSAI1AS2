# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:25:19 2019

@author: id1262

Fichier principal du programme
"""

import numpy as np
import matplotlib.pyplot as plt
import getpass

from datetime import date
from compte import Compte
from baseUtilisateur import BaseUtilisateur
from catalogue import Catalogue
from produit import Produit

class Choix:#Une simple classe qui contient la description associée à un choix, ainsi que la fonction appellée
    def __init__(self, desc, fonc):
        self.description = desc
        self.fonction = fonc

def inputRepete(demandeNouvelInput : str = "Ajouter un input"):
    print("Appuyez sur entrée pour arrêter")
    inputs = []
    inputs.append(input(demandeNouvelInput))
    while inputs[len(inputs) - 1] != "":
        inputs.append(input(demandeNouvelInput))
    inputs.pop()
    return inputs
        
class Main:
    def main(self):
        """
        Boucle principale.
        Tant que l'instruction de s'arrêter n'est pas donnée, elle demandera continuellement à l'utilisateur ses nouveaux choix
        """
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
           
    def menuChoix(self, indexDicChoix : str):
        """
        Fonction affichant les choix disponibles à l'utilisateur
        """
        for i in range(len(self.choixDispo[indexDicChoix])):
            print(" " + str(i+1) + "/" + self.choixDispo[indexDicChoix][i].description)
    
    def appliquerChoix(self, typeUtilisateur : str, choix : int):
        """
        Appelle la méthode associée à un type d'utilisateur et à un choix
        """
        self.choixDispo[typeUtilisateur][choix].fonction()#On appelle la fonction liée au choix
            
    def obtenirChoix(self, choixMax : float, choixMin : float = 1.0, messageDemande : str = "Entrez votre choix : ") -> int:
        """
        Fonction demandant à l'utilisateur un entier dans l'intervalle [choixMin,choixMax], et vérifiant que le nombre rentré est bien du bon format
        """
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
        """
        Initialise le catalogue, la base utilisateur, associe éventuellement un compte à l'utilisateur actuel, puis associe les choix possibles (et les méthodes leur étant liés) à certains status (utilisateur, admin etc.)
        """
        self.continuer = True
        self.choixDispo = {"utilisateur" : [], "contributeur" : [], "admin" : []} #Dictionnaires contenant les choix associés à chaque type d'utilisateur
        self.compteUtilisateur = Compte("Chad","Thunder",True) #Compte de l'utilisateur actuel (initialisé en rien)
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
        self.choixDispo["contributeur"].append(Choix("Créer ou modifier un produit", self.creerModifProd))
        self.choixDispo["contributeur"].append(Choix("Déconnexion", self.deconnecter))
        self.choixDispo["contributeur"].append(Choix("Quitter", self.quitter))
        #Si il est admin
        self.choixDispo["admin"].append(Choix("Afficher un produit", self.afficherProduit))
        self.choixDispo["admin"].append(Choix("Afficher les ingrédients d'un produit", self.afficherIngredientsProduit))
        self.choixDispo["admin"].append(Choix("Afficher n premiers produits ajoutés", self.affichierNPremiersProduits))
        self.choixDispo["admin"].append(Choix("Créer ou modifier un produit", self.creerModifProd))
        self.choixDispo["admin"].append(Choix("Supprimer un produit", self.supprimerProduit))
        self.choixDispo["admin"].append(Choix("Valider ou supprimer un compte contributeur", self.validerSupprimerCompte))
        self.choixDispo["admin"].append(Choix("Deux statistiques au choix parmi trois", self.dummy))
        self.choixDispo["admin"].append(Choix("Un graphique au choix parmi deux", self.choixGraphique))
        self.choixDispo["admin"].append(Choix("Déconnexion", self.deconnecter))
        self.choixDispo["admin"].append(Choix("Quitter", self.quitter))
    	
    def dummy(self):
        """
        Fonction utilisée pour retrouver rapidement dans le code les fonctions incomplétes. Inutile en lui-même
        """
        print("LE CODE DE CETTE OPTION N'A PAS ETE ECRIT")
        
    def statsDesc(self):
        pass
        
    def creerModifProd(self):
        """
        Demande à l'utilisateur si il souhaite modifier ou bien ajouter un produit, et le redirige vers la méthode adaptée
        """
        print("Options disponibles :")
        print(" 1/Ajout d'un nouveau produit")
        print(" 2/Modification d'un produit existant")
        
        choix = self.obtenirChoix(2.0, 1.0, "Entrez votre choix : ")
        
        if choix == 1:
            self.ajouterProd()
        elif choix == 2:
            self.modifProduit()
            
    def modifProduit(self):
        """
        Propose à l'utilisateur de modifier les attributs de son choix. 
        Les attributs non-listes sont directement remplacés, tandis que les attributs listes peuvent être complétés à la place, sur la demande de l'utilisateur
        """
        codeDemande = self.obtenirChoix(float("inf"), 0.0, "Code du produit à modifier : ")
        
        produitModif = self.catalogueOFF.obtenirProduit(codeDemande)
        
        if produitModif:
            choix = 1
            attrDesc = []#Liste contenant la description dans le choix de l'attribut ainsi que le nom de l'attribut lui-même
            attrDesc.append(["Nom","nom"])
            attrDesc.append(["Quantité","quantite"])
            attrDesc.append(["Lieux de fabrication","lieuxFabrication"])
            attrDesc.append(["Lieux de vente","lieuxVente"])
            attrDesc.append(["Pays de vente","paysVente"])
            attrDesc.append(["Ingrédients","ingredients"])
            attrDesc.append(["Quitter",""])
            
            while attrDesc[choix][1] != "":
                print("Etat actuel du produit : " + str(produitModif))
                print("Choisissez l'attribut à modifier : ")
                for i in range(len(attrDesc)):
                    print(" " + str(i+1) + "/" + str(attrDesc[i][0]))
                
                choix = self.obtenirChoix(len(attrDesc), 1.0) - 1
                
                if attrDesc[choix][1] != "":
                    if type(getattr(produitModif, attrDesc[choix][1])) == int:
                        setattr(produitModif, attrDesc[choix][1], self.obtenirChoix(float("inf"),0.0,"Entrez la nouvelle valeur"))
                        
                    elif type(getattr(produitModif, attrDesc[choix][1])) == list:
                        print("Souhaitez-vous :")
                        print(" 1/Remplacer les élèments")
                        print(" 2/En ajouter d'autres")

                        if self.obtenirChoix(2.0,1.0) == 1:
                            setattr(produitModif, attrDesc[choix][1], inputRepete("Ajouter une valeur : "))
                        else:
                            setattr(produitModif, attrDesc[choix][1], getattr(produitModif, attrDesc[choix][1]) + inputRepete("Ajouter une valeur : "))
                            
                    elif type(getattr(produitModif, attrDesc[choix][1])) == str:
                        setattr(produitModif, attrDesc[choix][1], input("Entrez la nouvelle valeur : "))
                
            produitModif.dateDerniereModif = date.today()
            self.catalogueOFF.mettreAJourProduit(codeDemande, produitModif)
            
    def ajouterProd(self):
        """
        Ajoute un produit. Les attributs nécessaires sont demandés un à un à l'utilisateur
        """
        code = self.obtenirChoix(float("inf"), 0.0, "Entrez le code produit : ")
        nom = input("Nom du produit : ")
        quantite = input("Quantité (veuillez préciser l'unité) : ")
        lieuxFabrication = inputRepete("Ajouter un lieu de fabrication : ")
        lieuxVente = inputRepete("Ajouter un lieu de vente : ")
        paysVente = inputRepete("Ajouter un pays de vente : ")
        ingredients = inputRepete("Ajouter un ingrédient : ")
        
        nvProd = Produit(code,self.compteUtilisateur.pseudo,date.today(),date.today(),nom,quantite,lieuxFabrication,lieuxVente,paysVente,ingredients)
        self.catalogueOFF.ajouterProduit(nvProd)
        print("Produit ajouté : " + nvProd.__str__())

    def choixGraphique(self):
        """
        Demande à l'utilisateur lequel des deux graphiques il souhaite, puis le redirige vers la méthode adaptée
        """
        print("Graphiques disponibles :")
        print(" 1/Boxplot des contributions")
        print(" 2/Histogramme des pays de vente")
        
        choix = self.obtenirChoix(2.0, 1.0, "Entrez le numéro du graphique désiré : ")
    
        if choix == 1:
            mini = self.obtenirChoix(float("inf"), 0.0, "Entrez le nombre minimum de contributions pour prendre en compte l'utilisateur : ")
            self.boxplotContrib(mini)
        else:
            mini = self.obtenirChoix(float("inf"), 0.0, "Entrez le nombre minimum de points de vente pour prendre en compte le pays : ")
            self.barplotPays(mini)
        
    def boxplotContrib(self, contribMin : int = 0):
        """
        Boxplot illustrant la dispersion des contributions utilisateurs, et ne prenant en compte que les utilisateurs ayant une quantité de contributions minimale (donnée par l'utilisateur)
        Le boxplot est ensuite sauvegardé dans une image au format png et nommée de manière à informer du paramètre
        """
        dictContrib = {} #Contient les contributions des utilisateurs, la clé d'accès étant leur pseudo

        for contrib in self.catalogueOFF.produits:
            if contrib.pseudoCreateur in dictContrib:
                dictContrib[contrib.pseudoCreateur] += 1
            else:
                dictContrib[contrib.pseudoCreateur] = 1
        
        contribList = []
        for contributeur in dictContrib:
            if dictContrib[contributeur] >= contribMin:
                contribList.append(dictContrib[contributeur])

        plt.boxplot(contribList)
        plt.savefig("BoxplotContribMin_Param="+str(contribMin)+".png")
        plt.close()
        
    def barplotPays(self, occMin : int = 0):
        """
        Barplot illustrant le nombre de produits enregistrés par pays. Il est possible de ne montrer que les pays apparaissant un certain nombre de fois, avec un paramètre donné par l'utilisateur (par défaut 0)
        Le barplot est ensuite sauvegardé dans une image au format png et nommée de manière à informer du paramètre
        """
        dictPays = {}

        for prod in self.catalogueOFF.produits:
            for pays in prod.paysVente:
                if pays in ["Greece","Griekenland"]:#On procède ainsi afin d'éviter les occurences entre pays dues à des langues différentes
                    pays = "Grèce"
                elif pays in [" en:france","Francia","Frankrijk"]:
                    pays = "France"
                elif pays in ["Belgium"," en:belgium","België"]:
                    pays = "Belgique"
                elif pays in ["Spain","Spanje","España"]:
                    pays = "Espagne"
                elif pays in ["Italy","Italia"]:
                    pays = "Italie"
                elif pays in [" en:french-polynesia"]:
                    pays = "Polynésie française"
                elif pays in [" en:switzerland"]:
                    pays = "Suisse"
                
                if pays in dictPays:
                    dictPays[pays] += 1
                else:
                    dictPays[pays] = 1
        pays = [] #Liste servant d'abscisse au graphique
        occurencesPays = [] #Liste lui servant d'ordonnée
        for key in dictPays:
            if dictPays[key] >= occMin:#On filtre les pays ayant une trop faible contribution
                pays.append(key)
                occurencesPays.append(dictPays[key])
            
        y_pos = np.arange(len(pays))
        
        plt.bar(y_pos, occurencesPays)
        plt.xticks(y_pos, pays)
        plt.savefig("BarplotPaysVente_Param="+str(occMin)+".png")
        plt.close()
        
    def validerSupprimerCompte(self):
        """
        Donne la possibilité à un administrateur de valider ou supprimer un compte. Cette méthode prend son choix et le redirige vers la méthode adéquate
        """
        
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
        """
        Méthode demandant à l'utilisateur un mot de passe et un pseudo. Si ils sont tous les deux correctement présents dans la base, l'utilisateur est connecté sous ce pseudo
        """
        pseudo = input("Pseudo : ")
        mdp = getpass.getpass("Mot de passe : ")
        if self.baseUsers.identifiantsCorrects(pseudo,mdp):
            self.compteUtilisateur = self.baseUsers.obtenirCompte(pseudo)
            if self.compteUtilisateur != None:
                print("Connexion réussie")
        else:
            print("Erreur : identifiant non trouvé ou mot de passe incorrect.")
        
    def afficherProduit(self):
        """
        Affiche un produit à l'aide de son code
        """
        codeDemande = self.obtenirChoix(float("inf"), 0.0, "Code du produit à visualiser : ")
        
        produitAAfficher = self.catalogueOFF.obtenirProduit(codeDemande)
        if produitAAfficher:
            print("\n" + produitAAfficher.__str__())
            
    def supprimerProduit(self):
        """
        Supprime un produit à l'aide de son code
        """
        codeDemande = self.obtenirChoix(float("inf"), 0.0, "Code du produit à supprimer : ")
        if self.catalogueOFF.aLeProduitCode(codeDemande):
            self.catalogueOFF.supprimerProduitCode(codeDemande)
            print("Produit supprimé avec succès.")
        else:
            print("Code produit " + str(codeDemande) + " non trouvé dans la base. Aucune action supplémentaire.")
    
    def affichierNPremiersProduits(self):
        """
        Affiche les n premiers produits présents dans la base, n étant donné par l'utilisateur
        """
        print("Vous pouvez afficher un nombre de produits allant de 0 à " + str(self.catalogueOFF.taille()))
        nombreDemande = self.obtenirChoix(self.catalogueOFF.taille())
        for i in range(nombreDemande):
            print(self.catalogueOFF.produits[i])
            
    def afficherIngredientsProduit(self, codeDemande = -1):#Si le code demandé vaut -1, alors il faut demander à l'utilisateur quel code il souhaite. Sinon on continue la méthode avec le code fourni
        """
        Affiche les ingrédients d'un produit identifié par un code. Il est possible que le programme appelle la fonction directement, dans ce cas le code ne sera pas demandé à l'utilisateur (si codeDemande est différent de -1)
        """        
        if codeDemande == -1:
            codeDemande = self.obtenirChoix(float("inf"), 0.0, "Code du produit à visualiser : ")
        
        produitAAfficher = self.catalogueOFF.obtenirProduit(codeDemande)
        if produitAAfficher:
            toPrint = ""
            for i in produitAAfficher.ingredients:
                toPrint += i
            print(toPrint)
            
    def creationCompte(self):
        """
        Permet à l'utilisateur de créer un compte, sous réserve que le pseudonyme qu'il souhaite utiliser ne soit pas déjà présent dans la base
        """
        pseudo = input("Pseudo : ")
        while self.baseUsers.pseudoDansBase(pseudo):
            print("Désolé, ce pseudo est déjà dans la base")
            pseudo = input("Entrez un nouveau pseudo : ")
        mdp = getpass.getpass("Mot de passe : ")
        nvCompte = Compte(pseudo, mdp, False)
        self.baseUsers.ajouterCompte(nvCompte)
        self.compteUtilisateur = nvCompte
            
    def deconnecter(self):
        """
        Associe la valeur "None" au compte utilisateur, ce que le programme intérprète comme une déconnexion
        """
        print("Déconnexion")
        self.compteUtilisateur = None
        
    def quitter(self):
        """
        Litérallement, dit au programme d'arrêter de continuer la boucle principale
        """
        print("Merci pour votre visite !")
        self.continuer = False
    
main = Main()
main.main()