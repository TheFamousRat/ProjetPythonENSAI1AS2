# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:25:19 2019

@author: id1262

Fichier principal du programme
"""

from compte import Compte
from baseUtilisateur import BaseUtilisateur

pseudoUtilisateur = None #Pseudo de l'utilisateur actuel

testBase = BaseUtilisateur()
testBase.ajouterCompte(Compte("gérardLeFat","1234"))
print(testBase.identifiantsCorrects("gérardeFat","1234"))
