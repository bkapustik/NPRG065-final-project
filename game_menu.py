import pygame
from menu_button import MenuButton
from enum import Enum

class GameState(Enum):
    INITIAL = 0
    PLAYING = 1
    PLAYER_WON = 2
    PLAYER_LOST = 3
    PAUSED = 4

class GameMenu:

    green = (0, 255, 0)
    black = (0, 0, 0)    

    screen: pygame.Surface
    background: pygame.Surface
    startTexture: pygame.Surface
    menuButton: MenuButton
    
    screenWidth: float
    screenHeight: float
    isHumanChoosingColor: bool = False
    gameState: GameState = GameState.INITIAL
    
    menuSprites: pygame.sprite.Group
    colorSprites: pygame.sprite.Group

    font: pygame.font.Font

    wonText: pygame.Surface
    lostText: pygame.Surface

    def __init__(self, screen: pygame.Surface, screenWidth: float = 1000, screenHeight: float = 700):
        self.screen = screen
        self.background = pygame.image.load("./Textures/Background/2796727.jpg")
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.wonText = self.font.render("You Won!", True, self.green)
        self.lostText = self.font.render("You Lost!", True, self.black)
        
        self.menuButton = MenuButton(
            startImagePath="./Textures/Menu/start.png",
            restartImagePath="./Textures/Menu/restart.png",
            screenWidth=self.screenWidth,
            screenHeight=self.screenHeight
        )

        self.menuSprites = pygame.sprite.Group(self.menuButton)
        self.colorSprites = pygame.sprite.Group()

    def setScreenSize(self, screenWidth: float, screenHeight: float):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.menuButton.setScreenSize(screenWidth, screenHeight)

    def displayColorOptions(self):
        

    def render(self):
        if (self.isHumanandChoosingColor):
            self.displayColorOptions()
        else if (self.gameState == GameState.PLAYING):

        # else
            self.displayMenu()
            
    def setGameEndText(self, text: pygame.Surface):
        textRect = text.get_rect(center=(self.screenWidth // 2, self.screenHeight // 2 - 100))
        self.screen.blit(text, textRect)

    def displayMenu(self):
        self.menuSprites.draw(self.screen)

        if self.gameState == GameState.PLAYER_WON:
            self.setGameEndText(self.wonText)

        elif self.gameState == GameState.PLAYER_LOST:
            self.setGameEndText(self.lostText)