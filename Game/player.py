from Cards.cards import Card

class Player:
    isOnTurn: bool = False
    hasFinished: bool = False
    firstCardPosition: tuple[float, float]
    cards: list[Card] = []

    def __init__(self, firstCardPosition: tuple[float, float]):
        self.firstCardPosition = firstCardPosition

    def setOnTurn(self):
        self.isOnTurn = True

    def wantsCustomTurn(self):
        return False
    
    def tryChooseAColor(self):
        return False