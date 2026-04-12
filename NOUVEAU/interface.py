import pygame
from carte import *
from batiment import *
from indicateurs import *
from events import *


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
# 
#         # Après avoir crée le dico batiment avec les images
        self.images_batiments = {}
#         
        # Je donne un exemple pour la suite (c'est répétitif pour chaque doc, on attend la création du dico des batiments pour avancer)
#         self.images_batiments["Maison"] = pygame.image.load("../graphisme/sprites/batiments/maison.png").convert_alpha()
#         self.images_batiments["Maison"] = pygame.transform.scale(self.images_batiments["Maison"], (50*2,50*2))
#         
#         self.images_batiments["Immeuble"] = pygame.image.load("../graphisme/sprites/batiments/immeuble.png").convert_alpha()
#         self.images_batiments["Immeuble"] = pygame.transform.scale(self.images_batiments["Immeuble"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Villa"] = pygame.image.load("../graphisme/sprites/batiments/villa.png").convert_alpha()
#         self.images_batiments["Villa"] = pygame.transform.scale(self.images_batiments["Villa"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Résidence sociale"] = pygame.image.load("../graphisme/sprites/batiments/residence_sociale.png").convert_alpha()
#         self.images_batiments["Résidence sociale"] = pygame.transform.scale(self.images_batiments["Résidence sociale"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Usine"] = pygame.image.load("../graphisme/sprites/batiments/usine.png").convert_alpha()
#         self.images_batiments["Usine"] = pygame.transform.scale(self.images_batiments["Usine"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Ferme"] = pygame.image.load("../graphisme/sprites/batiments/ferme.png").convert_alpha()
#         self.images_batiments["Ferme"] = pygame.transform.scale(self.images_batiments["Ferme"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Magasin"] = pygame.image.load("../graphisme/sprites/batiments/magasin.png").convert_alpha()
#         self.images_batiments["Magasin"] = pygame.transform.scale(self.images_batiments["Magasin"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Supermarché"] = pygame.image.load("../graphisme/sprites/batiments/supermarché.png").convert_alpha()
#         self.images_batiments["Supermarché"] = pygame.transform.scale(self.images_batiments["Supermarché"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Magasin bio"] = pygame.image.load("../graphisme/sprites/batiments/magasin_bio.png").convert_alpha()
#         self.images_batiments["Magasin bio"] = pygame.transform.scale(self.images_batiments["Magasin bio"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Banque"] = pygame.image.load("../graphisme/sprites/batiments/banque.png").convert_alpha()
#         self.images_batiments["Banque"] = pygame.transform.scale(self.images_batiments["Banque"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Bureaux"] = pygame.image.load("../graphisme/sprites/batiments/bureaux.png").convert_alpha()
#         self.images_batiments["Bureaux"] = pygame.transform.scale(self.images_batiments["Bureaux"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Marché local"] = pygame.image.load("../graphisme/sprites/batiments/marché_local.png").convert_alpha()
#         self.images_batiments["Marché local"] = pygame.transform.scale(self.images_batiments["Marché local"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Port marchand"] = pygame.image.load("../graphisme/sprites/batiments/port_marchand.png").convert_alpha()
#         self.images_batiments["Port marchand"] = pygame.transform.scale(self.images_batiments["Port marchand"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Parc"] = pygame.image.load("../graphisme/sprites/batiments/parc.png").convert_alpha()
#         self.images_batiments["Parc"] = pygame.transform.scale(self.images_batiments["Parc"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Forêt"] = pygame.image.load("../graphisme/sprites/batiments/forêt.png").convert_alpha()
#         self.images_batiments["Forêt"] = pygame.transform.scale(self.images_batiments["Forêt"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Plage"] = pygame.image.load("../graphisme/sprites/batiments/plage.png").convert_alpha()
#         self.images_batiments["Plage"] = pygame.transform.scale(self.images_batiments["Plage"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Éolienne"] = pygame.image.load("../graphisme/sprites/batiments/eolienne.png").convert_alpha()
#         self.images_batiments["Éolienne"] = pygame.transform.scale(self.images_batiments["Éolienne"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Mairie"] = pygame.image.load("../graphisme/sprites/batiments/mairie.png").convert_alpha()
#         self.images_batiments["Mairie"] = pygame.transform.scale(self.images_batiments["Mairie"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Route"] = pygame.image.load("../graphisme/sprites/batiments/route.png").convert_alpha()
#         self.images_batiments["Route"] = pygame.transform.scale(self.images_batiments["Route"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Commissariat"] = pygame.image.load("../graphisme/sprites/batiments/commissariat.png").convert_alpha()
#         self.images_batiments["Commissariat"] = pygame.transform.scale(self.images_batiments["Commissariat"], (50*1.5,50*1.5))
#         
#         #self.images_batiments["Caserne de pompiers"] = pygame.image.load("../graphisme/sprites/batiments/caserne_de_pompiers.png").convert_alpha()
#         #self.images_batiments["Caserne de pompiers"] = pygame.transform.scale(self.images_batiments["Caserne de pompiers"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Hôpital"] = pygame.image.load("../graphisme/sprites/batiments/hôpital.png").convert_alpha()
#         self.images_batiments["Hôpital"] = pygame.transform.scale(self.images_batiments["Hôpital"], (50*1.5,50*1.5))
#         
#         self.images_batiments["Prison"] = pygame.image.load("../graphisme/sprites/batiments/prison.png").convert_alpha()
#         self.images_batiments["Prison"] = pygame.transform.scale(self.images_batiments["Prison"], (50*1.5,50*1.5))
        # convert_alpha() est une fonction de pygame permettant d'optimiser l'image pour que la transparence soit gérée plus rapidement (car les dossiers en .png choisis auront une partie transparente)
        # transform.scale() est aussi une fonction de pygame permettant de redimensionner les images par rapport à la taille des cases (car images générées par IA et ne respectant pas forcément la taille des cases)
        
        # Redimensionnement pour rentrer dans le menu
        self.img_boutique = pygame.transform.scale(self.img_boutique, (160, 47))
        self.img_info = pygame.transform.scale(self.img_info, (160, 55))
        self.img_poubelle = pygame.transform.scale(self.img_poubelle, (160, 55))

        # Rectangles des boutons (pour les clics)
        self.rect_boutique = pygame.Rect(0, 0, 160, 40)
        self.rect_info = pygame.Rect(0, 0, 160, 40)
        self.rect_poubelle = pygame.Rect(0, 0, 160, 40)
        self.rect_categories = []
        self.rect_fermer = pygame.Rect(0, 0, 30, 30)
        self.rect_retour = pygame.Rect(0, 0, 40, 30)
        self.rect_supprimer_mode = pygame.Rect(0, 0, 160, 40)
        
        # Initialisation des éléments du jeu
        self.carte = Carte()
        self.jeu = Jeu()
        self.indicateurs = Indicateurs()

        # Gestion de la boutique
        self.boutique_ouverte = False
        self.categorie_boutique = "Habitation"
        self.dict_batiments = DictBatiments
        self.categories = list(self.dict_batiments.keys())
        self.rect_categories = []
        # Gestion des interactions souris / joueur
        self.case_souris = None
        self.case_selectionnee = None
        self.batiment_selectionne = None

        # Mode courant : placer / supprimer / info
        self.mode = "placer"

        # Messages affichés à l'écran
        self.messages = []

        self.running = True
        
        self.event_manager = Event() # evenements aléatoires
    
        # Ajout d'un système de "tick"
        self.compteur_tick = 0
        self.frequence_tick = 120 # En gros on se base sur les FPS, ici 60 FPS * 2 secondes = 120 frames
        
        self.categories = list(self.dict_batiments.keys())
        self.categorie_boutique = self.categories[0]
        
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
    
        # On gère ici le timer, sous forme de "tick"
        self.compteur_tick += 1
        if self.compteur_tick >= self.frequence_tick:
            self.jeu.actualiser_economie(self.indicateurs)
            self.jeu.calculer_population(self.indicateurs)
            self.jeu.verifier_niveau(self.indicateurs)
            message_event = self.event_manager.generer_evenement(self.indicateurs)
            self.compteur_tick = 0
            if message_event:
                self.ajouter_message(message_event)
            else:
                self.ajouter_message(f"Niveau {self.jeu.niveau} / Pop : {self.indicateurs.valeurs['population']}")
            

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
                self.batiment_selectionne = None
            else:
                self.ajouter_message("Pas assez d'argent")

        elif self.mode == "supprimer":
            if self.carte.verifier_case_libre(x, y):
                self.ajouter_message("Aucun bâtiment ici")
            else:
                self.carte.supprimer_batiment(x, y)
                self.ajouter_message("Bâtiment supprimé")
            self.mode = None

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
                    nom = case["batiment"].nom
                    if nom in self.images_batiments:
                        img = self.images_batiments[nom]
                        self.screen.blit(
                            img,
                            (
                                px - (img.get_width() - TAILLE_CASE)//2,
                                py - (img.get_height() - TAILLE_CASE)//2
                            )
                        )
                    else:
                        # En attendant que les images soient crées car pas pour l'instant, on fait en sorte de créer un "carré de secours" pour pas faire crash le jeu)
                        pygame.draw.rect(self.screen, (0, 120, 255), (px+2, py+2, TAILLE_CASE-4, TAILLE_CASE-4))








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

        # CENTRAGE DES IMAGES
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

    # boutique

    def dessiner_boutique(self):
        # Fenêtre boutique
        popup = pygame.Rect(100, 80, 800, 600)
        pygame.draw.rect(self.screen, (230, 230, 230), popup)
        pygame.draw.rect(self.screen, (0, 0, 0), popup, 2)

        titre = self.font.render("Boutique", True, (0, 0, 0))
        self.screen.blit(titre, (popup.x + 20, popup.y + 10))

        # bouton croix pr fermer
        self.rect_fermer.topleft = (popup.right - 40, popup.y + 10)
        pygame.draw.rect(self.screen, (200, 50, 50), self.rect_fermer)
        x_txt = self.font.render("X", True, (255, 255, 255))
        self.screen.blit(x_txt, (self.rect_fermer.x + 8, self.rect_fermer.y + 5))

        # bouton retour
        self.rect_retour.topleft = (popup.x + 20, popup.y + 50)
        pygame.draw.rect(self.screen, (100, 100, 100), self.rect_retour)
        retour_txt = self.font.render("<-", True, (255, 255, 255))
        self.screen.blit(retour_txt, (self.rect_retour.x + 10, self.rect_retour.y + 5))

        # bouton des categories
        self.rect_categories = []
        x_cat = popup.x + 20
        y_cat = popup.y + 100

        for categorie in self.categories:
            rect = pygame.Rect(x_cat, y_cat, 150, 30)
            self.rect_categories.append((rect, categorie))

            couleur = (150, 200, 255) if categorie == self.categorie_boutique else (200, 200, 200)

            pygame.draw.rect(self.screen, couleur, rect)
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

            texte = self.font.render(categorie, True, (0, 0, 0))
            self.screen.blit(texte, (rect.x + 5, rect.y + 5))

            y_cat += 40

        # les categories
        x_bat = popup.x + 200
        y_bat = popup.y + 100

        for batiment in self.dict_batiments[self.categorie_boutique].values():
            rect = pygame.Rect(x_bat, y_bat, 450, 40)

            pygame.draw.rect(self.screen, (100, 150, 255), rect)
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)
            
            if batiment.nom in self.images_batiments:
                img = self.images_batiments[batiment.nom]

                # redimensionnement des sprites
                img_small = pygame.transform.scale(img, (40, 40))

                self.screen.blit(img_small, (rect.x + 5, rect.y + 5))

            texte = self.font.render(
                f"{batiment.nom} | Coût : {batiment.cout} | Niv : {batiment.niveau_requis}",
                True, (0, 0, 0)
            )
            self.screen.blit(texte, (rect.x + 45, rect.y + 10))

            y_bat += 50
    
    def cliquer_boutique(self, x, y):
        # la croix
        if self.rect_fermer.collidepoint(x, y):
            self.boutique_ouverte = False
            return

        # la fleche du retour
        if self.rect_retour.collidepoint(x, y):
            self.ajouter_message("Retour")
            # Exemple : revenir à une catégorie par défaut
            self.categorie_boutique = self.categories[0]
            return

        # les categories des batiments
        for rect, categorie in self.rect_categories:
            if rect.collidepoint(x, y):
                self.categorie_boutique = categorie
                self.ajouter_message(f"Catégorie : {categorie}")
                return

        # la selection des bat
        popup = pygame.Rect(100, 80, 800, 600)

        x_bat = popup.x + 200
        y_bat = popup.y + 100

            
        for batiment in self.dict_batiments[self.categorie_boutique].values():
            rect = pygame.Rect(x_bat, y_bat, 550, 40)

            if rect.collidepoint(x, y):

                #verification du niveau requi pr le bat selectionné
                if self.jeu.niveau < batiment.niveau_requis:
                    self.ajouter_message("Niveau insuffisant")
                    return

                
                self.batiment_selectionne = batiment
                self.boutique_ouverte = False
                self.mode = "placer"
                self.ajouter_message(f"{batiment.nom} sélectionné")
                return

            y_bat += 50



    # CLICS MENU
    
    def cliquer_bouton(self, souris_x, souris_y):
        if self.rect_boutique.collidepoint(souris_x, souris_y):
            self.boutique_ouverte = not self.boutique_ouverte

        elif self.rect_info.collidepoint(souris_x, souris_y):
            self.mode = "info"

        elif self.rect_poubelle.collidepoint(souris_x, souris_y):
            self.mode = "supprimer"
        elif self.rect_supprimer_mode.collidepoint(souris_x, souris_y):
            self.mode = "supprimer"
            self.ajouter_message("Mode : Supprimer")
    # Clic sur les catégories des batiments
        for rect, categorie in self.rect_categories:
            if rect.collidepoint(souris_x, souris_y):
                self.categorie_boutique = categorie
                self.ajouter_message(f"Catégorie : {categorie}")
                return
