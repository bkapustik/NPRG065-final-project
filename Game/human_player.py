from Game.player import Player
from Cards.cards import Card

class HumanPlayer(Player):
    def __init__(self, firstCardPosition: tuple[float, float], appVariableValueHelper):
        super().__init__(firstCardPosition)

    def tryChooseAColor(self):
        return False
    
    def takeCards(self, cards: list[Card]):
        shiftXBy = 0
        self.displayedSprites.empty()
        for card in cards:
            card.rotateCard()
            self.cards.append(card)
        for card in self.cards:
            card.setPosition(self.firstCardPosition[0] + shiftXBy, self.firstCardPosition[1])
            shiftXBy += 125
            self.displayedSprites.add(card)
            
