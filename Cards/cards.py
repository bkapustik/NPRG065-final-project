from Cards.card_types import CardColorType
from Cards.card_types import CardNumberType
from Game.game_data import GameData
from Sprites.clickable_sprite import ClickableSprite

class Card(ClickableSprite):
    color: CardColorType
    number: CardNumberType

    def __init__(self, imgPath: str, x: float, y: float, color: CardColorType, number: CardNumberType):
        super().__init__(imgPath, x, y)
        self.color = color
        self.number = number