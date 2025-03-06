import pygame  # Importujemy pygame
from constants import *  # Importujemy stałe
def main():
    pygame.init()  # Inicjalizujemy pygame

    # Tworzymy okno gry o rozmiarze określonym w constants.py
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Pętla gry
    while True:
        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Zamknięcie gry

        # Wypełniamy ekran czarnym kolorem
        screen.fill((0, 0, 0))

        # Odświeżamy ekran
        pygame.display.flip()

if __name__ == "__main__":
    main()
