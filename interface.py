# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 15:31:58 2026

@author: maelysadoir
"""

import pyxel
from carte import *
from batiment import *
from indicateurs import *

# Dimensions
LARGEUR_FENETRE = 1000
HAUTEUR_FENETRE = 800
TAILLE_CASE = 50
LARGEUR_MENU = 200
TITLE="Dream Island"

class Interface:
    
    def __init__(self):
        pyxel.init(LARGEUR_FENETRE, HAUTEUR_FENETRE, title=TITLE)
        
        self.carte = Carte()
        self.jeu = Jeu()
        self.indicateurs = Indicateurs()
        
        # Au départ, on ne sait pas où est placé la souris, ni quel batiment est sélectionné. Donc par défaut on met "None".
        self.case_souris = None
        self.case_selectionnee = None
        self.batiment_selectionne = None
        self.mode = "placer" # par défaut (modifiable grâce à la méthode)
        
        # Les notifications
        self.messages = []
        
        
    def ajouter_message(self, texte):
        # On ne garde qu'un seul message à la fois
        self.messages = [texte]

    def case_valide(self, x, y):
        # Permet de vérifier si une case est dans la grille
        return 0 <= y < len(self.carte.grille) and 0 <= x < len(self.carte.grille[0])
        
    def mettre_a_jour(self):
        
        # Case sous la souris du joueur
        souris_x, souris_y = pyxel.mouse_x, pyxel.mouse_y
        self.case_souris = (souris_x // TAILLE_CASE, souris_y // TAILLE_CASE) # En divisant par TAILLE_CASE on obtient les coordonnées de la case sous la souris (utile pour plus tard)
        
        # Changer le MODE
        if pyxel.btnp(pyxel.KEY_P):
            self.mode = "placer"
            self.ajouter_message("Mode : Placer")
            
        elif pyxel.btnp(pyxel.KEY_S):
            self.mode = "supprimer"
            self.ajouter_message("Mode : Supprimer")
        
        elif pyxel.btnp(pyxel.KEY_I):
            self.mode = "info"
            self.ajouter_message("Mode : Info")

        # Clic souris
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if souris_x >= LARGEUR_FENETRE - LARGEUR_MENU:
                self.cliquer_bouton(souris_x, souris_y) 
            else:
                case_x = souris_x // TAILLE_CASE
                case_y = souris_y // TAILLE_CASE
                # Vérifie que le clic est dans la grille et pas sur le menu
                if self.case_valide(case_x, case_y) and souris_x < LARGEUR_FENETRE - LARGEUR_MENU:
                    self.case_selectionnee = (case_x, case_y) # Utile pour entourer la case sélectionnée (et utile pour interactions)
                    self.action_case(case_x, case_y) # Permet éventuellement de supprimer/ placer un bâtiment

                
        # Mettre à jour les indicateurs
        self.indicateurs.appliquer_variation()
        
        # On applique les effets des bâtiments placés
        for batiment, pos in self.jeu.batiments_places:
            self.indicateurs.modifier("argent", batiment.effet_argent)
            self.indicateurs.modifier("bonheur", batiment.effet_bonheur)
            self.indicateurs.modifier("population", batiment.effet_population)
            self.indicateurs.modifier("energie", getattr(batiment, 'effet_energie', 0))
            self.indicateurs.modifier("nourriture", getattr(batiment, 'effet_nourriture', 0))
            self.indicateurs.modifier("eau", getattr(batiment, 'effet_eau', 0))

    def action_case(self, x, y):
        # On vérifie d'abord que la case est dans la grille	
        if not self.case_valide(x, y):
            self.ajouter_message("Case hors limite")
            return

        if self.mode == "placer":
            if self.batiment_selectionne is None:
                self.ajouter_message("Aucun bâtiment sélectionné")
                return

            if not self.carte.verifier_case_libre(x, y):
                self.ajouter_message("Case occupée")
                return

            batiment = self.batiment_selectionne
            if self.jeu.ville.argent >= batiment.cout:
                self.jeu.acheter_batiment(batiment, (x, y))
                self.carte.placer_batiment(batiment, x, y)
                self.ajouter_message(f"{batiment.nom} construit !")
            else:
                self.ajouter_message("Pas assez d'argent")

        elif self.mode == "supprimer":
            if self.carte.verifier_case_libre(x, y):
                self.ajouter_message("Aucun bâtiment à supprimer")
            else:
                self.carte.supprimer_batiment(x, y)
                self.ajouter_message("Bâtiment supprimé")
        
        elif self.mode == "info":
            batiment = self.carte.voir_batiment(x,y)
            if batiment:
                texte = (
                    f"{batiment.nom} | Argent:{getattr(batiment, 'effet_argent', 0)} "
                    f"Pollution:{getattr(batiment, 'effet_pollution', 0)} "
                    f"Biodiv:{getattr(batiment, 'effet_biodiversite', 0)} "
                    f"Bonheur:{getattr(batiment, 'effet_bonheur', 0)} "
                    f"Pop:{getattr(batiment, 'effet_population', 0)}"
                )

                self.ajouter_message(texte)
            else :
                self.ajouter_message("Aucun bâtiment ici")

         
    def dessiner(self):
        pyxel.cls(7) # Pour l'instant fond blanc, on verra par la suite
        self.dessiner_carte()
        self.dessiner_menu()
        self.dessiner_hud()
        self.dessiner_notifications()
        self.dessiner_mode()
        
        
    def dessiner_carte(self):
        # Enumerate permet ici d'avoir des indices y et x utiles pour calculer par la suite la position en pixels
        for y, ligne in enumerate(self.carte.grille):
            for x, case in enumerate(ligne):
                couleur = 0 # Pour l'instant noir
                pyxel.rectb(x*TAILLE_CASE, y*TAILLE_CASE, TAILLE_CASE, TAILLE_CASE, couleur) # Dessine le contour de chaque case 
                if case["batiment"]:
                    pyxel.rect(x*TAILLE_CASE+2, y*TAILLE_CASE+2, TAILLE_CASE-4, TAILLE_CASE-4,12) # Pour l'instant, puisqu'on a pas de sprite, chaque bâtiment sera représentée par une case bleue sur la carte
                
        # Case survolée
        if self.case_souris:
            x, y = self.case_souris
            if self.case_valide(x, y):
                pyxel.rectb(x*TAILLE_CASE, y*TAILLE_CASE, TAILLE_CASE, TAILLE_CASE, 11)
 
        # Case sélectionnée
        if self.case_selectionnee:
            x, y = self.case_selectionnee
            if self.case_valide(x, y):
                pyxel.rectb(x*TAILLE_CASE, y*TAILLE_CASE, TAILLE_CASE, TAILLE_CASE, 8)
                
    
    def dessiner_menu(self):
        pyxel.rect(LARGEUR_FENETRE - LARGEUR_MENU, 0, LARGEUR_MENU, HAUTEUR_FENETRE, 6) # Représenté par une case grise
        
        # Boutons
        boutons = ["Boutique", "Info", "Poubelle"]
        for i, txt in enumerate(boutons):
            x = LARGEUR_FENETRE - LARGEUR_MENU + 10
            y = 10 + i*40
            pyxel.rect(x, y, 180, 30, 3)  # Représenté par une case verte
            pyxel.text(x+5, y+8, txt, 7)  # Le texte est blanc
            
            
    def dessiner_hud(self):
        y = 200
        for nom, valeur in self.indicateurs.valeurs.items():
            pyxel.text(LARGEUR_FENETRE-LARGEUR_MENU+10, y, f"{nom}: {valeur}", 0)
            y += 20


    def dessiner_notifications(self):
        for i, msg in enumerate(self.messages[-5:]):
            pyxel.text(10, HAUTEUR_FENETRE - 120 + i*20, msg, 0)
    
    
    def dessiner_mode(self):
        x = LARGEUR_FENETRE - LARGEUR_MENU + 10 
        y = 150  # juste au-dessus du HUD
        
        # Affiche le mode
        pyxel.text(x, y, f"Mode : {self.mode.capitalize()}", 0)  # 0 = noir


    def cliquer_bouton(self, souris_x, souris_y):
        boutons = ["Boutique", "Info", "Poubelle"]
        for i, txt in enumerate(boutons):
            x = LARGEUR_FENETRE - LARGEUR_MENU + 10
            y = 10 + i*40
            if x <= souris_x <= x + 180 and y <= souris_y <= y + 30:
                if txt == "Boutique":
                    self.ajouter_message("Boutique ouverte !")
                elif txt == "Info":
                    self.mode = "info"
                    self.ajouter_message("Mode info activé")
                elif txt == "Poubelle":
                    self.mode = "supprimer"
                    self.ajouter_message("Mode supprimer activé")


if __name__ == "__main__":
    interface = Interface()
    pyxel.run(interface.mettre_a_jour, interface.dessiner)
