class Carte:
   
   def __init__(self):
       # On ne va pas placer en paramètre largeur, hauteur, taille_case car on va par défaut mettre la carte en 15*15 et une case mesure 50 pixels
       self.largeur = 15  # Le nombre de colonnes x
       self.hauteur = 15 # Le nombre de lignes y
       
       self.taille_case =  50 # La taille d'une case, ici en pixels
       
       # Création de la grille vide
       # Ici, chaque case est un dictionnaire qui contient les coordonnées et les bâtiments
       
       self.grille = []
       for y in range(self.hauteur):
           ligne = []
           for x in range(self.largeur):
               case = {"x" :x, "y" : y, "batiment" : None} # La case ne doit pas contenir de bâtiment : elle doit être vide
               ligne.append(case)
            self.grille.append(ligne)
            
    
    def verifier_case_libre(self, x, y):
        # Doit return True si la case est libre
        return self.grille[y][x]["batiment"] == None # Si la case ne contient pas de bâtiment, elle renvoie None (donc True), donc elle est vide
                                                     # Dans le cas contraire, si elle contient un bâtiment elle renvoie False
    
    def placer_batiment(self, batiment, x, y):
        # On peut placer un batiment si la case est vide
        if self.verifier_case_libre(x,y):
            self.grille[y][x]["batiment"] = batiment
            print(batiment.nom + " placé en (" + str(x) + "," + str(y) + ")")
        else :
            print("Case déjà occupée")
            
    def supprimer_batiment(self, x, y):
        # Supprime le bâtiment si la case est occupée
        if self.grille[y][x]["batiment"] != None:
            print(self.grille[y][x]["batiment"].nom + "est supprimé")
            self.grille[y][x]["batiment"] = None
            
    def voir_batiment(self, x, y):
        # Permet de voir, si le joueur clique sur une case, le nom du bâtiment, et renvoie None si la case ne contient rien
        return self.grille[y][x]["batiment"]
    
    def afficher_carte_console(s)
        # Permet d'afficher la carte dans la console pour voir rapidement ce qu'il y a sur la carte, permet de tester (plus partie en dev, pas partie finale)
        for ligne in self.grille:
            print(["X" if case ["batiment"] else "." for case in ligne])
            
        
                    