import pygame
from app_variable_value_helper import AppVariableValueHelper
from typing import Callable

class Button(pygame.sprite.Sprite):
    """
    A clickable button sprite rendered with text, used for user interaction in the game.

    Attributes:
        rect (pygame.Rect): The rectangle representing the button's position and size.
        callback (Callable[[], None]): The function to call when the button is clicked.
    """
    rect: pygame.Rect
    callback: Callable[[], None]

    def __init__(self, appVariableHelper: AppVariableValueHelper, font: pygame.font.Font):
        """
        Initializes a Button instance.

        Args:
            appVariableHelper (AppVariableValueHelper): Helper for application-wide variables (e.g., screen size).
            font (pygame.font.Font): The font used to render the button text.
        """
        super().__init__()
        self.image = font.render("Take a card!", True, (0, 255, 0))
        self.rect = self.image.get_rect(center=(appVariableHelper.screenWidth / 2, appVariableHelper.screenHeight / 2 - 250))
        self.callback = None

    def update(self, events: list[pygame.event.Event]):
        """
        Handles mouse events and calls the callback if the button is clicked.

        Args:
            events (list[pygame.event.Event]): List of pygame events to process.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    if self.callback is not None:
                        self.callback()