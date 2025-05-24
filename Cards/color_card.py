from Cards.card_types import CardColorType
from Sprites.clickable_sprite import ClickableSprite

class ColorCard(ClickableSprite):
    color: CardColorType

    def __init__(self, color: CardColorType, imgPath: str, x: float, y: float, width: float, height: float):
        super().__init__(imgPath, x, y, width, height)
        self.color = color