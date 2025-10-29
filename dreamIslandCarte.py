# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 17:50:33 2025

@author: anfalousaidane
"""

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
            
    def placer_batiment(self, x, y, batiment: str):
        if self.case_libre(x, y):
            self.grille[y][x] = batiment
            print(f"{batiment} placé en ({x}, {y})")
            return True
        else:
            print(f"Impossible de placer {batiment} en ({x}, {y}) : case occupée.")
            return False
        
    def supprimer_batiment(self, x, y):
        if not self.case_libre(x, y):
            print(f"{self.grille[y][x]} supprimé de ({x}, {y})")
            self.grille[y][x] = None
            return True
        else:
            print(f"Aucune construction à cet emplacement ({x}, {y})")
            return False
        
    
