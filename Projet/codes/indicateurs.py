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
        
        
        self.variation = { # pour stocker les évolutions prevues avant de les appliquer
            "argent": 0,
            "bonheur": 0,
            "population": 0,
            "energie": 0,
            "nourriture": 0,
            "eau": 0,
        }

    def appliquer_variation(self) :
        for cle in self.valeurs :
            self.valeurs[cle] +=self.variation[cle]

    def modifier(self, cle, valeur):
        if cle in self.valeurs:
            self.valeurs[cle] += valeur

    def qualite_de_vie(self):
        return int((
            self.valeurs["bonheur"]+
            self.valeurs["energie"]
        )/2)

    def satisfaction(self) :
        population = self.valeurs["population"]
        if population == 0:
            return 0
        ressources = (
            self.valeurs["nourriture"] +
            self.valeurs["eau"]
        )/2
        return int(min(100,(ressources/population)*50+self.valeurs["bonheur"] / 2))

    def mise_a_jour(self):
        if self.valeurs["nourriture"] < self.valeurs["population"]:
            self.valeurs["bonheur"]-=1

        if self.valeurs["eau"] < self.valeurs["population"]:
            self.valeurs["bonheur"]-=1

        if self.valeurs["energie"]<=0:
            self.valeurs["bonheur"]-=2

        self.borner_valeurs()

    def borner_valeurs(self):
        for cle in self.valeurs:
            self.valeurs[cle] = max(0, self.valeurs[cle])

    def __str__(self):
        return str(self.valeurs)

