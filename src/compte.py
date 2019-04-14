# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:18:32 2019

@author: id1262
"""

class Compte:
    motDePasse = ""
    pseudo = ""
    admin = False #Administrateur ou collaborateur
    
    def __init__(self, pseudo_ : str, motDePasse_ : str, administrateur_ : bool = False):
        self.pseudo = pseudo_
        self.motDePasse = motDePasse_
        self.admin = administrateur_
        
    