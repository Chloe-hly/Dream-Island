# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:55:57 2026

@author: anfalousaidane
"""

import json

# Contraintes de proximité entre bâtiments
# La clé est le nom du bâtiment posé
# La valeur est la liste des bâtiments interdits à côté
CONTRAINTES_PROXIMITE = {
    "Villa": ["Usine", "Bidonville"],
    "Forêt": ["Usine", "Port marchand"],
    "École primaire": ["Usine", "Bidonville"],
    "Parc": ["Usine"],
    "Maison": ["Usine"],
    "Usine": ["Villa", "Forêt", "École primaire", "Parc", "Maison"],
    "Bidonville": ["Villa"],
    "Port marchand": ["Forêt"],
}

class Carte:
   
    def __init__(self):
       # On ne va pas placer en paramètre largeur, hauteur, taille_case
       # car on va par défaut mettre la carte en 15*15 et une case mesure 50 pixels
       self.largeur = 15  # Le nombre de colonnes x
       self.hauteur = 15  # Le nombre de lignes y
       
       self.taille_case = 50  # La taille d'une case, ici en pixels
       
       # Création de la grille vide
       # Ici, chaque case est un dictionnaire qui contient les coordonnées et les bâtiments
       self.grille = []
       for y in range(self.hauteur):
           ligne = []
           for x in range(self.largeur):
               case = None
               ligne.append(case)
           self.grille.append(ligne)
            
    def verifier_case_libre(self, x, y):
        # Doit return True si la case est libre
        # Si la case ne contient pas de bâtiment, elle renvoie None (donc True)
        # Dans le cas contraire, si elle contient un bâtiment elle renvoie False
        if 0 <= x < self.largeur and 0 <= y < self.hauteur:
            return self.grille[y][x] is None
        return False
    
    def batiments_adjacents(self, x, y):
        # Retourne la liste des bâtiments adjacents (haut, bas, gauche, droite)
        adjacents = []
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < self.largeur and 0 <= ny < self.hauteur:
                bat = self.grille[ny][nx]
                if bat is not None:
                    adjacents.append(bat)
        return adjacents
    
    def placer_batiment(self, batiment, x, y):
        # On peut placer un bâtiment si la case est libre
        # et si les contraintes de proximité sont respectées
        if not self.verifier_case_libre(x, y):
            print("Case déjà occupée")
            return False
        
        # Vérification des contraintes de proximité
        interdits = CONTRAINTES_PROXIMITE.get(batiment.nom, [])
        adjacents = self.batiments_adjacents(x, y)
        for voisin in adjacents:
            if voisin.nom in interdits:
                print("Contraintes de proximité non respectées")
                return False
        
        self.grille[y][x] = batiment
        print(batiment.nom + " placé en (" + str(x) + "," + str(y) + ")")
        return True
            
    def supprimer_batiment(self, x, y):
        # Supprime le bâtiment si la case est occupée
        if 0 <= x < self.largeur and 0 <= y < self.hauteur:
            if self.grille[y][x] is not None:
                print(self.grille[y][x].nom + " est supprimé")
                self.grille[y][x] = None
                return True
        return False
            
    def voir_batiment(self, x, y):
        # Permet de voir, si le joueur clique sur une case, le nom du bâtiment
        # et renvoie None si la case ne contient rien
        if 0 <= x < self.largeur and 0 <= y < self.hauteur:
            return self.grille[y][x]
        return None
    
    def afficher_carte_console(self):
        # Permet d'afficher la carte dans la console pour voir rapidement
        # ce qu'il y a sur la carte (partie dev, pas partie finale)
        for ligne in self.grille:
            print([case.nom[0] if case else "." for case in ligne])

    
#Sauvegarde JSON à vérifier 
def sauvegarder(ile, nom_fichier="sauvegarde.json"):
    donnees = ile.get_batiments() #Demande à l'objet ile de me donner la liste de tous les bâtiments présents sur la carte et stocke cette liste dans donnees
    with open(nom_fichier, "w") as f: #ouvre le fichier en écriture 
        json.dump(donnees, f, indent=2) # ca transforme la liste Python en JSON
    print(f"Sauvegarde réussie dans {nom_fichier}")
    
#Chargement JSON à vérifier aussi 
def charger(nom_fichier="sauvegarde.json"):
    with open(nom_fichier, "r") as f:
        donnees = json.load(f)
    ile = Carte()
    ile.charger_batiments(donnees)
    print(f"Chargement réussi depuis {nom_fichier}")
    return ile