from Cards.card_types import CardColorType

class AppVariableValueHelper:
    cardDecreaseWidthBy: float = 2
    cardDecreasHeightBy: float = 2
    cardHeight: float
    cardWidth: float
    screenHeight: float
    screenWidth: float
    
    def __init__(self, screenWidth: float, screenHeight: float):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.cardHeight = 200
        self.cardWidth = 100
        
    def cardNameToColor(self, name: str) -> CardColorType:
        if name == "Acorns":
            return CardColorType.ACORN
        if name == "Balls":
            return CardColorType.BELL
        if name == "Green":
            return CardColorType.LEAF
        return CardColorType.HEART