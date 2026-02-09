import pygame
from carte import *
from batiment import *
from indicateurs import *



# AFFICHAGE

TAILLE_CASE = 50
LARGEUR_MENU = 200      # panneau de droite
HAUTEUR_HUD = 80        # bande du bas (indicateurs)

TITLE = "Dream Island"


class Interface:
    def __init__(self):
        # Initialisation de pygame
        pygame.init()

        # Récupération de la taille réelle de l'écran
        info = pygame.display.Info()
        self.largeur_fenetre = info.current_w
        self.hauteur_fenetre = info.current_h

        # Création d'une grande fenêtre 
        self.screen = pygame.display.set_mode(
            (self.largeur_fenetre, self.hauteur_fenetre),
            pygame.RESIZABLE
        )

        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 16)
        
        # Chargement des images des boutons
        self.img_boutique = pygame.image.load("../graphisme/sprites/interface/bouton_boutique.png").convert_alpha()
        self.img_info = pygame.image.load("../graphisme/sprites/interface/bouton_info.png").convert_alpha()
        self.img_poubelle = pygame.image.load("../graphisme/sprites/interface/bouton_poubelle.png").convert_alpha()

        # Redimensionnement pour rentrer dans le menu
        self.img_boutique = pygame.transform.scale(self.img_boutique, (160, 40))
        self.img_info = pygame.transform.scale(self.img_info, (160, 40))
        self.img_poubelle = pygame.transform.scale(self.img_poubelle, (160, 40))

        # Rectangles des boutons (pour les clics)
        self.rect_boutique = pygame.Rect(0, 0, 160, 40)
        self.rect_info = pygame.Rect(0, 0, 160, 40)
        self.rect_poubelle = pygame.Rect(0, 0, 160, 40)


        # Initialisation des éléments du jeu
        self.carte = Carte()
        self.jeu = Jeu()
        self.indicateurs = Indicateurs()

        # Gestion de la boutique
        self.boutique_ouverte = False
        self.categorie_boutique = "Habitation"
        self.dict_batiments = DictBatiments

        # Gestion des interactions souris / joueur
        self.case_souris = None
        self.case_selectionnee = None
        self.batiment_selectionne = None

        # Mode courant : placer / supprimer / info
        self.mode = "placer"

        # Messages affichés à l'écran
        self.messages = []

        self.running = True

    def ajouter_message(self, texte):
        # On garde uniquement le dernier message
        self.messages = [texte]

    def case_valide(self, x, y):
        # Vérifie si la case est bien dans la grille
        return (
            0 <= y < len(self.carte.grille)
            and 0 <= x < len(self.carte.grille[0])
        )


    # BOUCLE DE MISE A JOUR

    def mettre_a_jour(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Gestion du clavier
            if event.type == pygame.KEYDOWN:
                # Quitter le jeu avec Echap
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                elif event.key == pygame.K_p:
                    self.mode = "placer"
                    self.ajouter_message("Mode : Placer")

                elif event.key == pygame.K_s:
                    self.mode = "supprimer"
                    self.ajouter_message("Mode : Supprimer")

                elif event.key == pygame.K_i:
                    self.mode = "info"
                    self.ajouter_message("Mode : Info")

            # Gestion du clic gauche
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                souris_x, souris_y = pygame.mouse.get_pos()

                # Si la boutique est ouverte, on clique dedans
                if self.boutique_ouverte:
                    self.cliquer_boutique(souris_x, souris_y)
                    return

                # Si on clique dans le menu de droite
                if souris_x >= self.largeur_fenetre - LARGEUR_MENU:
                    self.cliquer_bouton(souris_x, souris_y)
                else:
                    # Sinon on clique sur la carte
                    case_x = souris_x // TAILLE_CASE
                    case_y = souris_y // TAILLE_CASE

                    if self.case_valide(case_x, case_y):
                        self.case_selectionnee = (case_x, case_y)
                        self.action_case(case_x, case_y)

        # Mise à jour de la case sous la souris
        souris_x, souris_y = pygame.mouse.get_pos()
        self.case_souris = (souris_x // TAILLE_CASE, souris_y // TAILLE_CASE)


    # ACTIONS SUR LA CARTE

    def action_case(self, x, y):
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
            if self.jeu.acheter_batiment(batiment, (x, y), self.indicateurs):
                self.carte.placer_batiment(batiment, x, y)
                self.ajouter_message(f"{batiment.nom} construit")
            else:
                self.ajouter_message("Pas assez d'argent")

        elif self.mode == "supprimer":
            if self.carte.verifier_case_libre(x, y):
                self.ajouter_message("Aucun bâtiment ici")
            else:
                self.carte.supprimer_batiment(x, y)
                self.ajouter_message("Bâtiment supprimé")

        elif self.mode == "info":
            batiment = self.carte.voir_batiment(x, y)
            if batiment:
                texte = (
                    f"{batiment.nom} | "
                    f"Argent:{batiment.effet_argent} "
                    f"Pollution:{batiment.effet_pollution} "
                    f"Biodiv:{batiment.effet_biodiversite} "
                    f"Bonheur:{batiment.effet_bonheur} "
                    f"Pop:{batiment.effet_population}"
                )
                self.ajouter_message(texte)
            else:
                self.ajouter_message("Aucun bâtiment ici")

    # DESSIN DE L'INTERFACE

    def dessiner(self):
        # Fond blanc
        self.screen.fill((255, 255, 255))

        self.dessiner_carte()
        self.dessiner_menu()
        self.dessiner_hud()
        self.dessiner_notifications()

        if self.boutique_ouverte:
            self.dessiner_boutique()

        pygame.display.flip()

    def dessiner_carte(self):
        # Dessin de la grille de la carte
        for y, ligne in enumerate(self.carte.grille):
            for x, case in enumerate(ligne):
                px = x * TAILLE_CASE
                py = y * TAILLE_CASE

                # On évite de dessiner sous le HUD
                if py + TAILLE_CASE > self.hauteur_fenetre - HAUTEUR_HUD:
                    continue

                pygame.draw.rect(
                    self.screen, (0, 0, 0),
                    (px, py, TAILLE_CASE, TAILLE_CASE), 1
                )

                if case["batiment"]:
                    pygame.draw.rect(
                        self.screen, (0, 120, 255),
                        (px+2, py+2, TAILLE_CASE-4, TAILLE_CASE-4)
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
            pygame.draw.rect(
                self.screen, (255, 0, 0),
                (x*TAILLE_CASE, y*TAILLE_CASE, TAILLE_CASE, TAILLE_CASE), 2
            )

    def dessiner_menu(self):
        # Panneau de droite
        pygame.draw.rect(
            self.screen, (180, 180, 180),
            (self.largeur_fenetre - LARGEUR_MENU, 0, LARGEUR_MENU, self.hauteur_fenetre)
        )

        # Niveau
        texte_niveau = self.font.render(f"Niveau : {self.jeu.niveau}", True, (0, 0, 0))
        self.screen.blit(
            texte_niveau,
            (self.largeur_fenetre - LARGEUR_MENU + 20, 20)
        )

        # Position X commune
        x = self.largeur_fenetre - LARGEUR_MENU + 20

        # Position des boutons
        self.rect_boutique.topleft = (x, 70)
        self.rect_info.topleft = (x, 140)
        self.rect_poubelle.topleft = (x, 210)

        # FOND DES BOUTONS
        for rect in [self.rect_boutique, self.rect_info, self.rect_poubelle]:
            pygame.draw.rect(self.screen, (255, 255, 255), rect, border_radius=6)
            pygame.draw.rect(self.screen, (120, 120, 120), rect, 2, border_radius=6)

        #CENTRAGE DES IMAGES
        img_boutique_rect = self.img_boutique.get_rect(center=self.rect_boutique.center)
        img_info_rect = self.img_info.get_rect(center=self.rect_info.center)
        img_poubelle_rect = self.img_poubelle.get_rect(center=self.rect_poubelle.center)

        self.screen.blit(self.img_boutique, img_boutique_rect)
        self.screen.blit(self.img_info, img_info_rect)
        self.screen.blit(self.img_poubelle, img_poubelle_rect)


    def dessiner_hud(self):
        # Position verticale du HUD
        y = self.hauteur_fenetre - HAUTEUR_HUD
        largeur_hud = self.largeur_fenetre - LARGEUR_MENU

        # Fond du HUD
        pygame.draw.rect(
            self.screen,
            (220, 220, 220),
            (0, y, largeur_hud, HAUTEUR_HUD)
        )

        # Affichage des indicateurs
        nb_indicateurs = len(self.indicateurs.valeurs)
        espace = largeur_hud // nb_indicateurs

        x = 10
        for nom, valeur in self.indicateurs.valeurs.items():
            texte = self.font.render(f"{nom} : {valeur}", True, (0, 0, 0))
            self.screen.blit(texte, (x, y + 25))
            x += espace

    def dessiner_notifications(self):
        # Messages en bas à gauche
        for i, msg in enumerate(self.messages):
            texte = self.font.render(msg, True, (0, 0, 0))
            self.screen.blit(
                texte,
                (10, self.hauteur_fenetre - HAUTEUR_HUD - 25 + i * 20)
            )

    # BOUTIQUE

    def dessiner_boutique(self):
        pygame.draw.rect(self.screen, (230, 230, 230), (100, 80, 800, 600))
        pygame.draw.rect(self.screen, (0, 0, 0), (100, 80, 800, 600), 2)

        titre = self.font.render("Boutique", True, (0, 0, 0))
        self.screen.blit(titre, (460, 90))

        y = 150
        for batiment in self.dict_batiments[self.categorie_boutique].values():
            rect = pygame.Rect(150, y, 600, 35)
            pygame.draw.rect(self.screen, (100, 150, 255), rect)
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

            texte = self.font.render(
                f"{batiment.nom} | Coût : {batiment.cout}",
                True, (0, 0, 0)
            )
            self.screen.blit(texte, (160, y + 8))
            y += 45

    def cliquer_boutique(self, x, y):
        y_pos = 150
        for batiment in self.dict_batiments[self.categorie_boutique].values():
            rect = pygame.Rect(150, y_pos, 600, 35)
            if rect.collidepoint(x, y):
                self.batiment_selectionne = batiment
                self.mode = "placer"
                self.boutique_ouverte = False
                self.ajouter_message(f"{batiment.nom} sélectionné")
                return
            y_pos += 45


    # CLICS MENU
    
    def cliquer_bouton(self, souris_x, souris_y):
        if self.rect_boutique.collidepoint(souris_x, souris_y):
            self.boutique_ouverte = not self.boutique_ouverte

        elif self.rect_info.collidepoint(souris_x, souris_y):
            self.mode = "info"

        elif self.rect_poubelle.collidepoint(souris_x, souris_y):
            self.mode = "supprimer"

