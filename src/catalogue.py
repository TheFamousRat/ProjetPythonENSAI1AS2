# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:53:50 2019

@author: id1262
"""

from produit import Produit #Avec une majuscule désigne la classe

class Catalogue:
    produits = []
    def __init__(self):
        pass
    def ajouterProduit(self, nouveauProduit : Produit):
        self.produits.append(nouveauProduit)
        
    #Cherche si le catalogue a déjà un certain Produit
    def aLeProduit(self, produitCherche : Produit) -> bool:
        return self.aLeProduitCode(produitCherche.code)#Suppose que chaque code est unique à un produit
        
    def aLeProduitCode(self, codeCherche : int) -> bool:
        ret = False
        for prod in self.produits:
            if prod.code == codeCherche:
                ret = True
                break
        return ret
    
catTest = Catalogue()
truc = Produit()
catTest.ajouterProduit(truc)
print(catTest.aLeProduitCode(1))