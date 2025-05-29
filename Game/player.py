from Cards.cards import Card
import pygame

class Player:
    isOnTurn: bool
    hasFinished: bool
    firstCardPosition: tuple[float, float]
    cards: list[Card]
    displayedSprites: pygame.sprite.Group

    def __init__(self, firstCardPosition: tuple[float, float]):
        self.firstCardPosition = firstCardPosition
        self.displayedSprites = pygame.sprite.Group()
        self.isOnTurn = False
        self.hasFinished = False
        self.cards = []

    def tryChooseAColor(self):
        return False
    
    def tryPlayCard(self, topDeckCard: Card) -> Card | None:
        return None
    
    def takeCards(self, cards: list[Card]):
        pass

    def checkHasFinished(self) -> bool:
        if len(self.cards) == 0:
            self.hasFinished = True
        return self.hasFinished