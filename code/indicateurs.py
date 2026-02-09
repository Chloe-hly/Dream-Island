class Indicateurs:
    def __init__(self):
        self.valeurs = {
            "argent": 10000,
            "pollution": 0,
            "biodiversite": 50,
            "bonheur": 50,
            "population": 0
        }

    def modifier(self, cle, valeur):
        if cle in self.valeurs:
            self.valeurs[cle] += valeur

    def __str__(self):
        return str(self.valeurs)

