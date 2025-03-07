import pygame  # Importujemy pygame
from constants import *  # Importujemy stałe
def main():
    pygame.init()  # Inicjalizujemy pygame

    # Tworzymy okno gry o rozmiarze określonym w constants.py
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # Obiekt do kontroli FPS
    dt = 0  # Delta time

    # Pętla gry
    while True:
        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Zamknięcie gry

       	screen.fill("black")  # Czyszczenie ekranu
        pygame.display.flip()  # Aktualizacja ekranu

        dt = clock.tick(60) / 1000  # Ograniczenie do 60 FPS + obliczenie delta time

if __name__ == "__main__":
    main()
