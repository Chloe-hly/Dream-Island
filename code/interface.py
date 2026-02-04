# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 15:31:58 2026

@author: maelysadoir
"""
# -*- coding: utf-8 -*-
import pygame
from carte import *
from batiment import *
from indicateurs import *

# Dimensions
LARGEUR_FENETRE = 1000
HAUTEUR_FENETRE = 800
TAILLE_CASE = 50
LARGEUR_MENU = 200
TITLE = "Dream Island"

class Interface:
    
    def __init__(self):
        # Initialisation de pygame
        pygame.init()
        self.screen = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 16)
        
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
        
        self.running = True
        
    def ajouter_message(self, texte):
        # On ne garde qu'un seul message à la fois
        self.messages = [texte]

    def case_valide(self, x, y):
        # Permet de vérifier si une case est dans la grille
        return 0 <= y < len(self.carte.grille) and 0 <= x < len(self.carte.grille[0])
        
    def mettre_a_jour(self):
        # Gestion des événements pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                # Changer le MODE
                if event.key == pygame.K_p:
                    self.mode = "placer"
                    self.ajouter_message("Mode : Placer")
                elif event.key == pygame.K_s:
                    self.mode = "supprimer"
                    self.ajouter_message("Mode : Supprimer")
                elif event.key == pygame.K_i:
                    self.mode = "info"
                    self.ajouter_message("Mode : Info")

            # Clic souris
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                souris_x, souris_y = pygame.mouse.get_pos()
                
                if souris_x >= LARGEUR_FENETRE - LARGEUR_MENU:
                    self.cliquer_bouton(souris_x, souris_y)
                else:
                    case_x = souris_x // TAILLE_CASE
                    case_y = souris_y // TAILLE_CASE
                    # Vérifie que le clic est dans la grille et pas sur le menu
                    if self.case_valide(case_x, case_y):
                        self.case_selectionnee = (case_x, case_y) # Utile pour entourer la case sélectionnée
                        self.action_case(case_x, case_y)

        # Case sous la souris du joueur
        souris_x, souris_y = pygame.mouse.get_pos()
        self.case_souris = (souris_x // TAILLE_CASE, souris_y // TAILLE_CASE)

        # Mettre à jour les indicateurs
        self.indicateurs.appliquer_variation()
        
        # On applique les effets des bâtiments placés
        for batiment, pos in self.jeu.batiments_places:
            self.indicateurs.modifier("argent", getattr(batiment, "effet_argent", 0))
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
            batiment = self.carte.voir_batiment(x, y)
            if batiment:
                texte = (
                    f"{batiment.nom} | Argent:{getattr(batiment, 'effet_argent', 0)} "
                    f"Pollution:{getattr(batiment, 'effet_pollution', 0)} "
                    f"Biodiv:{getattr(batiment, 'effet_biodiversite', 0)} "
                    f"Bonheur:{getattr(batiment, 'effet_bonheur', 0)} "
                    f"Pop:{getattr(batiment, 'effet_population', 0)}"
                )
                self.ajouter_message(texte)
            else:
                self.ajouter_message("Aucun bâtiment ici")

    def dessiner(self):
        self.screen.fill((255, 255, 255)) # Pour l'instant fond blanc, on verra par la suite
        self.dessiner_carte()
        self.dessiner_menu()
        self.dessiner_hud()
        self.dessiner_notifications()
        self.dessiner_mode()
        pygame.display.flip()
        
    def dessiner_carte(self):
        # Enumerate permet ici d'avoir des indices y et x utiles pour calculer par la suite la position en pixels
        for y, ligne in enumerate(self.carte.grille):
            for x, case in enumerate(ligne):
                pygame.draw.rect(
                    self.screen, (0, 0, 0),
                    (x*TAILLE_CASE, y*TAILLE_CASE, TAILLE_CASE, TAILLE_CASE), 1
                )
                if case["batiment"]:
                    pygame.draw.rect(
                        self.screen, (0, 120, 255),
                        (x*TAILLE_CASE+2, y*TAILLE_CASE+2, TAILLE_CASE-4, TAILLE_CASE-4)
                    )

        # Case survolée
        if self.case_souris:
            x, y = self.case_souris
            if self.case_valide(x, y):
                pygame.draw.rect(
                    self.screen, (255, 200, 0),
                    (x*TAILLE_CASE, y*TAILLE_CASE, TAILLE_CASE, TAILLE_CASE), 2
                )

        # Case sélectionnée
        if self.case_selectionnee:
            x, y = self.case_selectionnee
            if self.case_valide(x, y):
                pygame.draw.rect(
                    self.screen, (255, 0, 0),
                    (x*TAILLE_CASE, y*TAILLE_CASE, TAILLE_CASE, TAILLE_CASE), 2
                )

    def dessiner_menu(self):
        pygame.draw.rect(
            self.screen, (180, 180, 180),
            (LARGEUR_FENETRE - LARGEUR_MENU, 0, LARGEUR_MENU, HAUTEUR_FENETRE)
        )

        # Boutons
        boutons = ["Boutique", "Info", "Poubelle"]
        for i, txt in enumerate(boutons):
            x = LARGEUR_FENETRE - LARGEUR_MENU + 10
            y = 10 + i*40
            pygame.draw.rect(self.screen, (0, 150, 0), (x, y, 180, 30))
            texte = self.font.render(txt, True, (255, 255, 255))
            self.screen.blit(texte, (x+5, y+7))

    def dessiner_hud(self):
        y = 200
        for nom, valeur in self.indicateurs.valeurs.items():
            texte = self.font.render(f"{nom}: {valeur}", True, (0, 0, 0))
            self.screen.blit(texte, (LARGEUR_FENETRE - LARGEUR_MENU + 10, y))
            y += 20

    def dessiner_notifications(self):
        for i, msg in enumerate(self.messages[-5:]):
            texte = self.font.render(msg, True, (0, 0, 0))
            self.screen.blit(texte, (10, HAUTEUR_FENETRE - 120 + i*20))

    def dessiner_mode(self):
        x = LARGEUR_FENETRE - LARGEUR_MENU + 10 
        y = 150  # juste au-dessus du HUD
        texte = self.font.render(f"Mode : {self.mode.capitalize()}", True, (0, 0, 0))
        self.screen.blit(texte, (x, y))

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
    while interface.running:
        interface.clock.tick(60)
        interface.mettre_a_jour()
        interface.dessiner()
    pygame.quit()
