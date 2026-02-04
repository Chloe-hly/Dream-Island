''' indicateurs principaux :

argent

bonheur

population

energie

nourriture

eau'''

class Indicateurs:
    
    def __init__(self):
        
        self.valeurs = {
            "argent": 1000,
            "bonheur": 50,
            "population": 10,
            "energie": 20,
            "nourriture": 20,
            "eau": 20,
        }
        
        
        self.variation = {
            "argent": 0,
            "bonheur": 0,
            "population": 0,
            "energie": 0,
            "nourriture": 0,
            "eau": 0,
        }

    def appliquer_variation(self):
        for cle in self.valeurs:
            self.valeurs[cle] += self.variation[cle]

    def modifier(self, cle, valeur):
        if cle in self.valeurs:
            self.valeurs[cle] += valeur

    def __str__(self):
        return str(self.valeurs)
