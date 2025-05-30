from Cards.card_types import CardColorType
from Sprites.clickable_sprite import ClickableSprite
from typing import Callable
import pygame

class ColorCard(ClickableSprite):
    """
    Represents a clickable color card used for color selection in the game.

    Attributes:
        color (CardColorType): The color represented by this card.
        colorCardCallBack (Callable[[CardColorType], None]): Callback function called when the card is clicked.
    """
    color: CardColorType
    colorCardCallBack: Callable[[CardColorType], None]

    def __init__(self, color: CardColorType, imgPath: str, x: float, y: float, width: float, height: float):
        """
        Initializes a ColorCard instance.

        Args:
            color (CardColorType): The color represented by this card.
            imgPath (str): Path to the image representing the card.
            x (float): The x-coordinate of the card's center.
            y (float): The y-coordinate of the card's center.
            width (float): The width of the card.
            height (float): The height of the card.
        """
        super().__init__(imgPath, x, y, width, height)
        self.color = color

    def update(self, events: list[pygame.event.Event]):
        """
        Handles mouse events for the color card, triggering the callback if clicked.

        Args:
            events (list[pygame.event.Event]): List of pygame events to process.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    if (self.colorCardCallBack is not None):
                        self.colorCardCallBack(self.color)