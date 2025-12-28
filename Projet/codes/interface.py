import pyxel
from Carte import *
from Batiment import *
from Indicateurs import *

# Dimensions
LARGEUR_FENETRE = 1000
HAUTEUR_FENETRE = 800
TAILLE_CASE = 50
LARGEUR_MENU = 200

class Interface:
    
    def __init__(self):
        pyxel.init(LARGEUR_FENETRE, HAUTEUR_FENETRE, caption="Dream Island Interface")
        
        self.carte = Carte()
        self.jeu = Jeu()
        self.indicateurs = Indicateurs()
        
        # Au départ, on ne sait pas où est placé la souris, ni quel batiment est sélectionné. Donc par défaut on met "None" car ces instances nous serviront plus tard
        self.case_souris = None
        self.case_selectionnee = None
        self.batiment_selectionne = None
        self.mode = "placer" # par défaut, on peut changer ça plus tard, grâce à la méthode
        
        # Les notifications
        self.messages = []
        
        pyxel.run(self.mettre_a_jour, self.dessiner)
        
    def mettre_a_jour(self):
        
        # Case sous la souris du joueur
        souris_x, souris_y = pyxel.mouse_x, pyxel.mouse_y
        self.case_souris = (souris_x // TAILLE_CASE, souris_y // TAILLE_CASE) # En divisant par TAILLE_CASE on obtient les coordonnées de la case sous la souris (utile pour plus tard)
        
        # Changer le MODE
        if pyxel.btnp(pyxel.KEY_P):
            self.mode = "placer"
            self.messages.append("Mode : Placer")
            
        elif pyxel.btnp(pyxel.KEY_S):
            self.mode = "suppprimer"
            self.messages.append("Mode : Supprimer")
        
        # Clic souris
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if souris_x < LARGEUR_FENETRE - LARGEUR_MENU: # Permet de détecter si le joueur clique sur la carte, ou s'il clique sur le menu (ou autre part)
                case_x = souris_x // TAILLE_CASE
                case_y = souris_y // TAILLE_CASE
                self.case_selectionnee = (case_x, case_y) # Utile plus tard pour entourer la case sélectionnée (et utile pour interactions)
                self.action_case(case_x, case_y) # Permet éventuellement de supprimer/ placer un bâtiment
                
        # Mettre à jour les indicateurs
        self.indicateurs.appliquer_variation()
    
    def action_case(self, x, y):
        if self.mode == "placer" and self.batiment_selectionne:
            batiment = self.batiment_selectionee
            if self.jeu.ville.argent >= batiment.cout:
                self.jeu.acheter_batiment(batiment, (x,y))
                self.carte.placer_batiment(batiment, x, y)
                self.messages.append(f"{batiment.nom} construit !")
            else:
                self.messages.append("Pas assez d'argent")
                
        elif self.mode == "supprimer":
            self.carte.supprimer_batiment(x,y)
            self.messages.append("Bâtiment supprimé")
            
            
    def dessiner(self):
        pyxel.cls(7) # Pour l'instant fond blanc, on verra par la suite
        self.dessiner_carte()
        self.dessiner_menu()
        self.dessiner_hud()
        self.dessiner_notifications()
        self.dessiner_mode
        
        
    def dessiner_carte(self):
        # Enumerate permet ici d'avoir des indices y et x utiles pour calculer par la suite la position en pixels
        for y, ligne in enumerate(self.carte.grille):
            for x, case in enumerate(ligne):
                couleur = 0: # Pour l'instant noir
                pyxel.rectb(x*TAILLE_CASE, y*TAILLE_CASE, TAILLE_CASE, TAILLE_CASE, couleur) # Dessine le contour de chaque case 
                if case["batiment"];
                pyxel.rect(x*TAILLE_CASE+2, y*TAILLE_CASE+2, TAILLE_CASE-4, TAILLE_CASE-4,12) # Pour l'instant, puisqu'on a pas de sprite, chaque bâtiment sera représentée par une case bleue sur la carte
                
    

