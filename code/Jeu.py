import pygame
from batiment import *
from indicateurs import *
from carte import *
from interface import *

def main():
    interface = Interface()

    while interface.running:
        interface.mettre_a_jour()
        interface.dessiner()
        interface.clock.tick(60)

    pygame.quit()



    pygame.quit()

if __name__ == "__main__":
    main()
