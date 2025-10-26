# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 13:59:30 2025

@author: maelysadoir
"""

class Building:
    def __init__(self, nom, categorie, cout, effet_argent, effet_pollution,
                 effet_biodiversite, effet_bonheur, effet_population,):
        """
        Constructeur de la classe Building.
        Chaque bâtiment a des effets sur la ville et certaines contraintes."""
        self.nom = nom
        self.categorie = categorie
        self.cout = cout
        self.effet_pollution = effet_pollution
        self.effet_biodiversite = effet_biodiversite
        self.effet_bonheur = effet_bonheur
        self.effet_population = effet_population
        
        

    def appliquer_effets(self, ville):
        ville.argent += self.effet_argent
        ville.pollution += self.effet_pollution
        ville.biodiversite += self.effet_biodiversite
        ville.bonheur += self.effet_bonheur
        ville.population += self.effet_population
        
        

tous_les_batiments = [

    #habitations
    Building("Maison", "Habitation", 500, 1, 1, -1, 2, 10, 1),
    Building("Immeuble", "Habitation", 1500, 2, 4, -3, 0, 30, 3),
    Building("Villa", "Habitation", 2200, 2, 2, -1, 5, 12, 4),
    Building("Résidence sociale", "Habitation", 900, 1, 3, -1, -2, 25, 2),
    Building("Bidonville", "Habitation", 0, 0, 6, -4, -5, 20, 0),

    #economie
    Building("Usine", "Économie", 1400, 8, 8, -4, -3, 8, 3),
    Building("Ferme", "Économie", 800, 3, 2, -2, 2, 6, 2),
    Building("Magasin", "Économie", 600, 3, 2, 0, 1, 5, 1),
    Building("Supermarché", "Économie", 1000, 5, 3, -1, 1, 10, 2),
    Building("Magasin bio", "Économie", 850, 3, 0, 3, 3, 6, 3),
    Building("Banque", "Économie", 1600, 6, 1, 0, -2, 3, 4),
    Building("Bureaux", "Économie", 1100, 5, 3, -1, 1, 10, 3),
    Building("Marché local", "Économie", 700, 2, 0, 2, 4, 5, 2),
    Building("Port marchand", "Économie", 2200, 10, 7, -3, 0, 15, 5),

    #éducation
    Building("Crèche", "Éducation", 600, 0, 1, 0, 3, 5, 1),
    Building("École primaire", "Éducation", 800, 1, 1, 0, 4, 6, 2),
    Building("Collège", "Éducation", 1000, 2, 2, 0, 4, 8, 3),
    Building("Lycée", "Éducation", 1300, 3, 2, 0, 5, 10, 4),
    Building("Université", "Éducation", 2000, 5, 3, 0, 7, 12, 5),

    #environnement
    Building("Parc", "Environnement", 700, 0, -3, 4, 5, 0, 2),
    Building("Forêt", "Environnement", 1000, 0, -5, 6, 2, 0, 3),
    Building("Plage", "Environnement", 1300, 1, 0, 3, 6, 2, 4),
    Building("Éolienne", "Environnement", 900, 2, -2, 1, 2, 0, 3),
    Building("Décharge", "Environnement", 800, 0, 5, -4, -3, 0, 0),

    #les services publics
    Building("Mairie", "Services publics", 2200, 3, 0, 0, 6, 3, 4),
    Building("Commissariat", "Services publics", 1200, 0, 1, 0, 3, 3, 3),
    Building("Caserne de pompiers", "Services publics", 1400, 0, 0, 0, 4, 3, 3),
    Building("Hôpital", "Services publics", 2000, 0, 2, 0, 7, 10, 5),
    Building("Prison", "Services publics", 1500, 0, 3, -1, -3, 0, 4),
    Building("Tribunal", "Services publics", 1000, 1, 0, 0, 3, 0, 3),

    #les transports
    Building("Route", "Transports", 400, 1, 3, -1, 0, 0, 1),
    Building("Tramway", "Transports", 1300, 3, -2, 0, 3, 5, 3),
    Building("Métro", "Transports", 2200, 5, -3, 0, 4, 10, 4),
    Building("Piste cyclable", "Transports", 600, 0, -2, 0, 4, 0, 2),
    Building("Port", "Transports", 2500, 8, 6, -3, 1, 12, 5),
    Building("Aéroport", "Transports", 3200, 12, 10, -5, 2, 20, 6),

    #culture...
    Building("Monument", "Culture & spéciaux", 2200, 4, 0, 0, 10, 0, 5),
    Building("Centre culturel", "Culture & spéciaux", 1600, 2, 1, 0, 6, 5, 4),
    Building("Stade", "Culture & spéciaux", 2500, 6, 4, -2, 8, 10, 5),
    Building("Centre commercial", "Culture & spéciaux", 2000, 8, 5, -2, 3, 10, 5),
    Building("Festival local", "Culture & spéciaux", 500, 3, 2, -1, 8, 5, 0),
]