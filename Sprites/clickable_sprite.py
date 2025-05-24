import pygame
from typing import Callable

class ClickableSprite(pygame.sprite.Sprite):
    rect: pygame.Rect
    callback: Callable[[], None]

    def __init__(self, imgPath: str, x: float, y: float, width: float, height: float):
        super().__init__()
        self.image = pygame.image.load(imgPath).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, events: list[pygame.event.Event]):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback()