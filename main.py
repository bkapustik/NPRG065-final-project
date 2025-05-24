import pygame
import sys
from game_menu import GameMenu

if __name__ == "__main__":
    pygame.init()

    screenWidth = 1300
    screenHeight = 800
    screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
    gameMenu = GameMenu(screen)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.VIDEORESIZE:
                screenWidth, screenHeight = event.w, event.h
                gameMenu.setScreenSize(screenWidth, screenHeight)

        screen.fill((255, 255, 255))
        screen.blit(gameMenu.background, (0, 0))
        gameMenu.render()
        gameMenu.reactToClicks(events)
        pygame.display.flip()