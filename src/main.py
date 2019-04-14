# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:25:19 2019

@author: id1262

Fichier principal du programme
"""

from compte import Compte
from baseUtilisateur import BaseUtilisateur
from catalogue import Catalogue

compteUtilisateur = Compte("Boris","1234", False) #Pseudo de l'utilisateur actuel
catalogueOFF = Catalogue() #OFF = Open Food Facts
baseUsers = BaseUtilisateur()

NOMBRE_DE_CHOIX = 0

def main():
	init() # On initialise le code
	
	continuer = True
	while (continuer):
		print("Bienvenue dans la base OFF.")
		if compteUtilisateur:
			print("Vous êtes connecté sous le pseudo " + str(compteUtilisateur.pseudo) + (" (admin)." if compteUtilisateur.admin else "."))
		else:
			print("Vous n'êtes pas connecté")
		print("\nTâches disponibles :")
		#On va maintenant afficher les tâches en fonction de la connexion ou non de l'utilisateur (et de ses droits)
		print(" 1/Afficher un produit")
		print(" 2/Afficher les ingrédients d'un produit")
		if compteUtilisateur == None:#L'utilisateur n'est pas connecté
			print(" 3/Création de compte")
			print(" 4/Connection")
			NOMBRE_DE_CHOIX = 4
		else:
			print(" 3/Afficher n premiers produits ajoutés")
			print(" 4/Créer ou modifier un produit")
			print(" 5/Déconnexion")
			if compteUtilisateur.admin:
				print(" 6/Supprimer un produit")
				print(" 7/Valider ou supprimer un compte contributeur")
				print(" 8/Deux statistiques au choix parmi trois")
				print(" 9/Un graphique au choix parmi deux")
				NOMBRE_DE_CHOIX = 9
			else:
				NOMBRE_DE_CHOIX = 5
		
		nombreRecu = ""
		while nombreRecu == "":
			nombreRecu = input("Entrez votre choix : ")
			try:
				nombreRecu = int(nombreRecu)
				if nombreRecu < 0 or nombreRecu > NOMBRE_DE_CHOIX:
					print("Erreur : choix inconnu")
					nombreRecu = ""
			except ValueError:
				print("Erreur : type de variable incompatible (entrez un entier)")
				nombreRecu = ""
			
	
def init():
	catalogueOFF.chargerBase("../data/open_food_facts.csv")
	baseUsers.ajouterCompte(Compte("FredPoul","jesuisvieux",False))
	
main()