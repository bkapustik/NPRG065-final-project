from Cards.card_types import CardColorType
from Cards.card_types import CardNumberType
from Sprites.clickable_sprite import ClickableSprite
from app_variable_value_helper import AppVariableValueHelper
import pygame
from typing import Callable

class Card(ClickableSprite):
    color: CardColorType
    number: CardNumberType
    frontImgPath: str
    backImgPath: str
    isFaceUp: bool
    x: float
    y: float
    appVariableValueHelper: AppVariableValueHelper
    cardClickCallBack: Callable[['Card'], None]

    def __init__(self, backImgPath: str, frontImgPath: str, x: float, y: float, color: CardColorType, number: CardNumberType, appVariableHelper: AppVariableValueHelper):
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
        if self.isFaceUp:
            self.image = pygame.image.load(self.backImgPath).convert_alpha()
        else:
            self.image = pygame.image.load(self.frontImgPath).convert_alpha()

        self.image = pygame.transform.scale(self.image, (int(self.appVariableValueHelper.cardWidth), int(self.appVariableValueHelper.cardHeight)))
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.isFaceUp = not self.isFaceUp

    def update(self, events: list[pygame.event.Event]):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    if self.isFaceUp:
                        if self.cardClickCallBack is not None:
                            self.cardClickCallBack(self)