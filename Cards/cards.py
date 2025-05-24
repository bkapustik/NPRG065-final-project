from Cards.card_types import CardColorType
from Cards.card_types import CardNumberType
from Sprites.clickable_sprite import ClickableSprite
from app_variable_value_helper import AppVariableValueHelper

class Card(ClickableSprite):
    color: CardColorType
    number: CardNumberType
    allowFunction: bool = False

    def __init__(self, imgPath: str, x: float, y: float, color: CardColorType, number: CardNumberType, appVariableHelper: AppVariableValueHelper):
        super().__init__(imgPath, x, y, appVariableHelper.cardWidth, appVariableHelper.cardHeight)
        self.color = color
        self.number = number