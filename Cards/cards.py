from Cards.card_types import CardColorType
from Cards.card_types import CardNumberType
from Sprites.clickable_sprite import ClickableSprite
from app_variable_value_helper import AppVariableValueHelper
import pygame
from typing import Callable

class Card(ClickableSprite):
    """
    Represents a playing card in the game.

    Attributes:
        color (CardColorType): The color (suit) of the card.
        number (CardNumberType): The number (rank) of the card.
        frontImgPath (str): Path to the front image of the card.
        backImgPath (str): Path to the back image of the card.
        isFaceUp (bool): Whether the card is currently face up.
        x (float): The x-coordinate of the card's center.
        y (float): The y-coordinate of the card's center.
        appVariableValueHelper (AppVariableValueHelper): Helper for app-wide variables.
        cardClickCallBack (Callable[['Card'], None]): Callback for when the card is clicked.
    """
    color: CardColorType
    number: CardNumberType
    frontImgPath: str
    backImgPath: str
    isFaceUp: bool
    x: float
    y: float
    appVariableValueHelper: AppVariableValueHelper
    cardClickCallBack: Callable[['Card'], None]

    def __init__(self, backImgPath: str, frontImgPath: str, x: float, y: float, color: CardColorType, number: CardNumberType, appVariableHelper: AppVariableValueHelper
    ):
        """
        Initializes a Card instance.

        Args:
            backImgPath (str): Path to the back image of the card.
            frontImgPath (str): Path to the front image of the card.
            x (float): The x-coordinate of the card's center.
            y (float): The y-coordinate of the card's center.
            color (CardColorType): The color (suit) of the card.
            number (CardNumberType): The number (rank) of the card.
            appVariableHelper (AppVariableValueHelper): Helper for app-wide variables.
        """
        super().__init__(backImgPath, x, y, appVariableHelper.cardWidth, appVariableHelper.cardHeight)
        self.color = color
        self.number = number
        self.frontImgPath = frontImgPath
        self.backImgPath = backImgPath
        self.appVariableValueHelper = appVariableHelper
        self.x = x
        self.y = y
        self.isFaceUp = False

    def rotateCard(self):
        """
        Flips the card between face up and face down, updating its image accordingly.
        """
        if self.isFaceUp:
            self.image = pygame.image.load(self.backImgPath).convert_alpha()
        else:
            self.image = pygame.image.load(self.frontImgPath).convert_alpha()

        self.image = pygame.transform.scale(self.image, (int(self.appVariableValueHelper.cardWidth), int(self.appVariableValueHelper.cardHeight)))
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.isFaceUp = not self.isFaceUp

    def update(self, events: list[pygame.event.Event]):
        """
        Handles mouse events for the card, triggering the click callback if the card is face up and clicked.

        Args:
            events (list[pygame.event.Event]): List of pygame events to process.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    if self.isFaceUp:
                        if self.cardClickCallBack is not None:
                            self.cardClickCallBack(self)