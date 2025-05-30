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
    """
    Main class for managing the game menu, game loop, and rendering.

    Attributes:
        screen (pygame.Surface): The main display surface.
        background (pygame.Surface): The background image.
        startTexture (pygame.Surface): The start button texture.
        menuButton (MenuButton): The menu button instance.
        takeCardButton (Button): The button for taking a card.
        gameManager (GameManager): The main game manager instance.
        gameData (GameData): The shared game state.
        millisecondsBetweenRounds (int): Delay between rounds in milliseconds.
        lastTick (int): Timestamp of the last round.
        menuSprites (pygame.sprite.Group): Sprites for the menu.
        colorSprites (pygame.sprite.Group): Sprites for color selection.
        gameSprites (pygame.sprite.Group): Sprites for in-game UI.
        appVariableHelper (AppVariableValueHelper): Helper for app-wide variables.
        font (pygame.font.Font): Font used for rendering text.
        wonTextSprite (pygame.Surface): Surface for the "You Won!" text.
        lostTextSprite (pygame.Surface): Surface for the "You Lost!" text.
        wonTextRect (pygame.Rect): Rect for positioning the "You Won!" text.
        lostTextRect (pygame.Rect): Rect for positioning the "You Lost!" text.
        clock (pygame.time.Clock): Pygame clock for timing.
    """

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
        """
        Initializes the GameMenu, sets up UI elements, game manager, and state.

        Args:
            screen (pygame.Surface): The main display surface.
            screenWidth (float): Width of the screen.
            screenHeight (float): Height of the screen.
        """
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
        """
        Updates the screen size and repositions menu elements.

        Args:
            screenWidth (float): The new width of the screen.
            screenHeight (float): The new height of the screen.
        """
        self.appVariableHelper.screenWidth = screenWidth
        self.appVariableHelper.screenHeight = screenHeight
        self.menuButton.setPositionDefault()

    def menuButtonClick(self):
        """
        Handles the menu button click event, restarting the game and updating the UI.
        """
        print("Menu button clicked")
        self.gameData = GameData()
        self.gameManager.restartGame(self.gameData)
        self.menuButton.setRestartImage()
        self.gameData.gameState = GameState.PLAYING

    def displayColorOptions(self):
        """
        Draws the color selection options to the screen.
        """
        self.colorSprites.draw(self.screen)

    def render(self):
        """
        Renders the current game or menu state to the screen.
        """
        if (self.gameData.gameState == GameState.PLAYING):
            if (self.gameData.displayColorOptions):
                self.displayColorOptions()
            else:
                self.displayGame()
        else:
            self.displayMenu()

    def reactToClicks(self, events: list[pygame.event.Event]):
        """
        Handles click events and updates the appropriate sprite groups.

        Args:
            events (list[pygame.event.Event]): List of pygame events to process.
        """
        if (self.gameData.displayColorOptions):
            self.colorSprites.update(events)
        elif (self.gameData.gameState == GameState.PLAYING):
            self.gameManager.humanPlayer.displayedSprites.update(events)
            if (not self.gameManager.gameData.userInputReceived):
                self.gameSprites.update(events)
        else:
            self.menuSprites.update(events)
            
    def displayGameEndText(self, textSprite: pygame.Surface, textRect: pygame.Rect):
        """
        Draws the end-of-game text (win/lose) to the screen.

        Args:
            textSprite (pygame.Surface): The text surface to display.
            textRect (pygame.Rect): The rectangle for positioning the text.
        """
        self.screen.blit(textSprite, textRect)

    def displayMenu(self):
        """
        Draws the menu sprites and win/lose text if the game has ended.
        """
        self.menuSprites.draw(self.screen)

        if self.gameData.gameState == GameState.PLAYER_WON:
            self.displayGameEndText(self.wonTextSprite, self.wonTextRect)

        elif self.gameData.gameState == GameState.PLAYER_LOST:
            self.displayGameEndText(self.lostTextSprite, self.lostTextRect)

    def displayGame(self):
        """
        Handles the main game rendering and turn progression logic.
        """
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
        """
        Creates and positions the color selection cards for the color selection UI.
        """
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
        """
        Handles the logic when a color option card is selected by the player.

        Args:
            color (CardColorType): The color selected by the player.
        """
        self.gameData.evaluateColorOptionCard(color)
        self.gameManager.playerOnTurnIndex += 1