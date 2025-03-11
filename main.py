import pygame  # Importujemy pygame
from constants import *  # Importujemy stałe
from player import Player

def main():
    pygame.init()  # Inicjalizujemy pygame

    # Tworzymy okno gry o rozmiarze określonym w constants.py
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # Obiekt do kontroli FPS
    dt = 0  # Delta time

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Pętla gry
    while True:
        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Zamknięcie gry

       	screen.fill("black")  # Czyszczenie ekranu

        player.draw(screen)

        pygame.display.flip()  # Aktualizacja ekranu

        dt = clock.tick(60) / 1000  # Ograniczenie do 60 FPS + obliczenie delta time
        

    

if __name__ == "__main__":
    main()
