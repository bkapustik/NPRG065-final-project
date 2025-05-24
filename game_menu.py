import pygame
from menu_button import MenuButton
from game_manager import GameManager
from Game.game_data import GameData
from enum import Enum
from Cards.color_card import ColorCard
from app_variable_value_helper import AppVariableValueHelper

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
    
    gameState: GameState = GameState.INITIAL
    gameManager: GameManager
    gameData: GameData

    millisecondsBetweenRounds: int = 500
    clock: pygame.time.Clock
    
    menuSprites: pygame.sprite.Group
    colorSprites: pygame.sprite.Group
    appVariableHelper: AppVariableValueHelper

    font: pygame.font.Font

    wonText: pygame.Surface
    lostText: pygame.Surface

    def __init__(self, screen: pygame.Surface, screenWidth: float = 1000, screenHeight: float = 700):
        self.screen = screen
        self.background = pygame.image.load("./Textures/Background/2796727.jpg")
        self.appVariableHelper = AppVariableValueHelper(screenWidth, screenHeight)

        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.wonText = self.font.render("You Won!", True, self.green)
        self.lostText = self.font.render("You Lost!", True, self.black)
        
        self.menuButton = MenuButton(
            startImagePath="./Textures/Menu/start.png",
            restartImagePath="./Textures/Menu/restart.png",
            appVariableHelper=self.appVariableHelper
        )

        self.menuSprites = pygame.sprite.Group(self.menuButton)
        self.colorSprites = pygame.sprite.Group()
        self.createColorOptions()

        self.clock = pygame.time.Clock()
        self.gameData = GameData()
        self.gameManager = GameManager(self.colorSprites, self.gameData)

    def setScreenSize(self, screenWidth: float, screenHeight: float):
        self.appVariableHelper.screenWidth = screenWidth
        self.appVariableHelper.screenHeight = screenHeight
        self.menuButton.setPosition()

    def displayColorOptions(self):
        self.colorSprites.draw(self.screen)

    def render(self):
        if (True):
            self.displayColorOptions()
        elif (self.gameState == GameState.PLAYING):
            self.displayGame()
        else:
            self.displayMenu()
            
    def setGameEndText(self, text: pygame.Surface):
        textRect = text.get_rect(center=(self.appVariableHelper.screenWidth // 2, self.appVariableHelper.screenHeight // 2 - 100))
        self.screen.blit(text, textRect)

    def displayMenu(self):
        self.menuSprites.draw(self.screen)

        if self.gameState == GameState.PLAYER_WON:
            self.setGameEndText(self.wonText)

        elif self.gameState == GameState.PLAYER_LOST:
            self.setGameEndText(self.lostText)

    def displayGame(self):
        if (self.clock.get_time() > self.millisecondsBetweenRounds and
             self.gameManager.userInputReceived
        ):
            if (self.gameData.playerHasFinished):
                self.gameState = GameState.PLAYER_WON

    def createColorOptions(self):
        colors = ["Acorns", "Balls", "Green", "Heart"]
        #colorOptionHeight = colorOptionWidth * 2
        spaceBetweenColorOptions = 50
        xPositionRelativeToCenter = -(self.appVariableHelper.cardWidth * 2 + spaceBetweenColorOptions * 1.5)

        for color in colors:
            colorType = self.appVariableHelper.cardNameToColor(color)
            colorCard = ColorCard(
                colorType,
                "./Textures/Colors/" + color + ".jpg",
                self.appVariableHelper.screenWidth / 2 + xPositionRelativeToCenter,
                self.appVariableHelper.screenHeight / 2,
                self.appVariableHelper.cardWidth,
                self.appVariableHelper.cardHeight)
            self.colorSprites.add(colorCard)
            xPositionRelativeToCenter += self.appVariableHelper.cardHeight + spaceBetweenColorOptions