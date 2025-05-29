import pygame
from menu_button import MenuButton
from button import Button
from game_manager import GameManager
from Game.game_data import GameData
from Game.game_data import GameState
from Cards.color_card import ColorCard
from Cards.card_types import CardColorType
from app_variable_value_helper import AppVariableValueHelper

class GameMenu:
    green = (0, 255, 0)
    black = (0, 0, 0)    

    screen: pygame.Surface
    background: pygame.Surface
    startTexture: pygame.Surface
    menuButton: MenuButton
    takeCardButton: Button
    
    gameManager: GameManager
    gameData: GameData

    millisecondsBetweenRounds: int = 500
    lastTick: int = 0
    
    menuSprites: pygame.sprite.Group
    colorSprites: pygame.sprite.Group
    gameSprites: pygame.sprite.Group
    appVariableHelper: AppVariableValueHelper

    font: pygame.font.Font

    wonTextSprite: pygame.Surface
    lostTextSprite: pygame.Surface
    wonTextRect: pygame.Rect
    lostTextRect: pygame.Rect

    def __init__(self, screen: pygame.Surface, screenWidth: float, screenHeight: float):
        self.screen = screen
        self.background = pygame.image.load("./Textures/Background/2796727.jpg")
        self.appVariableHelper = AppVariableValueHelper(screenWidth, screenHeight)

        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.wonTextSprite = self.font.render("You Won!", True, self.green)
        self.lostTextSprite = self.font.render("You Lost!", True, self.black)
        
        self.wonTextRect = self.wonTextSprite.get_rect(center=(self.appVariableHelper.screenWidth // 2, self.appVariableHelper.screenHeight // 2 - 100))
        self.lostTextRect = self.lostTextSprite.get_rect(center=(self.appVariableHelper.screenWidth // 2, self.appVariableHelper.screenHeight // 2 - 100))
        
        self.menuButton = MenuButton(
            startImagePath="./Textures/Menu/start.png",
            restartImagePath="./Textures/Menu/restart.png",
            appVariableHelper=self.appVariableHelper
        )

        self.takeCardButton = Button(
            self.appVariableHelper,
            self.font
        )

        self.menuSprites = pygame.sprite.Group(self.menuButton)
        self.colorSprites = pygame.sprite.Group()
        self.gameSprites = pygame.sprite.Group(self.takeCardButton)

        self.clock = pygame.time.Clock()
        self.gameData = GameData()
        self.createColorOptions()
        self.gameManager = GameManager(self.colorSprites, self.gameData, self.appVariableHelper)
        self.menuButton.callback = self.menuButtonClick
        self.takeCardButton.callback = self.gameManager.evaluateTakeCardButtonClick

    def setScreenSize(self, screenWidth: float, screenHeight: float):
        self.appVariableHelper.screenWidth = screenWidth
        self.appVariableHelper.screenHeight = screenHeight
        self.menuButton.setPositionDefault()

    def menuButtonClick(self):
        print("Menu button clicked")
        self.gameData = GameData()
        self.gameManager.restartGame(self.gameData)
        self.menuButton.setRestartImage()
        self.gameData.gameState = GameState.PLAYING

    def displayColorOptions(self):
        self.colorSprites.draw(self.screen)

    def render(self):
        if (self.gameData.displayColorOptions):
            self.displayColorOptions()
        elif (self.gameData.gameState == GameState.PLAYING):
            self.displayGame()
        else:
            self.displayMenu()

    def reactToClicks(self, events: list[pygame.event.Event]):
        if (self.gameData.displayColorOptions):
            self.colorSprites.update(events)
        elif (self.gameData.gameState == GameState.PLAYING):
            self.gameManager.humanPlayer.displayedSprites.update(events)
            if (not self.gameManager.gameData.userInputReceived):
                self.gameSprites.update(events)
        else:
            self.menuSprites.update(events)
            
    def displayGameEndText(self, textSprite: pygame.Surface, textRect: pygame.Rect):
        self.screen.blit(textSprite, textRect)

    def displayMenu(self):
        self.menuSprites.draw(self.screen)

        if self.gameData.gameState == GameState.PLAYER_WON:
            self.displayGameEndText(self.wonTextSprite, self.wonTextRect)

        elif self.gameData.gameState == GameState.PLAYER_LOST:
            self.displayGameEndText(self.lostTextSprite, self.lostTextRect)

    def displayGame(self):
        currentTime = pygame.time.get_ticks()
        if (currentTime > self.millisecondsBetweenRounds + self.lastTick and
             self.gameData.userInputReceived
        ):
            if (self.gameData.playerHasFinished):
                self.gameData.gameState = GameState.PLAYER_WON
            else:
                self.gameManager.playOneTurn()
                if (len(self.gameManager.players) <= 1):
                    self.gameData.gameState = GameState.PLAYER_LOST
            self.lastTick = currentTime

        self.gameManager.render(self.screen)
        if not self.gameData.userInputReceived:
            self.gameSprites.draw(self.screen)

    def createColorOptions(self):
        colors = ["Acorns", "Balls", "Green", "Heart"]
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
            
            colorCard.colorCardCallBack = self.evaluateColorOptionCard

    def evaluateColorOptionCard(self, color: CardColorType):
        self.gameData.evaluateColorOptionCard(color)
        self.gameManager.playerOnTurnIndex += 1