import pygame
from typing import Callable

class ClickableSprite(pygame.sprite.Sprite):
    """
    A pygame sprite that can be clicked and can execute a callback function.

    Attributes:
        rect (pygame.Rect): The rectangle representing the sprite's position and size.
        callback (Callable[[], None]): The function to call when the sprite is clicked.
    """

    rect: pygame.Rect
    callback: Callable[[], None]

    def __init__(self, imgPath: str, x: float, y: float, width: float, height: float):
        """
        Initializes a ClickableSprite.

        Args:
            imgPath (str): Path to the image file for the sprite.
            x (float): The x-coordinate of the sprite's center.
            y (float): The y-coordinate of the sprite's center.
            width (float): The width of the sprite.
            height (float): The height of the sprite.
        """
        super().__init__()
        self.image = pygame.image.load(imgPath).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))
        self.rect = self.image.get_rect(center=(x, y))
        self.callback = None

    def update(self, events: list[pygame.event.Event]):
        """
        Handles mouse events and calls the callback if the sprite is clicked.

        Args:
            events (list[pygame.event.Event]): List of pygame events to process.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    if self.callback is not None:
                        self.callback()

    def setPosition(self, x: float, y: float):
        """
        Sets the position of the sprite.

        Args:
            x (float): The new x-coordinate of the sprite's center.
            y (float): The new y-coordinate of the sprite's center.
        """
        self.rect = self.image.get_rect(center=(x, y))