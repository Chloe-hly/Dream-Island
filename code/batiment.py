class Ville:
    def __init__(self):
        self.argent = 10000
        self.pollution = 0
        self.biodiversite = 50
        self.bonheur = 50
        self.population = 0
        self.niveau = 1


class Batiment:
    def __init__(self, nom, categorie, cout, effet_argent, effet_pollution,
                 effet_biodiversite, effet_bonheur, effet_population, niveau_requis):
        """
        Constructeur de la classe Batiment.
        Chaque bâtiment a des effets sur la ville.
        """
        self.nom = nom
        self.categorie = categorie
        self.cout = cout

        # Effets
        self.effet_argent = effet_argent
        self.effet_pollution = effet_pollution
        self.effet_biodiversite = effet_biodiversite
        self.effet_bonheur = effet_bonheur
        self.effet_population = effet_population

        self.niveau_requis = niveau_requis


class Jeu:
    def __init__(self):
        self.ville = Ville()
        self.batiments_places = []   # Liste : (batiment, position)
        self.niveau = 1
        
    def placer_batiment(self, batiment, position):
        """Ajoute le bâtiment sur la carte."""
        self.batiments_places.append((batiment, position))

    def acheter_batiment(self, batiment, position, indicateurs):
        # Vérification de l'argent
        if indicateurs.valeurs["argent"] < batiment.cout:
            print("Pas assez d'argent")
            return False

        # Vérification du niveau
        if self.ville.niveau < batiment.niveau_requis:
            print(f"Niveau {batiment.niveau_requis} requis pour construire {batiment.nom}")
            return False

        # Paiement
        indicateurs.modifier("argent", -batiment.cout)

        # Application des effets
        indicateurs.modifier("argent", batiment.effet_argent)
        indicateurs.modifier("bonheur", batiment.effet_bonheur)
        indicateurs.modifier("population", batiment.effet_population)

        # Placement
        self.placer_batiment(batiment, position)

        print(f"{batiment.nom} construit")
        return True

DictBatiments = {
    "Habitation": {
        "Maison":Batiment("Maison", "Habitation", 500, +1, +1, -1, +2, +10, 1),
        "Immeuble":Batiment("Immeuble", "Habitation", 1500, +2, +4, -3, 0, +30, 3),
        "Villa":Batiment("Villa", "Habitation", 2200, +2, +2, -1, +5, +12, 4),
        "Residence_sociale":Batiment("Résidence sociale", "Habitation", 900, +1, +3, -1, -2, +25, 2),
    },
    "Travail": {
        "Usine":Batiment("Usine", "Économie", 1400, +8, +8, -4, -3, +8, 3),
        "Ferme":Batiment("Ferme", "Économie", 800, +3, +2, -2, +2, +6, 2),
        "Magasin":Batiment("Magasin", "Économie", 600, +3, +2, 0, +1, +5, 1),
        "Supermarché": Batiment("Supermarché", "Économie", 1000, +5, +3, -1, +1, +10, 2),
        "Magasin_bio": Batiment("Magasin bio", "Économie", 850, +3, 0, +3, +3, +6, 3),
        "Banque": Batiment("Banque", "Économie", 1600, +6, +1, 0, -2, +3, 4),
        "Bureaux":Batiment("Bureaux", "Économie", 1100, +5, +3, -1, +1, +10, 3),
        "Marché_local": Batiment("Marché local", "Économie", 700, +2, 0, +2, +4, +5, 2),
        "Port_marchand": Batiment("Port marchand", "Économie", 2200, +10, +7, -3, 0, +15, 5)
    },
    "Environnement": {
        "Parc": Batiment("Parc", "Environnement", 700, 0, -3, +4, +5, 0, 2),
        "Forêt": Batiment("Forêt", "Environnement", 1000, 0, -5, +6, +2, 0, 3),
        "Plage": Batiment("Plage", "Environnement", 1300, +1, 0, +3, +6, +2, 4),
        "Éolienne": Batiment("Éolienne", "Environnement", 900, +2, -2, +1, +2, 0, 3),
    },
    "sevices_publique": {
        "Mairie": Batiment("Mairie", "Services publics", 2200, +3, 0, 0, +6, +3, 4),
        "Commissariat":Batiment("Commissariat", "Services publics", 1200, 0, +1, 0, +3, +3, 3),
        "Caserne_de_pompiers": Batiment("Caserne de pompiers", "Services publics", 1400, 0, 0, 0, +4, +3, 3),
        "Hôpital": Batiment("Hôpital", "Services publics", 2000, 0, +2, 0, +7, +10, 5),
        "Prison": Batiment("Prison", "Services publics", 1500, 0, +3, -1, -3, 0, 4),
        "Tribunal": Batiment("Tribunal", "Services publics", 1000, +1, 0, 0, +3, 0, 3),   
    },
    "transports":{
        "Route": Batiment("Route", "Transports", 400, +1, +3, -1, 0, 0, 1),
        "Tramway": Batiment("Tramway", "Transports", 1300, +3, -2, 0, +3, +5, 3),
        "Métro": Batiment("Métro", "Transports", 2200, +5, -3, 0, +4, +10, 4),
        "Piste_cyclable": Batiment("Piste cyclable", "Transports", 600, 0, -2, 0, +4, 0, 2),
        "Port": Batiment("Port", "Transports", 2500, +8, +6, -3, +1, +12, 5),
        "Aéroport": Batiment("Aéroport", "Transports", 3200, +12, +10, -5, +2, +20, 6),
        
        },
    "culture":{
        "Monument": Batiment("Monument", "Culture & spéciaux", 2200, +4, 0, 0, +10, 0, 5),
        "Centre_culturel": Batiment("Centre culturel", "Culture & spéciaux", 1600, +2, +1, 0, +6, +5, 4),
        "Stade": Batiment("Stade", "Culture & spéciaux", 2500, +6, +4, -2, +8, +10, 5),
        "Centre_commercial": Batiment("Centre commercial", "Culture & spéciaux", 2000, +8, +5, -2, +3, +10, 5),
        "Festival_local": Batiment("Festival local", "Culture & spéciaux", 500, +3, +2, -1, +8, +5, 0),
        }
    
}
