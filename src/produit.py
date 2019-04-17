# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:26:23 2019

@author: id1262
"""

from datetime import date

defaultDate = date(1970,1,1)


#Classe décrivant un seul produit précisement
class Produit:
    code = 0
    pseudoCreateur = ""
    dateEnregistrement = defaultDate
    dateDerniereModif = defaultDate
    nom = ""
    quantite = ""
    lieuxFabrication = []
    lieuxVente = []
    paysVente = []
    ingredients = []
    
    def __init__(self, code_ = 0, pseudoCreateur_ = "", dateEnregistrement_ = defaultDate, dateDerniereModif_ = defaultDate, nom_ = "", quantite_ = 0, lieuxFabrication_ = [], lieuxVente_ = [], paysVente_ = [], ingredients_ = []):
        self.code = code_
        self.pseudoCreateur = pseudoCreateur_
        self.dateEnregistrement = dateEnregistrement_
        self.dateDerniereModif = dateDerniereModif_
        self.nom = nom_
        self.quantite = quantite_
        self.lieuxFabrication = lieuxFabrication_
        self.lieuxVente = lieuxVente_
        self.paysVente = paysVente_
        self.ingredients = ingredients_

    def __str__(self):
        toRet = ""
        toRet += "Le produit est " + str(self.nom)
        toRet += ", du code barre " + str(self.code)
        toRet += ", crée le " + str(self.dateEnregistrement )
        toRet += "et modifié le " + str(self.dateDerniereModif )
        toRet += ", de quantité " + str(self.quantite )
        toRet += ", fabriqué en " + str(self.lieuxFabrication )
        toRet += " et vendu à " + str(self.lieuxVente )
        toRet += " en " + str(self.paysVente)
        return toRet