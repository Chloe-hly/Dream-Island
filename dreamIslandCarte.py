# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 17:50:33 2025

@author: anfalousaidane
"""
import json

CONTRAINTES_PROXIMITE = {
    "Villa": ["Usine", "Bidonville"],
    "Forêt": ["Usine", "Port marchand"],
    "École primaire": ["Usine"],
    "Parc": ["Usine"],
    "Maison": [],
    "Usine": [],
    "Bidonville": [],
    "Port marchand": [],
}

class Island:
    def __init__(self,  largeur=30,  hauteur=14):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [[None for _ in range(largeur)] for _ in range(hauteur)]#avec None qui représente les cases vides
        
    def case_libre(self, x: int, y: int):
        if 0 <= x < self.largeur and 0 <= y < self.hauteur:
           return self.grille[y][x] is None
        else:
           print("Position hors de la carte.")
           return False         
  
    def batiments_adjacents(self, x, y):
        adjacents = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # gauche, droite, haut, bas
        for dx, dy in directions:
            nx= x + dx
            ny= y + dy
            if 0 <= nx < self.largeur and 0 <= ny < self.hauteur:
                batiment = self.grille[ny][nx]
                if batiment:
                    adjacents.append(batiment)
        return adjacents          
    
    def placer_batiment(self, x, y, batiment):
        if not self.case_libre(x, y):
            print(f"Impossible de placer {batiment} en ({x}, {y}) : case occupée.")
            return False
        interdits = CONTRAINTES_PROXIMITE.get(batiment, [])
        adjacents = self.batiments_adjacents(x, y)
        for voisin in adjacents:
            if voisin in interdits:
                print(f"{batiment} ne peut pas être à côté de {voisin} en ({x}, {y})")
                return False
            
        self.grille[y][x] = batiment
        print(f"{batiment} placé en ({x}, {y})")
        return True
        
    def supprimer_batiment(self, x, y):
        if not self.case_libre(x, y):
            print(f"{self.grille[y][x]} supprimé de ({x}, {y})")
            self.grille[y][x] = None
            return True
        else:
            print(f"Aucune construction à cet emplacement ({x}, {y})")
            return False
        
    #def coordonées_case(self, x, y):
        #par défauts python self.grille->[y][x] mais coordonnées= [x][y] donc faut code qui inverse
        
            
    def get_batiments(self):
        batiments = []
        for y in range(self.hauteur):
            for x in range(self.largeur):
                bat=self.grille[y][x]
                if bat:    
                    batiments.append({"type": bat,"x": x,"y": y})
        return batiments
    
    def charger_batiments(self, donnees):
        for bat in donnees:
            x= bat["x"]
            y= bat["y"]
            self.grille[y][x] = bat["type"]
    
    def afficher_grille(self):
        for ligne in self.grille:
            ligne_affichee = []
            for b in ligne:
                if b:
                    ligne_affichee.append(b[0])
                else:
                    ligne_affichee.append(".")
    
            print(" ".join(ligne_affichee))
            

#Sauvegarde JSON à vérifier 
def sauvegarder(ile, nom_fichier="sauvegarde.json"):
    donnees = ile.get_batiments()
    with open(nom_fichier, "w") as f:
        json.dump(donnees, f, indent=2)
    print(f"Sauvegarde réussie dans {nom_fichier}")
    
#Chargement JSON à vérifier aussi 
def charger(nom_fichier="sauvegarde.json"):
    with open(nom_fichier, "r") as f:
        donnees = json.load(f)
    ile = Island()
    ile.charger_batiments(donnees)
    print(f"Chargement réussi depuis {nom_fichier}")
    return ile

      
