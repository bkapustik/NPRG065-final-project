import pygame

class MenuButton(pygame.sprite.Sprite):
    startImage: pygame.Surface
    restartImage: pygame.Surface
    screenWidth: float
    screenHeight: float

    def __init__(self, startImagePath: str, restartImagePath: str, screenWidth: float, screenHeight: float):
        super().__init__()
        
        self.startImage = pygame.image.load(startImagePath).convert_alpha()
        self.restartImage = pygame.image.load(restartImagePath).convert_alpha()
        
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.setStartImage()
        self.setPosition()

    def setStartImage(self):
        self.image = self.startImage
        self.setPosition()

    def setRestartImage(self):
        self.image = self.restartImage
        self.setPosition()

    def setPosition(self):
        self.rect = self.image.get_rect(center=(self.screenWidth / 2, self.screenHeight / 2))

    def setScreenSize(self, screenWidth: float, screenHeight: float):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.setPosition()