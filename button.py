import pygame
from app_variable_value_helper import AppVariableValueHelper
from typing import Callable

class Button(pygame.sprite.Sprite):
    rect: pygame.Rect
    callback: Callable[[], None]

    def __init__(self, appVariableHelper: AppVariableValueHelper, font: pygame.font.Font):
        super().__init__()
        self.image = font.render("Take a card!", True, (0, 255, 0))
        self.rect = self.image.get_rect(center=(appVariableHelper.screenWidth / 2, appVariableHelper.screenHeight / 2 - 250))
        self.callback = None

    def update(self, events: list[pygame.event.Event]):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    if self.callback is not None:
                        self.callback()