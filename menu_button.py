import pygame
from app_variable_value_helper import AppVariableValueHelper

class MenuButton(pygame.sprite.Sprite):
    startImage: pygame.Surface
    restartImage: pygame.Surface
    appVariableValueHelper: AppVariableValueHelper

    def __init__(self, startImagePath: str, restartImagePath: str, appVariableHelper: AppVariableValueHelper):
        super().__init__()
        
        self.startImage = pygame.image.load(startImagePath).convert_alpha()
        self.restartImage = pygame.image.load(restartImagePath).convert_alpha()
        
        self.appVariableValueHelper = appVariableHelper

        self.setStartImage()
        self.setPosition()

    def setStartImage(self):
        self.image = self.startImage
        self.setPosition()

    def setRestartImage(self):
        self.image = self.restartImage
        self.setPosition()

    def setPosition(self):
        self.rect = self.image.get_rect(center=(self.appVariableValueHelper.screenWidth / 2, self.appVariableValueHelper.screenHeight / 2))