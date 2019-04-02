# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:22:09 2019

@author: id1262

Ce fichier contient la classe BaseUtilisateur, qui contient les comptes de tous les utilisateurs enregistrés
"""

from compte import Compte

class BaseUtilisateur:
    comptes = []
    
    def __init__(self):
        pass
    
    #Cherche si le pseudo est dans la base
    def pseudoDansBase(self, pseudoCherche : str) -> bool:
        ret = False
        for comp in self.comptes:
            if comp.pseudo == pseudoCherche:
                ret = True
                break
        return ret
        
    #Ajoute un compte dans la base, si son pseudo n'est pas déjà présent
    def ajouterCompte(self, nouveauCompte : Compte):
        if not self.pseudoDansBase(nouveauCompte.pseudo):
            self.comptes.append(nouveauCompte)
        else:
            print("Le pseudo " + str(nouveauCompte.pseudo) + " est déjà pris")
            
    #Verifie si les identifiants (mdp + pseudo) sont présents dans la base (en couple)
    def identifiantsCorrects(self, pseudo : str, motDePasse : str):
        ret = False
        for comp in self.comptes:
            if comp.pseudo == pseudo and comp.motDePasse == motDePasse:
                ret = True
                break
        return ret

        
