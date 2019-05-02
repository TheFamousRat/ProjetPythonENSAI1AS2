# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:22:09 2019

@author: id1262

Ce fichier contient la classe BaseUtilisateur, qui contient les comptes de tous les utilisateurs enregistrés
"""

from compte import Compte

class BaseUtilisateur:
    """
    Classe contenant une base de données d'utilisateur, et contenant diverses méthodes d'interaction avec la base
    """
    comptes = []
    
    def __init__(self):
        """
        Méthode vide
        """
        pass
    
    def obtenirCompte(self, pseudo : str) -> Compte:
        """
        Si il existe, retourne le compte associé à un certain pseudonyme. Sinon retourne None
        """
        for comp in self.comptes:
            if comp.pseudo == pseudo:
                return comp
        return None
    
    #Cherche si le pseudo est dans la base
    def pseudoDansBase(self, pseudoCherche : str) -> bool:
        """
        Cherche si un certain pseudonyme est présent dans la base
        """
        return (self.obtenirCompte(pseudoCherche) != None)
        
    #Ajoute un compte dans la base, si son pseudo n'est pas déjà présent
    def ajouterCompte(self, nouveauCompte : Compte):
        """
        Ajoute un certain compte dans la base, sous réserve que le pseudonyme y étant associé ne soit pas présent dans la base
        """
        if not self.pseudoDansBase(nouveauCompte.pseudo):
            self.comptes.append(nouveauCompte)
        else:
            print("Le pseudo " + str(nouveauCompte.pseudo) + " est déjà pris")
    
    def supprimerCompte(self, pseudo : str):
        """
        
        """
        self.comptes.remove(self.obtenirCompte(pseudo))
        
    def validerCompte(self, pseudo : str):
        idx = self.comptes.index(self.obtenirCompte(pseudo))
        if idx == -1:
            print("Erreur : compte de pseudo " + pseudo + " introuvable")
        else:
            self.comptes[idx].admin = True
            
    #Verifie si les identifiants (mdp + pseudo) sont présents dans la base (en couple)
    def identifiantsCorrects(self, pseudo : str, motDePasse : str):
        ret = False
        for comp in self.comptes:
            if comp.pseudo == pseudo and comp.motDePasse == motDePasse:
                ret = True
                break
        return ret

    
