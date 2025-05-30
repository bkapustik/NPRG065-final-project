import pygame
from app_variable_value_helper import AppVariableValueHelper
from Sprites.clickable_sprite import ClickableSprite

class MenuButton(ClickableSprite):
    """
    A button sprite for the game menu, supporting start and restart images.

    Attributes:
        startImage (pygame.Surface): The image for the start button.
        restartImage (pygame.Surface): The image for the restart button.
        appVariableValueHelper (AppVariableValueHelper): Helper for application-wide variables.
    """
    startImage: pygame.Surface
    restartImage: pygame.Surface
    appVariableValueHelper: AppVariableValueHelper

    def __init__(self, startImagePath: str, restartImagePath: str, appVariableHelper: AppVariableValueHelper):
        """
        Initializes a MenuButton instance.

        Args:
            startImagePath (str): Path to the start button image.
            restartImagePath (str): Path to the restart button image.
            appVariableHelper (AppVariableValueHelper): Helper for application-wide variables.
        """
        super().__init__(startImagePath, appVariableHelper.screenWidth / 2, appVariableHelper.screenHeight / 2, 400, 100)
        self.startImage = pygame.image.load(startImagePath).convert_alpha()
        self.restartImage = pygame.image.load(restartImagePath).convert_alpha()
        self.appVariableValueHelper = appVariableHelper
        self.setPositionDefault()

    def setStartImage(self):
        """
        Sets the button image to the start image and repositions the button.
        """
        self.image = self.startImage
        self.setPositionDefault()

    def setRestartImage(self):
        """
        Sets the button image to the restart image and repositions the button.
        """
        self.image = self.restartImage
        self.setPositionDefault()

    def setPositionDefault(self):
        """
        Sets the button's position to the center of the screen based on current screen dimensions.
        """
        self.setPosition(self.appVariableValueHelper.screenWidth / 2, self.appVariableValueHelper.screenHeight / 2)