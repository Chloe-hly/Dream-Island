import random

EVENEMENTS = [
    {
        "nom": "Canicule",
        "type": "negatif",
        "message": "Canicule ! La chaleur fait baisser le bonheur.",
        "effets": {"bonheur": -5, "pollution": +3}
    },
    {
        "nom": "Festival",
        "type": "positif",
        "message": "Un festival local booste le bonheur !",
        "effets": {"bonheur": +8, "argent": +500}
    },
    {
        "nom": "Tempête",
        "type": "negatif",
        "message": "Tempête ! Des dégâts sur l'île.",
        "effets": {"bonheur": -4, "argent": -300}
    },
    {
        "nom": "Touristes",
        "type": "positif",
        "message": "Arrivée de touristes ! L'économie se porte mieux.",
        "effets": {"argent": +800, "bonheur": +3}
    },
    {
        "nom": "Épidémie",
        "type": "negatif",
        "message": "Épidémie ! La population est touchée.",
        "effets": {"bonheur": -6, "population": -5}
    },
    {
        "nom": "Subvention",
        "type": "positif",
        "message": "Subvention gouvernementale reçue !",
        "effets": {"argent": +1000}
    },
]

class Event:
    def __init__(self):
        self.evenement_actif = None
        self.duree_restante = 0

    def generer_evenement(self, indicateurs):
        """1 chance sur 100 de déclencher un événement à chaque appel."""
        if self.duree_restante > 0:
            self.duree_restante -= 1
            return None

        if random.randint(1, 100) == 1:
            evenement = random.choice(EVENEMENTS)
            self.evenement_actif = evenement
            self.duree_restante = 5  # dure 5 ticks

            for cle, valeur in evenement["effets"].items():
                indicateurs.modifier(cle, valeur)

            return evenement["message"]

        return None