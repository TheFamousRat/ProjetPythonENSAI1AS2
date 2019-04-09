# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:53:50 2019

@author: id1262

Ce fichier contient la classe catalogue, qui contient tous les produits enregistrés, et permet d'effectuer des opérations sur ces derniers
"""

import csv
from produit import Produit #Avec une majuscule désigne la classe
from datetime import date

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

    def reinitialiserBase(self) -> None:
        del self.produits[:]

    #Charge un fichier csv contenant les données
    def chargerBase(self, baseDeDonnes : str):
        index = 0
        self.reinitialiserBase()
        
        with open(baseDeDonnes, newline='',encoding="utf8") as csvfile:
            
            fileReader = csv.reader(csvfile, delimiter="	", quotechar='|')
            
            for row in fileReader:
                if index == 0:#La première ligne n'a que les en-têtes
                    pass
                else:
                    self.produits.append(Produit())
                    currentIndex = len(self.produits) - 1
                    #0 code barre
                    self.produits[currentIndex].code = int(row[0])
                    #1 créateur
                    self.produits[currentIndex].pseudoCreateur = row[1]
                    #2 date création
                    self.produits[currentIndex].dateEnregistrement = date.fromtimestamp(int(row[2]))
                    #3 dernière modif
                    self.produits[currentIndex].dateDerniereModif = date.fromtimestamp(int(row[3]))
                    #4 nom
                    self.produits[currentIndex].nom = row[4]
                    #5 quantité
                    self.produits[currentIndex].quantite = row[5]
                    #6 lieux fabrication
                    for i in row[6].split(','):
                        self.produits[currentIndex].lieuxFabrication.append(i)
                    #7 lieux vente
                    for i in row[7].split(','):
                        self.produits[currentIndex].lieuxVente.append(i)
                    #8 pays vente
                    for i in row[8].split(','):
                        self.produits[currentIndex].paysVente.append(i)
                    #9 ingrédients
                    for i in row[9].split(','):
                        self.produits[currentIndex].ingredients.append(i)

                index+=1

dummy = Catalogue()
dummy.chargerBase("../data/open_food_facts.csv")