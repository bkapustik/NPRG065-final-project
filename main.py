import pygame
import sys
from game_menu import GameMenu

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    gameMenu = GameMenu(screen, screen.get_width(), screen.get_height())

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        screen.blit(gameMenu.background, (0, 0))
        gameMenu.render()
        gameMenu.reactToClicks(events)
        pygame.display.flip()