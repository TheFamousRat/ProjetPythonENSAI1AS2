# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:53:50 2019

@author: id1262

Ce fichier contient la classe catalogue, qui contient tous les produits enregistrés, et permet d'effectuer des opérations sur ces derniers
"""

import csv
from produit import Produit #Avec une majuscule désigne la classe

class Catalogue:
    produits = []
    def __init__(self):
        pass
    
    def ajouterProduit(self, nouveauProduit : Produit):
        if not self.aLeProduit(nouveauProduit):
            self.produits.append(nouveauProduit)
            
    def supprimerProduit(self, produitCible : Produit):
        self.supprimerProduitCode(produitCible.code)
        
    def supprimerProduitCode(self, codeProduitCible : int):
        indexProduitCible = self.indexProduitCode(codeProduitCible)
        if indexProduitCible != -1:
            self.produits.pop(indexProduitCible)
            
    #Donne l'index dans le tableau du produit ayant un certain code (-1 sinon)
    def indexProduitCode(self, codeProduitCherche : int) -> int:
        indexProduit = -1
        for i in range(0, len(self.produits)):
            if self.produits[i].code == codeProduitCherche:
                indexProduit = i
                break
        return indexProduit
    
    def indexProduit(self, produitCherche : Produit) -> int:
        return self.indexProduitCode(produitCherche.code)
        
    #Cherche si le catalogue a déjà un certain Produit
    def aLeProduit(self, produitCherche : Produit) -> bool:
        return self.aLeProduitCode(produitCherche.code)#Suppose que chaque code est unique à un produit
        
    #Cherche si un produit avec un certain code est déjà enregistré
    def aLeProduitCode(self, codeCherche : int) -> bool:
        return self.indexProduitCode(codeCherche) != -1
        
    #Charge un fichier csv contenant les données
    def chargerBase(self, baseDeDonnes : str):
        index = 0
        with open(baseDeDonnes, newline='') as csvfile:
            fileReader = csv.reader(csvfile, delimiter="	", quotechar='|')
            for row in fileReader:
                if index == 0:#La première ligne n'a que les en-têtes
                    pass
                else:
                    print(row[0])
                index+=1

myAss = Catalogue()
myAss.chargerBase("../data/open_food_facts.csv")