from Cards.card_types import CardColorType
from Sprites.clickable_sprite import ClickableSprite
from typing import Callable
import pygame

class ColorCard(ClickableSprite):
    color: CardColorType
    colorCardCallBack: Callable[[CardColorType], None]

    def __init__(self, color: CardColorType, imgPath: str, x: float, y: float, width: float, height: float):
        super().__init__(imgPath, x, y, width, height)
        self.color = color

    def update(self, events: list[pygame.event.Event]):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    if (self.colorCardCallBack is not None):
                        self.colorCardCallBack(self.color)